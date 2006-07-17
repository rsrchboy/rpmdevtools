AUTOMAKE_OPTIONS = foreign 1.5 dist-bzip2

SUBDIRS = emacs test

pkgdatadir = $(datadir)/rpmdevtools
pkgsysconfdir = $(sysconfdir)/rpmdevtools
rpmlibdir = $(libdir)/rpm

dist_bin_SCRIPTS = buildrpmtree diffarchive extractarchive \
	rpmmd5 newrpmspec \
	rmdevelrpms rpmchecksig rpminfo rpmvercmp \
	wipebuildtree

dist_man1_MANS = extractarchive.1 diffarchive.1
dist_man8_MANS = rmdevelrpms.8

dist_pkgdata_DATA = template.init

dist_pkgsysconf_DATA = spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-python.spec \
	spectemplate-ruby.spec rmdevelrpms.conf

dist_rpmlib_SCRIPTS = check-buildroot check-rpaths check-rpaths-worker

EXTRA_DIST = $(PACKAGE).spec

MAINTAINERCLEANFILES = $(dist_man1_MANS) $(dist_man8_MANS) rpminfo

all:

%.1: %
	chmod +x $<
	env PATH=$(top_srcdir):$$PATH \
	$(HELP2MAN) --section=1 --no-info -h -h -v -v $< --output=$@

%.8: %
	chmod +x $<
	env PATH=$(top_srcdir):$$PATH \
	$(HELP2MAN) --section=8 --no-info $< --output=$@

rpminfo:
	$(WGET) -N http://people.redhat.com/twoerner/rpminfo/bin/rpminfo -O $@
