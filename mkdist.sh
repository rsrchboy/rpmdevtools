#!/bin/bash

#
# Helper script for creating the fedora-rpmdevtools dist tarball.
# $Id: mkdist.sh,v 1.2 2004/04/01 19:31:08 scop Exp $
#
# Author:  Ville Skyttä <ville.skytta at iki.fi>
# License: GPL
#

set -e

trap cleanup EXIT
tmpdir=

cleanup()
{
    [ -z "$tmpdir" ] || rm -rf "$tmpdir"
}

if [ -z "$1" ] ; then
    echo "Usage: $0 <version>" >&2
    exit 1
fi

pwd=`pwd`
tmpdir=`mktemp -d /tmp/rpmdevtools.XXXXXX`
mkdir -p $tmpdir/fedora-rpmdevtools-$1
cp -pR * $tmpdir/fedora-rpmdevtools-$1
find $tmpdir -type d -name CVS | xargs -r rm -rf
rm -f $tmpdir/fedora-rpmdevtools-$1/mkdist.sh
find $tmpdir/fedora-rpmdevtools-$1 -type d | xargs chmod 0755
find $tmpdir/fedora-rpmdevtools-$1 -type f | xargs chmod 0644
cd $tmpdir
tar --owner=0 --group=0 -jcvf \
  $pwd/fedora-rpmdevtools-$1.tar.bz2 fedora-rpmdevtools-$1
cd $pwd
