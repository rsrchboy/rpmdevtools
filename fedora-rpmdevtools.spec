Summary:        Fedora RPM Development Tools
Name:           fedora-rpmdevtools
Epoch:          0
Version:        0.0.9
Release:        0.fdr.1
URL:            http://www.fedora.us/tools
License:        GPL
Group:          Development/Tools
Source0:        fedora-rpmdevtools-0.0.9.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
# Required for tool operations
Requires:       rpm-python, python, cpio, sed
# Minimal RPM build requirements
Requires:       rpm-build, gcc, gcc-c++, redhat-rpm-config
BuildArch:      noarch

%description
Scripts to aid in development of Fedora RPM packages.  These
tools are designed for Red Hat Linux 8 and higher.
fedora-newrpmspec	Creates new .spec from template
fedora-rpmvercmp	RPM version comparison checker
fedora-buildrpmtree	Create RPM build tree within user homedir
fedora-rmdevelrpms	Find (and optionally remove) "development" RPMs
fedora-installdevkeys	Install developer keys in alternate RPM keyring
fedora-rpmsigcheck	Check package sigs using alterate RPM keyring
fedora-wipebuildtree	Erases all files within ~/redhat
fedora-unrpm		Extract a RPM, "tar zxvf"-style

#---------------------------------------------------------------------

%prep
%setup -q

#---------------------------------------------------------------------

%build

#---------------------------------------------------------------------

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/fedora-rpmdevtools/devgpgkeys/
cp -p fedora-newrpmspec      %{buildroot}%{_bindir}
cp -p fedora-rpmvercmp       %{buildroot}%{_bindir}
cp -p fedora-buildrpmtree    %{buildroot}%{_bindir}
cp -p fedora-rmdevelrpms     %{buildroot}%{_bindir}
cp -p fedora-installdevkeys  %{buildroot}%{_bindir}
cp -p fedora-rpmchecksig     %{buildroot}%{_bindir}
cp -p fedora-wipebuildtree   %{buildroot}%{_bindir}
cp -p fedora-unrpm           %{buildroot}%{_bindir}
cp -p devgpgkeys/*           %{buildroot}%{_sysconfdir}/fedora-rpmdevtools/devgpgkeys/
cp -p spectemplate.spec      %{buildroot}%{_sysconfdir}/fedora-rpmdevtools/
cp -p develrpms.conf         %{buildroot}%{_sysconfdir}/fedora-rpmdevtools/

#---------------------------------------------------------------------

%clean
rm -rf %{buildroot}

#---------------------------------------------------------------------

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/fedora-rpmdevtools
%config(noreplace) %{_sysconfdir}/fedora-rpmdevtools/develrpms.conf
%config %{_sysconfdir}/fedora-rpmdevtools/spectemplate.spec
%dir %{_sysconfdir}/fedora-rpmdevtools/devgpgkeys
%config %{_sysconfdir}/fedora-rpmdevtools/devgpgkeys/*

#---------------------------------------------------------------------

%changelog
* Sat Apr 26 2003 Warren Togami <warren@togami.com> - 0:0.0.9-0.fdr.1
- #224 fedora-installdevkeys added RH's key and beta key
- #224 RH8 has redhat-rpm-config too
- #224 -y option for fedora-rmdevelrpms

* Mon Apr 22 2003 Warren Togami <warren@togami.com> - 0:0.0.8-0.fdr.1
- #181 changes to rmdevelrpms
- #181 added Requires
- #181 rpmchecksig file not found crash

* Mon Apr 14 2003 Warren Togami <warren@togami.com> - 0:0.0.7-0.fdr.1
- Update Seth's rpmchecksig - non-zero exit codes with errors
- Include Seth's key

* Sun Apr 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.6-0.fdr.1
- Make KEEP_DEVEL_RPMS actually work, include a sample develrpms.conf.
- Mark stuff in %%{_sysconfdir}/fedora-rpmdevtools properly as %%config.
- Some spectemplate.spec updates.

* Sat Apr 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.5-0.fdr.1
- Improved version of fedora-rmdevelrpms: configurable packages to keep.
- Add fedora-unrpm.
- Use whoami instead of $USER in fedora-installdevkeys.
- Some spec file tweaks.

* Thu Apr 10 2003 Warren Togami <warren@togami.com> 0.0.4-0.fdr.1
- Replace rpmchecksig with Seth Vidal's python version with more verbose output

* Wed Apr 09 2003 Warren Togami <warren@togami.com> 0.0.3-0.fdr.1
- Update spec template
- Add Ville Skyttä's fedora-rmdevelrpms script
- Add Warren's installdevkeys and rpmchecksig
- Add Warren's wipebuildtree

* Thu Mar 27 2003 Warren Togami <warren@togami.com> 0.0.1-0.fdr.1
- Initial RPM release.
