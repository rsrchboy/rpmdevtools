Summary:        Fedora RPM Development Tools
Name:           fedora-rpmdevtools
Epoch:          0
Version:        0.0.12
Release:        0.fdr.2
URL:            http://www.fedora.us/
License:        GPL
Group:          Development/Tools
Source0:        %{name}-%{version}.tar.bz2
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

%package        emacs
Summary:        (X)Emacs support for Fedora RPM Development Tools
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    emacs
(X)Emacs support for Fedora RPM Development Tools.

# -----------------------------------------------------------------------------

%prep
%setup -q

# -----------------------------------------------------------------------------

%build

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-newrpmspec      $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-rpmvercmp       $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-buildrpmtree    $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-rmdevelrpms     $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-installdevkeys  $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-rpmchecksig     $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-wipebuildtree   $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-unrpm           $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fedora-rpmdevtools/devgpgkeys
cp -p devgpgkeys/* $RPM_BUILD_ROOT%{_sysconfdir}/fedora-rpmdevtools/devgpgkeys

cp -p spectemplate*.spec $RPM_BUILD_ROOT%{_sysconfdir}/fedora-rpmdevtools
cp -p develrpms.conf $RPM_BUILD_ROOT%{_sysconfdir}/fedora-rpmdevtools

mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
cp -p emacs/fedora-init.el \
  $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d
cp -p emacs/fedora-init.el \
  $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d

# -----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%files
%defattr(0644,root,root,0755)
%doc COPYING
%attr(0755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/fedora-rpmdevtools
%config(noreplace) %{_sysconfdir}/fedora-rpmdevtools/develrpms.conf
%config %{_sysconfdir}/fedora-rpmdevtools/spectemplate*.spec
%dir %{_sysconfdir}/fedora-rpmdevtools/devgpgkeys
%config %{_sysconfdir}/fedora-rpmdevtools/devgpgkeys/*

%files emacs
%defattr(0644,root,root,0755)
%doc emacs/*.patch
%{_datadir}/emacs/site-lisp/site-start.d
%{_datadir}/xemacs/site-packages/lisp/site-start.d

#---------------------------------------------------------------------

%changelog
* Wed May 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.12-0.fdr.2
- Make install-info in spec template silent for --excludedocs (#234).

* Tue May 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.12-0.fdr.1
- Include a minimal spec template for use with editors (#234).
- Split (X)Emacs stuff into -emacs subpackage (#234).

* Wed May  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.11-0.fdr.1
- #234 add (post,preun) install-info scriptlets to spec template.
- Install Fedora rpm-spec-mode (X)Emacs init stuff.  Needs a patched
  rpm-spec-mode.el (patch included in docs).
- Include a copy of the GPL.

* Sat May 03 2003 Warren Togami <warren@togami.com> - 0:0.0.10-0.fdr.1
- Added Enrico's key 0xE421D146
- #234 fedora-develrpms added docbook-utils-pdf, tetex-dvips
- #234 Most of Thomas' spec changes
- #234 %{buildroot} --> $RPM_BUILD_ROOT
- #234 Ville + Adrian's BuildRoot
- #234 Adrian's improved newrpmspec

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
