SUBDIRS = scripts

pkgsysconfdir = $(sysconfdir)/rpmdevtools

pkgsysconf_DATA = devscripts.conf

EXTRA_DIST = devscripts.conf.in version

MOSTLYCLEANFILES = devscripts.conf

all: devscripts.conf

devscripts.conf: devscripts.conf.in $(srcdir)/version
	VERSION=`cat $(srcdir)/version` && \
	sed -e "s/###VERSION###/$$VERSION/" $< > $@
