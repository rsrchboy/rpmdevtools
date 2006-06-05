EXTRA_DIST = fedora-kmodhelper-test.sh rpathtest.sh

check:
	chmod +x $(srcdir)/*.sh $(top_srcdir)/{fedora-kmodhelper,check-*}
	$(srcdir)/fedora-kmodhelper-test.sh $(top_srcdir)/fedora-kmodhelper
	env srcdir=$(top_srcdir) $(srcdir)/rpathtest.sh
