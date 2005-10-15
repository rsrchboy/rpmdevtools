#! /bin/bash

: ${CC:=gcc}
: ${CFLAGS:=-O2 -g3}
: ${srcdir:=.}

COL_BOLD=
COL_NORMAL=
COL_PANIC=
COL_OK=
COL_FAIL=
COL_TEST=
COL_NONE=
MOVE_TO_COL=$(echo -en "\t")


indent=""
count_total=0
count_ok=0
count_fail=0

# Usage: panic <msg>
function panic() {
    echo "$COL_PANIC""$@""$COL_NONE" >&2
    exit 1
}

function tellOk() {
    echo "$MOVE_TO_COL${COL_OK}OK$COL_NONE"
    let ++count_ok
}

function tellFail() {
    echo "$MOVE_TO_COL${COL_FAIL}FAIL$COL_NONE"
    let ++count_fail
}

function tellTest() {
    echo -n "$indent$COL_TEST""$@""$COL_NONE"
    let ++count_total
}

function tellTestGroup()
{
    echo "$indent$COL_TEST""$@""$COL_NONE"
    indent="$indent  "
}

function tellTestGroupEnd()
{
    indent=${indent:2}
}

function tellResult()
{
    echo "${COL_BOLD}Result:$COL_NORMAL $COL_TEST$count_total$COL_NONE tests total, $COL_FAIL$count_fail$COL_NONE failed, $COL_OK$count_ok$COL_NONE succeeded"
    test $count_fail -eq 0
}

function initcolors() {
    ! tty -s || {
	COL_PANIC=$(echo -en "\e[1;33;41m")
	COL_OK=$(echo -en "\e[0;32m")
	COL_FAIL=$(echo -en "\e[0;31m")
	COL_TEST=$(echo -en "\e[0;34m")
	COL_NONE=$(echo -en "\e[m")
	COL_BOLD=$(echo -en "\e[1m")
	COL_NORMAL=$(echo -en "\e[1m")
	MOVE_TO_COL=$(echo -en "\e[60G\t")
    }
}

tmpdir=$(mktemp -d /tmp/rpath-test.XXXXXX)
mkdir -p $tmpdir
trap "rm -rf $tmpdir" EXIT


initcolors

set -e

## create the test objects
tellTest "Creating sourcefiles"

cat >$tmpdir/libok.c <<"EOF"
#include <unistd.h>
int foo() { write(1, "OK\n", 3);   return 0; }
EOF

cat >$tmpdir/libfail.c <<"EOF"
#include <unistd.h>
int foo() { write(1, "FAIL\n", 5); return 1; }
EOF


cat >$tmpdir/test.c <<"EOF"
extern int foo();
int main() { return foo(); }
EOF

tellOk

## create the libraries
tellTest "Creating the libraries"

mkdir -p $tmpdir/lib{ok,fail}
$CC $CFLAGS -fpic -shared $tmpdir/libok.c   -o $tmpdir/libok/librpathtest.so
$CC $CFLAGS -fpic -shared $tmpdir/libfail.c -o $tmpdir/libfail/librpathtest.so

tellOk

