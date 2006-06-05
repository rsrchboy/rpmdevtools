#!/bin/sh

err=
kmodhelper=${1:-../fedora-kmodhelper}

t ()
{
    res=`$kmodhelper $1`
    if ! test "$res" = "$2" ; then
        cat <<EOF >&2
Error (fedora-kmodhelper $1):
  expected '$2', got '$res'
EOF
        err=1
    fi
}

t "variant -u 2.4.22-1.2149.nptl" ""
t "variant -u 2.4.22-1.2149.nptlcustom" ""
t "variant -u 2.4.22-1.2149.nptlcustomsmp" "smp"
t "variant -u 2.4.22-1.2149.nptlsmpcustom" ""
t "variant -u 2.4.22-1.2149.nptlsmpcustomdebug" "debug"
t "variant -u 2.4.22-1.2149.nptldebugsmp" "smp"

t "verrel -u 2.4.22-1.2149.nptl" "2.4.22-1.2149.nptl"
t "verrel -u 2.4.22-1.2149.nptlcustom" "2.4.22-1.2149.nptl"
t "verrel -u 2.4.22-1.2149.nptlcustomsmp" "2.4.22-1.2149.nptl"
t "verrel -u 2.4.22-1.2149.nptlsmpcustom" "2.4.22-1.2149.nptlsmp"
t "verrel -u 2.4.22-1.2149.nptlsmpcustomdebug" "2.4.22-1.2149.nptlsmp"
t "verrel -u 2.4.22-1.2149.nptldebugsmp" "2.4.22-1.2149.nptldebug"

t "version -u 2.4.22-1.2149.nptl" "2.4.22"
t "version -u 2.6.0-pre1-1bigmem" "2.6.0-pre1"
t "version -u 2.6.1-1" "2.6.1"

if [ -z "$err" ] ; then
    echo "All tests successful."
else
    echo "Some tests failed."
    exit 1
fi
