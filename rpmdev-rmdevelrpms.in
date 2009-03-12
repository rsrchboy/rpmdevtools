#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# rpmdev-rmdevelrpms -- Find (and optionally remove) "development" RPMs
#
# Copyright (c) 2004-2009 Ville Skyttä <ville.skytta at iki.fi>
# Credits: Seth Vidal (yum), Thomas Vander Stichele (mach)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


import optparse
import os
import re
import stat
import sys
import types

import rpm


__version__ = "1.12"


dev_re  = re.compile("-(?:de(?:buginfo|vel)|sdk|static)\\b", re.IGNORECASE)
test_re = re.compile("^perl-(?:Devel|ExtUtils|Test)-")
lib_re1 = re.compile("^lib.+")
lib_re2 = re.compile("-libs?$")
a_re    = re.compile("\\w\\.a$")
so_re   = re.compile("\\w\\.so(?:\\.\\d+)*$")
comp_re = re.compile("^compat-gcc")
# required by Ant, which is required by Eclipse...
jdev_re = re.compile("^java-.+-gcj-compat-devel$")


def_devpkgs =\
("autoconf", "autoconf213", "automake", "automake14", "automake15",
 "automake16", "automake17", "bison", "byacc", "cmake", "dev86", "djbfft",
 "docbook-utils-pdf", "doxygen", "flex", "gcc-g77", "gcc-gfortran", "gcc-gnat",
 "gcc-objc", "gcc32", "gcc34", "gcc34-c++", "gcc34-java", "gcc35", "gcc35-c++",
 "gcc4", "gcc4-c++", "gcc4-gfortran", "gettext", "glade", "glade2", "imake",
 "intltool", "kernel-source", "kernel-sourcecode", "libtool", "m4", "nasm",
 "perl-Module-Build", "pkgconfig", "qt-designer", "scons", "swig", "texinfo",
 "yasm",
 )

def_nondevpkgs =\
("glibc-devel", "libstdc++-devel", "vamp-plugin-sdk",
 )


devpkgs = ()
nondevpkgs = ()
qf = '%{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}'

def isDevelPkg(hdr):
    """
    Decides whether a package is a devel one, based on name, configuration
    and contents.
    """
    if not hdr: return 0
    name = hdr[rpm.RPMTAG_NAME]
    if not name: return 0
    na = "%s.%s" % (name, hdr[rpm.RPMTAG_ARCH])
    # Check nondevpkgs first (exclusion overrides inclusion)
    if name in nondevpkgs or na in nondevpkgs: return 0
    if name in devpkgs or na in devpkgs: return 1
    if name in def_nondevpkgs or na in def_nondevpkgs: return 0
    if name in def_devpkgs or na in def_devpkgs: return 1
    if jdev_re.search(name): return 0
    if dev_re.search(name): return 1
    if test_re.search(name): return 1
    if comp_re.search(name): return 1
    if lib_re1.search(name) or lib_re2.search(name):
        # Heuristics for lib*, *-lib and *-libs packages (kludgy...)
        a_found = so_found = 0
        fnames = hdr[rpm.RPMTAG_FILENAMES]
        fmodes = hdr[rpm.RPMTAG_FILEMODES]
        for i in range(len(fnames)):
            # Peek into the files in the package.
            if not (stat.S_ISLNK(fmodes[i]) or stat.S_ISREG(fmodes[i])):
                # Not a file or a symlink: ignore.
                pass
            fn = fnames[i]
            if so_re.search(fn):
                # *.so or a *.so.*: cannot be sure, treat pkg as non-devel.
                so_found = 1
                break
            if not a_found and a_re.search(fn):
                # A *.a: mmm... this has potential, let's look further...
                a_found = 1
        # If we have a *.a but no *.so or *.so.*, assume devel.
        return a_found and not so_found


def callback(what, bytes, total, h, user):
    "Callback called during rpm transaction."
    sys.stdout.write(".")
    sys.stdout.flush()


def _hdrcmp(x, y):
    "Comparison function for rpm headers."
    return cmp(x[rpm.RPMTAG_NAME], y[rpm.RPMTAG_NAME]) or cmp(x, y) or \
           cmp(x[rpm.RPMTAG_ARCH], y[rpm.RPMTAG_ARCH])


