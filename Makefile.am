AUTOMAKE_OPTIONS = foreign 1.5 dist-bzip2

SUBDIRS = emacs qa-robot

pkgdatadir = $(datadir)/rpmdevtools
pkgsysconfdir = $(sysconfdir)/rpmdevtools

dist_bin_SCRIPTS = rpmdev-checksig rpmdev-diff rpmdev-extract rpmdev-md5 \
	rpmdev-newspec rpmdev-rmdevelrpms rpmdev-setuptree rpmdev-vercmp \
	rpmdev-wipetree rpminfo rpmls rpmdev-bumpspec

dist_man1_MANS = rpmdev-diff.1 rpmdev-extract.1
dist_man8_MANS = rpmdev-rmdevelrpms.8

dist_pkgdata_DATA = template.init

dist_pkgsysconf_DATA = spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-php-pear.spec \
	spectemplate-python.spec spectemplate-ruby.spec \
	spectemplate-fonts.spec newspec.conf rmdevelrpms.conf

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
