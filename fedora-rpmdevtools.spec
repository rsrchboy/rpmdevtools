%define emacs_sitestart_d  %{_datadir}/emacs/site-lisp/site-start.d
%define xemacs_sitestart_d %{_datadir}/xemacs/site-packages/lisp/site-start.d
%define spectool_version   1.0.7

Name:           fedora-rpmdevtools
Version:        1.6
Release:        1%{?dist}
Summary:        Fedora RPM Development Tools

Group:          Development/Tools
License:        GPL
URL:            http://fedora.redhat.com/
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://people.redhat.com/nphilipp/spectool/spectool-%{spectool_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Provides:       %{name}-emacs = %{version}-%{release}
Provides:       spectool = %{spectool_version}
Obsoletes:      %{name}-emacs < 0.1.9
# Required for tool operations
Requires:       rpm-python, python, cpio, sed, perl, wget, file
# Minimal RPM build requirements
Requires:       rpm-build, gcc, gcc-c++, redhat-rpm-config, make, tar, patch
Requires:       diffutils, gzip, bzip2, unzip

%description
This package contains scripts and (X)Emacs support files to aid in
development of Fedora RPM packages.  These tools are designed for Fedora
Core 2 and later.
fedora-buildrpmtree     Create RPM build tree within user's home directory
fedora-installdevkeys   Install GPG keys in alternate RPM keyring
fedora-kmodhelper       Helper script for building kernel module RPMs
fedora-md5              Display the md5sum of all files in an RPM
fedora-newrpmspec       Creates new .spec from template
fedora-rmdevelrpms      Find (and optionally remove) "development" RPMs
fedora-rpmchecksig      Check package signatures using alternate RPM keyring
fedora-rpminfo          Prints information about executables and libraries
fedora-rpmvercmp        RPM version comparison checker
fedora-extract          Extract various archives, "tar xvf" style
fedora-diffarchive      Diff contents of two archives
fedora-wipebuildtree    Erase all files within dirs created by buildrpmtree
spectool                Expand and download sources and patches in specfiles


%prep
%setup -q -a 1
cp -p spectool*/README README.spectool


%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -pm 755 spectool*/spectool $RPM_BUILD_ROOT%{_bindir}

for dir in %{emacs_sitestart_d} %{xemacs_sitestart_d} ; do
  install -dm 755 $RPM_BUILD_ROOT$dir
  ln -s %{_datadir}/fedora/emacs/fedora-init.el $RPM_BUILD_ROOT$dir
  touch $RPM_BUILD_ROOT$dir/fedora-init.elc
done


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%triggerin -- emacs-common
[ -d %{emacs_sitestart_d} ] && \
  ln -sf %{_datadir}/fedora/emacs/fedora-init.el %{emacs_sitestart_d} || :

%triggerin -- xemacs-common
[ -d %{xemacs_sitestart_d} ] && \
  ln -sf %{_datadir}/fedora/emacs/fedora-init.el %{xemacs_sitestart_d} || :

%triggerun -- emacs-common
[ $2 -eq 0 ] && rm -f %{emacs_sitestart_d}/fedora-init.el* || :

%triggerun -- xemacs-common
[ $2 -eq 0 ] && rm -f %{xemacs_sitestart_d}/fedora-init.el* || :


%files
%defattr(-,root,root,-)
%doc COPYING README*
%config(noreplace) %{_sysconfdir}/fedora
%{_datadir}/fedora/
%{_bindir}/fedora-*
%{_bindir}/spectool
%{_prefix}/lib/rpm/check-*
%ghost %{_datadir}/*emacs
%{_mandir}/man?/fedora-*.?*


%changelog
* Mon Jun  5 2006 Ville Skyttä <ville.skytta at iki.fi>
- Add manual pages for rmdevelrpms and extract.
- Trim pre-2005 changelog entries.
- Autotoolize source tree.

* Tue May 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6-1
- Add spec template for library packages (#185606, Ignacio Vazquez-Abrams).

* Sun Feb 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.5-1
- Improve diffarchive and extract error messages.

* Fri Feb 24 2006 Ville Skyttä <ville.skytta at iki.fi>
- Update spectool to 1.0.7 (#162253).

* Thu Feb  9 2006 Ville Skyttä <ville.skytta at iki.fi>
- Add file(1) based archive type detection to fedora-extract.

* Wed Feb  8 2006 Ville Skyttä <ville.skytta at iki.fi>
- Add "diff file lists only" option to diffarchive.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi>
- Add Ruby spec template (#180066, Oliver Andrich) and make newrpmspec
  use it for ruby-*.

* Sat Feb  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-2
- Fix rpath checker tests with bash 3.1 (#178636, Enrico Scholz).

* Fri Dec 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.4-1
- Update spectool to 1.0.6 (#176521).

* Wed Dec 28 2005 Ville Skyttä <ville.skytta at iki.fi>
- Update spectool to 1.0.5 (#162253), require wget for it.
- Add disttags to spec templates.

* Thu Oct 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3-1
- check-rpaths-worker: detect when RPATH references the parent directory
  of an absolute path (#169298, Enrico Scholz).
- Add regression test for check-rpaths* (#169298, Enrico Scholz).
- Honor user's indent-tabs-mode setting in fedora-init.el (#170902).

* Fri Oct  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2-1
- check-buildroot: grep for buildroot as a fixed string, not a regexp.
- Update FSF's address in copyright notices.
- check-rpaths-worker: allow multiple $ORIGIN paths in an RPATH and allow
  RPATHs which are relative to $ORIGIN (#169298, Enrico Scholz).
- check-rpaths-worker: give out an hint about usage and the detected issues
  at the first detected error (Enrico Scholz).
- Remove some redundancy from the Perl spec template.
- Teach fedora-newrpmspec to detect and use different specfile variants.
- Use fedora-newrpmspec in fedora-init.el.

* Fri Jul  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1-1
- Drop more pre-FC2 compat stuff from Perl spec template.
- Treat gcc-gfortran as a devel package in rmdevelrpms.
- Drop fedora.us GPG key.

* Thu Mar 24 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0-1
- Make fedora-diffarchive work better with archives containing dirs without
  read/execute permissions.
- Sync "Epoch: 0" drops with Fedora Extras CVS.
- Include Nils Philippsen's spectool.
- Own (%%ghost'd) more dirs from the site-lisp dir hierarchies.
- Drop trigger support pre-FC2 Emacs and XEmacs packages.
- Drop rpm-spec-mode.el patch, no longer needed for FC2 Emacs and later.
- Update URLs.
- Drop developer GPG keys from the package, add Fedora Extras key.
- Drop fedora-pkgannfmt, it's no longer relevant.
- Remove pre-FC2 compatibility stuff from Perl spec template.
- Don't try to remove gcc-java and related packages by default in rmdevelrpms.
- Remove "full featured" spec template, convert newrpmspec to use -minimal.

* Sun Feb  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.1-1
- Make buildrpmtree and wipebuildtree less dependent on a specific
  configuration (#147014, Ignacio Vazquez-Abrams).

* Tue Jan 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.0-1
- Remove 0.fdr. prefixes and epoch 0's from all spec templates.
- Add try-restart action to init script template.
- Remove deprecated fedora-diffrpm and fedora-unrpm.
- Install check-* to %%{_prefix}/lib/rpm instead of %%{_libdir}/rpm (bug 2351).
- Check both %%{_prefix}/lib and %%{_prefix}/lib64 in the xemacs trigger.
- Update rpminfo to 2004-07-07-01 and include it in the tarball.
