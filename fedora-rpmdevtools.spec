Name:           fedora-rpmdevtools
Version:        0.1.5
Release:        0.fdr.1
Epoch:          0
Summary:        Fedora RPM Development Tools

Group:          Development/Tools
License:        GPL
URL:            http://www.fedora.us/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
# Required for tool operations
Requires:       rpm-python, python, cpio, sed, perl
# Minimal RPM build requirements
Requires:       rpm-build, gcc, gcc-c++, redhat-rpm-config, make, tar, patch
Requires:       diffutils, gzip, bzip2, unzip

%description
Scripts to aid in development of Fedora RPM packages.  These
tools are designed for Red Hat Linux 8 and higher.
fedora-newrpmspec       Creates new .spec from template
fedora-rpmvercmp        RPM version comparison checker
fedora-buildrpmtree     Create RPM build tree within user homedir
fedora-rmdevelrpms      Find (and optionally remove) "development" RPMs
fedora-installdevkeys   Install developer keys in alternate RPM keyring
fedora-rpmsigcheck      Check package sigs using alterate RPM keyring
fedora-wipebuildtree    Erases all files within ~/redhat
fedora-unrpm            Extract a RPM, "tar zxvf"-style
fedora-pkgannfmt        Produce output for fedora-package-announce
fedora-md5              Display the md5sum of all files in a RPM

%package        emacs
Summary:        (X)Emacs support for Fedora RPM Development Tools
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    emacs
(X)Emacs support for Fedora RPM Development Tools.


%prep
%setup -q


%build


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
cp -p fedora-pkgannfmt       $RPM_BUILD_ROOT%{_bindir}
cp -p fedora-md5             $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fedora/devgpgkeys
cp -p spectemplate*.spec template.init $RPM_BUILD_ROOT%{_datadir}/fedora
cp -p devgpgkeys/* $RPM_BUILD_ROOT%{_datadir}/fedora/devgpgkeys

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fedora
cp -p rmdevelrpms.conf $RPM_BUILD_ROOT%{_sysconfdir}/fedora

mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
cp -p emacs/fedora-init.el \
  $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d
cp -p emacs/fedora-init.el \
  $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0644,root,root,0755)
%doc COPYING
%attr(0755,root,root) %{_bindir}/fedora-*
%config(noreplace) %{_sysconfdir}/fedora
%{_datadir}/fedora

%files emacs
%defattr(0644,root,root,0755)
%doc emacs/*.patch
%{_datadir}/emacs/site-lisp/site-start.d
%{_datadir}/xemacs/site-packages/lisp/site-start.d


%changelog
* Sat Dec  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.5-0.fdr.1
- Incorporate $TNV suggestions from bug 1010:
- Add unzip into the list of "assumed present" packages.
- Treat gcc32, m4, *-debuginfo and perl-Test-* as development packages
  in rmdevelrpms.
- Add sanity checks to fedora-wipebuildtree.
- New tool: fedora-md5.
- Include perl spec file template and add (X)Emacs support for it.

* Sat Nov  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.4-0.fdr.2
- Remove duplicate rawhide 2003 automated build key.

* Sat Nov  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.4-0.fdr.1
- Add Fedora Project keys.

* Fri Oct 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.3-0.fdr.1
- Add Nils Olav Selåsdal's key into devgpgkeys (bug 783).
- fedora-wipebuildtree now cleans up both ~/redhat and ~/rpmbuild for
  consistency with fedora-buildrpmtree and backwards compatibility (bug 783).
- Treat pkgconfig as a devel package in fedora-rmdevelrpms (bug 783).
- New script: fedora-pkgannfmt (bug 783).
- Make fedora-rmdevelrpms tolerate strings in devpkgs and nondevpkgs (bug 783).

* Sat Oct 18 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.2-0.fdr.1
- Skip removing packages in fedora-rmdevelrpms if it would cause
  unresolved dependencies (bug 783).

* Wed Oct  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.1-0.fdr.1
- Unobfuscate new devel pkg heuristics in fedora-rmdevelrpms (bug 783).

* Wed Oct  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.0-0.fdr.1
- Rewrite fedora-rmdevelrpms in Python.
  Note: configuration files have moved and changed format.

* Sun Sep 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.22-0.fdr.1
- Remove tetex-dvips from rmdevelrpms (bug 525).

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.21-0.fdr.1
- Add the new Rawhide package signing key.

* Thu Sep 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.20-0.fdr.1
- Use "make install DESTDIR=..." instead of %%makeinstall in spec templates.

* Thu Sep  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.19-0.fdr.1
- Add Andreas Bierfert's key to devgpgkeys.

* Fri Aug 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.18-0.fdr.1
- Change fallback case to exit 2 in init script template (bug 525).
- Sync fedora-buildrpmtree with Russ's latest version (bug 594).
- Add CVS Id keywords to applicable files.

* Tue Aug  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.17-0.fdr.1
- Require gzip and bzip2 (bug 525).
- Read configs first in fedora-rmdevelrpms to prevent overriding internals.
- Add autoconf, autoconf213, automake, automake14, automake15, automake16,
  dev86, doxygen and swig to packages treated as devel in rmdevelrpms.
- Make rmdevelrpms work with non-English locales (bug 544).
- 2 empty lines instead of # --------- separators in spec templates (bug 525).
- Move non-config files under %%{_datadir}/fedora.
- Change %%{_sysconfdir}/fedora-rpmdevtools to %%{_sysconfdir}/fedora.

* Tue Jul 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.16-0.fdr.3
- Require diffutils, make, patch and tar (bug 492).

* Sat Jul 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.16-0.fdr.2
- One more typo fix for init script template.

* Sat Jul 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.16-0.fdr.1
- Fix force-reload in init script template.

* Thu Jul 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.15-0.fdr.1
- Address init script issues in bug 342, comment 9.

* Tue Jul  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.14-0.fdr.1
- Add init script template.

* Fri Jun 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0.13-0.fdr.1
- Address issues in #342:
- Add Michael Schwendt's (0xB8AF1C54) and Adrian Reber's (0x3ED6F034) keys.
- Treat libtool and qt-designer as devel packages in fedora-rmdevelrpms.

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