def _usage():
    return '''rpmdev-rmdevelrpms [options]

rpmdev-rmdevelrpms is a script for finding and optionally removing
"development" packages, for example for cleanup purposes before starting to
build a new package.

By default, the following packages are treated as development ones and are
thus candidates for removal: any package whose name matches "-devel\\b",
"-debuginfo\\b", "-sdk\\b", or "-static\\b" (case insensitively) except gcc
requirements; any package whose name starts with "perl-(Devel|ExtUtils|Test)-";
any package whose name starts with "compat-gcc"; packages in the internal list
of known development oriented packages (see def_devpkgs in the source code);
packages determined to be development ones based on some basic heuristic
checks on the package\'s contents.

The default set of packages above is not intended to not reduce a system into
a minimal clean build root, but to keep it usable for general purposes while
getting rid of a reasonably large set of development packages.  The package
set operated on can be configured to meet various scenarios.

To include additional packages in the list of ones treated as development
packages, use the "devpkgs" option in the configuration file.  To exclude
packages from the list use "nondevpkgs" in it.  Exclusion overrides inclusion.

The system wide configuration file is __SYSCONFDIR__/rpmdevtools/rmdevelrpms.conf,
and per user settings (which override system ones) can be specified in
~/.config/rpmdevtools/rmdevelrpms.conf or ~/.rmdevelrpmsrc (deprecated).
These files are written in Python.

Report bugs to <http://bugzilla.redhat.com/>.'''


def version():
    print "rpmdev-rmdevelrpms version %s" % __version__
    print '''
Copyright (c) 2004-2009 Ville Skyttä <ville.skytta at iki.fi>
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.'''
    sys.exit(0)


def main():
    "Da meat."

    # TODO: implement -r|--root for checking a specified rpm root
    op = optparse.OptionParser(usage=_usage())
    op.add_option("-l", "--list-only", dest="listonly", action="store_true",
                  help="Output condensed list of packages, do not remove.")
    op.add_option("--qf", "--queryformat", dest="qf", action="store",
                  default=qf, help="Query format to use for output.")
    op.add_option("-y", "--yes", dest="yes", action="store_true",
                  help="Root only: remove without prompting; ignored with -l.")
    op.add_option("-v", "--version", dest="version", action="store_true",
                  help="Print program version and exit.")

    (opts, args) = op.parse_args()

    if opts.version:
        version()

    ts = rpm.TransactionSet("/")
    ts.setVSFlags(~(rpm._RPMVSF_NOSIGNATURES|rpm._RPMVSF_NODIGESTS))
    mi = ts.dbMatch()
    hdrs = []
    for hdr in mi:
        if isDevelPkg(hdr):
            hdrs.append(hdr)
            ts.addErase(mi.instance())
    ts.order()

    try:
        if len(hdrs) > 0:
            hdrs.sort(_hdrcmp)
            indent = ""
            if not opts.listonly:
                indent = "  "
                print "Found %d devel packages:" % len(hdrs)
            for hdr in hdrs:
                print indent + hdr.sprintf(opts.qf)
            if opts.listonly:
                pass
            else:
                # TODO: is there a way to get arch for the unresolved deps?
                unresolved = ts.check()
                if unresolved:
                    print "...whose removal would cause unresolved dependencies:"
                    unresolved.sort(lambda x, y: cmp(x[0][0], y[0][0]))
                    for t in unresolved:
                        dep = t[1][0]
                        if t[1][1]:
                            dep = dep + " "
                            if t[2] & rpm.RPMSENSE_LESS:
                                dep = dep + "<"
                            if t[2] & rpm.RPMSENSE_GREATER:
                                dep = dep + ">"
                            if t[2] & rpm.RPMSENSE_EQUAL:
                                dep = dep + "="
                            dep = dep + " " + t[1][1]
                        if t[4] == rpm.RPMDEP_SENSE_CONFLICTS:
                            dep = "conflicts with " + dep
                        elif t[4] == rpm.RPMDEP_SENSE_REQUIRES:
                            dep = "requires " + dep
                        print "  %s-%s-%s %s" % (t[0][0], t[0][1], t[0][2], dep)
                    print "Not removed due to dependencies."
                elif os.geteuid() == 0:
                    if not opts.yes:
                        proceed = raw_input("Remove them? [y/N] ")
                    else:
                        proceed = "y"
                    if (proceed in ("Y", "y")):
                        sys.stdout.write("Removing...")
                        errors = ts.run(callback, "")
                        print "Done."
                        if errors:
                            for error in errors:
                                print error
                            sys.exit(1)
                    else:
                        print "Not removed."
                else:
                    print "Not running as root, skipping remove."
        else:
            print "No devel packages found."
    finally:
        ts.closeDB()
        del ts


for conf in ("__SYSCONFDIR__/rpmdevtools/rmdevelrpms.conf",
             os.path.join(os.environ["HOME"], ".rmdevelrpmsrc"), # deprecated
             os.path.join(os.environ["HOME"],
                          ".config/rpmdevtools/rmdevelrpms.conf")):
    try:
        execfile(conf)
    except IOError:
        pass
    if type(devpkgs) == types.StringType:
        devpkgs = devpkgs.split()
    if type(nondevpkgs) == types.StringType:
        nondevpkgs = nondevpkgs.split()
main()
