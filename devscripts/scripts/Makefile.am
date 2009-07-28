bin_SCRIPTS = annotate-output checkbashisms licensecheck manpage-alert

man1_MANS = licensecheck.1
dist_man1_MANS = annotate-output.1 checkbashisms.1 manpage-alert.1

EXTRA_DIST = annotate-output.sh checkbashisms.pl licensecheck.pl \
	manpage-alert.sh

MOSTLYCLEANFILES = annotate-output checkbashisms licensecheck licensecheck.1 \
	manpage-alert

all: $(bin_SCRIPTS) $(man1_MANS)

%: %.pl $(srcdir)/../version
	VERSION=`cat $(srcdir)/../version` && \
	$(SED) -e "s|###VERSION###|$$VERSION|g" \
	       -e 's|__SYSCONFDIR__|$(sysconfdir)|g' \
	$< > $@ && chmod +x $@

%: %.sh $(srcdir)/../version
	VERSION=`cat $(srcdir)/../version` && \
	$(SED) -e "s|###VERSION###|$$VERSION|g" \
	       -e 's|__SYSCONFDIR__|$(sysconfdir)|g' \
	$< > $@ && chmod +x $@

licensecheck.1: licensecheck
	$(POD2MAN) --center=" " --release="Debian Utilities" $< > $@
