pkgdatadir = $(datadir)/rpmdevtools
POD2MAN = pod2man --release "$(PACKAGE) $(VERSION)" --center ""

bin_SCRIPTS = rpmargs rpmpeek rpmsodiff
dist_bin_SCRIPTS = rpmelfsym rpmfile rpmsoname

pkgdata_DATA = tmpdir.sh trap.sh

dist_man1_MANS = rpmargs.1 rpmelfsym.1 rpmfile.1 rpmpeek.1 rpmsodiff.1 \
	rpmsoname.1

DIST_SOURCES = rpmargs.in rpmpeek.in rpmsodiff.in tmpdir.sh.in trap.sh.in
MAINTAINERCLEANFILES = $(dist_man1_MANS)
MOSTLYCLEANFILES = $(bin_SCRIPTS) $(pkgdata_DATA)

#all: $(dist_man1_MANS)

%: %.in
	sed -e 's|@pkgdatadir@|$(pkgdatadir)|g' $< > $@
	chmod +x $@

%.1: %
	$(POD2MAN) $< $@
