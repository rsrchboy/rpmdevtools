pkgdatadir = $(datadir)/rpmdevtools
POD2MAN = pod2man --release "$(PACKAGE) $(VERSION)" --center ""

dist_bin_SCRIPTS = rpmargs rpmelfsym rpmfile rpmpeek rpmsodiff rpmsoname

dist_pkgdata_DATA = tmpdir.sh trap.sh

dist_man1_MANS = rpmargs.1 rpmelfsym.1 rpmfile.1 rpmpeek.1 rpmsodiff.1 \
	rpmsoname.1

MAINTAINERCLEANFILES = $(dist_man1_MANS) rpmargs rpmpeek rpmsodiff \
	tmpdir.sh trap.sh

all: $(dist_man1_MANS)

%: %.in
	sed -e 's|@pkgdatadir@|$(pkgdatadir)|g' $< > $@
	chmod +x $@

%.1: %
	$(POD2MAN) $< $@
