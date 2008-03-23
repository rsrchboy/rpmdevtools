AUTOMAKE_OPTIONS = foreign 1.5 dist-bzip2

SUBDIRS = emacs qa-robot

pkgdatadir = $(datadir)/rpmdevtools
pkgsysconfdir = $(sysconfdir)/rpmdevtools

bin_SCRIPTS = rpmdev-newspec rpmdev-rmdevelrpms
dist_bin_SCRIPTS = rpmdev-checksig rpmdev-diff rpmdev-extract rpmdev-md5 \
	rpmdev-setuptree rpmdev-vercmp rpmdev-wipetree rpminfo rpmls \
	rpmdev-bumpspec

man1_MANS = rpmdev-diff.1 rpmdev-extract.1 rpmdev-bumpspec.1
man8_MANS = rpmdev-rmdevelrpms.8

dist_pkgdata_DATA = template.init

dist_pkgsysconf_DATA = newspec.conf rmdevelrpms.conf \
	spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-php-pear.spec \
	spectemplate-python.spec spectemplate-ruby.spec \
	spectemplate-fonts.spec spectemplate-ocaml.spec

EXTRA_DIST = $(PACKAGE).spec rpmdev-newspec.in rpmdev-rmdevelrpms.in

MOSTLYCLEANFILES = $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS)
MAINTAINERCLEANFILES = rpminfo

all: $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS)

%: %.in
	$(SED) -e 's|__SYSCONFDIR__|$(sysconfdir)|g' $< > $@
	chmod +x $@

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