## and some scenarios
tellTest "Creating some scenarios"
mkdir $tmpdir/scenarios
(
    cd $tmpdir/scenarios
    mkdir -p 1/usr/{dir1,dir2/{lib,dir1}}
    ln -s dir2/lib/ 1/usr/lib
    
    ln ../libok/*.so   1/usr/dir1/
    ln ../libfail/*.so 1/usr/dir2/dir1/

### this creates:
#   .
#   |-- dir1
#   |   `-- librpathtest.so      [ok]
#   |-- dir2
#   |   |-- dir1
#   |   |   `-- librpathtest.so  [fail]
#   |   `-- lib
#   `-- lib -> dir2/lib/
)

tellOk


## and the programs
function compile() {
    local name=$1
    shift
    tellTest "compiling $name"
    $CC $CFLAGS $tmpdir/test.c -o $tmpdir/$name "$@" -L $tmpdir/libok -lrpathtest && tellOk || tellFail
}

mkdir -p $tmpdir/{ok,fail}

tellTestGroup "Compiling the good programs"
    compile ok/link-0
    compile ok/link-1 -Wl,-rpath='/usr/lib/foo'
    compile ok/link-2 -Wl,-rpath='/usr/lib/foo' -Wl,-rpath='/usr/lib/bar'
    compile ok/link-3 -Wl,-rpath='$ORIGIN'
    compile ok/link-4 -Wl,-rpath='$ORIGIN/..'
    compile ok/link-5 -Wl,-rpath='$ORIGIN/../text'
    compile ok/link-6 -Wl,-rpath='$ORIGIN/../..'
    compile ok/link-7 -Wl,-rpath='$ORIGIN/../../test'
    compile ok/exec-0 -Wl,-rpath='$ORIGIN/../libok'
    compile ok/exec-1 -Wl,-rpath='$ORIGIN/../scenarios/1/usr/dir1'
tellTestGroupEnd

tellTest "Checking the good programs"
    export RPM_BUILD_ROOT=$tmpdir
    bash $srcdir/check-rpaths-worker $tmpdir/ok/* && tellOk || tellFail

tellTestGroup "Compiling the bad programs"
    compile fail/link-0 -Wl,-rpath='/usr/lib'
    compile fail/link-1 -Wl,-rpath='.'
    compile fail/link-2 -Wl,-rpath=''
    compile fail/link-3 -Wl,-rpath='$ORIGIN/test/../libok'
    compile fail/exec-0 -Wl,-rpath='$ORIGIN/../scenarios/1/usr/lib/../dir1'
tellTestGroupEnd
    
tellTestGroup "Checking the bad programs"
    export RPM_BUILD_ROOT=$tmpdir
    bash $srcdir/check-rpaths-worker $tmpdir/fail/* 2>$tmpdir/err >/dev/null || :
    
# check whether all errors were detected
for i in '0001 link-0' '0004 link-1' '0010 link-2' '0020 link-3' '0020 exec-0'; do
    set -- $i
    tellTest "checking for error $1 in $2"
    grep -q "^ERROR *$1:.*'/fail/$2'" $tmpdir/err && tellOk || tellFail
done
tellTestGroupEnd

## check some paths manually for referencing '..'
tellTestGroup "Checking some paths for error 0x0020"
    set --
    . $srcdir/check-rpaths-worker

    tellTestGroup "Checking good paths"
    # good paths
    for i in '/' '/..' '/test' '/test/foo' '/test/...' '/test/.../foo' \
	     'foo/bar/...' \
	     '$ORIGIN/..' '$ORIGIN/../..' '$ORIGIN/../' '$ORIGIN/../../' \
	     '$ORIGIN' '$ORIGIN/foo' '$ORIGIN/../foo'; do
	 tellTest "checking '$i'"
         ! expr match "$i" "$BADNESS_EXPR_32" >/dev/null && tellOk || tellFail
    done
    tellTestGroupEnd

    # bad paths
    tellTestGroup "Checking bad paths"
    for i in '/usr/lib/..' '/usr/lib/../lib64' \
	     '$ORIGIN/lib/..'    '$ORIGIN/lib/../' \
	     '$ORIGIN/lib/../..' '$ORIGIN/lib/../../' \
	     '$ORIGIN/lib/../lib64' '$ORIGIN/lib/../../lib64' \
	     '$ORIGIN/../lib/..'       '$ORIGIN/../lib/../'      '$ORIGIN/../lib/../foo' \
	     '$ORIGIN/../lib/../..'    '$ORIGIN/../lib/../..'    '$ORIGIN/../lib/../../foo' \
	     '$ORIGIN/../../lib/..'    '$ORIGIN/../../lib/../'   '$ORIGIN/../../lib/../foo' \
	     '$ORIGIN/../../lib/../..' '$ORIGIN/../../lib/../..' '$ORIGIN/../../lib/../../foo' \
	     ; do
	 tellTest "checking '$i'"
         expr match "$i" "$BADNESS_EXPR_32" >/dev/null && tellOk || tellFail
    done
    tellTestGroupEnd
tellTestGroupEnd

tellResult
