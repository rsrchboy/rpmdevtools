AUTOMAKE_OPTIONS = foreign 1.11 dist-xz

SUBDIRS = devscripts emacs qa-robot

pkgsysconfdir = $(sysconfdir)/rpmdevtools
bashcompdir = $(sysconfdir)/bash_completion.d

bin_SCRIPTS = rpmdev-newinit rpmdev-newspec rpmdev-rmdevelrpms
dist_bin_SCRIPTS = rpmdev-checksig rpmdev-diff rpmdev-extract rpmdev-md5 \
	rpmdev-setuptree rpmdev-vercmp rpmdev-wipetree rpminfo rpmls \
	rpmdev-bumpspec rpmdev-packager

man1_MANS = rpmdev-diff.1 rpmdev-extract.1 rpmdev-bumpspec.1 rpmdev-newinit.1 \
	rpmdev-newspec.1 rpmdev-packager.1
man8_MANS = rpmdev-rmdevelrpms.8

dist_pkgsysconf_DATA = newspec.conf rmdevelrpms.conf \
	spectemplate-lib.spec spectemplate-minimal.spec \
	spectemplate-perl.spec spectemplate-php-pear.spec \
	spectemplate-python.spec spectemplate-ruby.spec \
	spectemplate-ocaml.spec spectemplate-R.spec spectemplate-dummy.spec \
	template.init

bashcomp_DATA = rpmdevtools.bash-completion

EXTRA_DIST = rpmdev-newinit.in rpmdev-newspec.in rpmdev-rmdevelrpms.py \
	rpmdevtools.bash-completion.in

MOSTLYCLEANFILES = $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS) $(bashcomp_DATA)

sums = sum cksum sha1 sha224 sha256 sha384 sha512

all: $(bin_SCRIPTS) $(man1_MANS) $(man8_MANS) $(bashcomp_DATA)

%: %.in
	$(SED) -e 's|__SYSCONFDIR__|$(sysconfdir)|g' $< > $@

%: %.py
	$(SED) -e 's|__SYSCONFDIR__|$(sysconfdir)|g' $< > $@

%.1: %
	chmod +x $<
	COLUMNS=1000 $(HELP2MAN) -s 1 -N -h -h -v -v $(<D)/$(<F) -o $@

%.8: %
	chmod +x $<
	COLUMNS=1000 $(HELP2MAN) -s 8 -N $(<D)/$(<F) -o $@

install-exec-hook:
	cd $(DESTDIR)$(bindir) && \
	for sum in $(sums) ; do ln rpmdev-md5 rpmdev-$$sum ; done

uninstall-hook:
	cd $(DESTDIR)$(bindir) && \
	for sum in $(sums) ; do $(RM) rpmdev-$$sum ; done
