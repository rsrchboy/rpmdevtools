pkgdatadir = $(datadir)/rpmdevtools
POD2MAN_OPTS = --release "$(PACKAGE) $(VERSION)" --center ""

bin_SCRIPTS = rpmargs rpmpeek rpmsodiff
dist_bin_SCRIPTS = rpmelfsym rpmfile rpmsoname

pkgdata_DATA = tmpdir.sh trap.sh

man1_MANS = rpmargs.1 rpmelfsym.1 rpmfile.1 rpmpeek.1 rpmsodiff.1 rpmsoname.1

EXTRA_DIST = rpmargs.in rpmpeek.in rpmsodiff.in tmpdir.sh.in trap.sh.in
MOSTLYCLEANFILES = $(bin_SCRIPTS) $(man1_MANS) $(pkgdata_DATA)

all: $(bin_SCRIPTS) $(man1_MANS)

%: %.in
	$(SED) -e 's|__PKGDATADIR__|$(pkgdatadir)|g' $< > $@
	chmod +x $@

%.1: %
	$(POD2MAN) $(POD2MAN_OPTS) $< $@
