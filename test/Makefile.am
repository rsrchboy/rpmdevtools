EXTRA_DIST = rpathtest.sh

check:
	chmod +x $(srcdir)/*.sh $(top_srcdir)/check-*
	env srcdir=$(top_srcdir) $(srcdir)/rpathtest.sh
