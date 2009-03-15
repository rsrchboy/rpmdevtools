AUTOMAKE_OPTIONS = foreign 1.10.1 dist-lzma

SUBDIRS = emacs qa-robot

pkgdatadir = $(datadir)/rpmdevtools
pkgsysconfdir = $(sysconfdir)/rpmdevtools
bashcompdir = $(sysconfdir)/bash_completion.d

bin_SCRIPTS = rpmdev-newspec rpmdev-rmdevelrpms
dist_bin_SCRIPTS = rpmdev-checksig rpmdev-diff rpmdev-extract rpmdev-md5 \
	rpmdev-setuptree rpmdev-vercmp rpmdev-wipetree rpminfo rpmls \
	rpmdev-bumpspec

man1_MANS = rpmdev-diff.1 rpmdev-extract.1 rpmdev-bumpspec.1 rpmdev-newspec.1
man8_MANS = rpmdev-rmdevelrpms.8

dist_pkgdata_DATA = template.init

dist_pkgsysconf_DATA = newspec.conf rmdevelrpms.conf \
	spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-php-pear.spec \
	spectemplate-python.spec spectemplate-ruby.spec \
	spectemplate-ocaml.spec

dist_bashcomp_DATA = rpmdevtools.bash-completion

EXTRA_DIST = $(PACKAGE).spec rpmdev-newspec.in rpmdev-rmdevelrpms.in

MOSTLYCLEANFILES = $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS)

sums = sum cksum sha1 sha224 sha256 sha384 sha512

all: $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS)

%: %.in
	$(SED) -e 's|__SYSCONFDIR__|$(sysconfdir)|g' $< > $@
	chmod +x $@

%.1: %
	chmod +x $<
	$(HELP2MAN) --section=1 --no-info -h -h -v -v $(<D)/$(<F) --output=$@

%.8: %
	chmod +x $<
	$(HELP2MAN) --section=8 --no-info $(<D)/$(<F) --output=$@

install-exec-hook:
	cd $(DESTDIR)$(bindir) && \
	for sum in $(sums) ; do ln rpmdev-md5 rpmdev-$$sum ; done

uninstall-hook:
	cd $(DESTDIR)$(bindir) && \
	for sum in $(sums) ; do $(RM) rpmdev-$$sum ; done
