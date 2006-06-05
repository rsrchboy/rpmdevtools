AUTOMAKE_OPTIONS = foreign 1.5 dist-bzip2

SUBDIRS = devgpgkeys emacs test

pkgdatadir = $(datadir)/fedora
pkgsysconfdir = $(sysconfdir)/fedora
rpmlibdir = $(libdir)/rpm

dist_bin_SCRIPTS = fedora-buildrpmtree fedora-diffarchive fedora-extract \
	fedora-installdevkeys fedora-kmodhelper fedora-md5 fedora-newrpmspec \
	fedora-rmdevelrpms fedora-rpmchecksig fedora-rpminfo fedora-rpmvercmp \
	fedora-wipebuildtree

dist_pkgdata_DATA = spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-python.spec \
	spectemplate-ruby.spec template.init

dist_man1_MANS = fedora-extract.1 fedora-diffarchive.1
dist_man8_MANS = fedora-rmdevelrpms.8

dist_rpmlib_SCRIPTS = check-buildroot check-rpaths check-rpaths-worker

dist_pkgsysconf_DATA = rmdevelrpms.conf

EXTRA_DIST = $(PACKAGE).spec

MAINTAINERCLEANFILES = $(dist_man1_MANS) $(dist_man8_MANS) fedora-rpminfo

all:

%.1: %
	chmod +x $<
	env PATH=$(top_srcdir):$$PATH \
	$(HELP2MAN) --section=1 --no-info -h -h -v -v $< --output=$@

%.8: %
	chmod +x $<
	env PATH=$(top_srcdir):$$PATH \
	$(HELP2MAN) --section=8 --no-info $< --output=$@

fedora-rpminfo:
	$(WGET) -N http://people.redhat.com/twoerner/rpminfo/bin/rpminfo -O $@