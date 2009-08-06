%global emacs_sitestart_d  %{_datadir}/emacs/site-lisp/site-start.d
%global xemacs_sitestart_d %{_datadir}/xemacs/site-packages/lisp/site-start.d
%global spectool_version   1.0.10

Name:           rpmdevtools
Version:        7.3
Release:        1%{?dist}
Summary:        RPM Development Tools

Group:          Development/Tools
# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:        GPLv2+ and GPLv2
URL:            https://fedorahosted.org/rpmdevtools/
Source0:        https://fedorahosted.org/released/rpmdevtools/%{name}-%{version}.tar.lzma
Source1:        http://people.redhat.com/nphilipp/spectool/spectool-%{spectool_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
# lzma for unpacking the tarball
BuildRequires:  lzma
# help2man, pod2man, *python for creating man pages
BuildRequires:  help2man
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  python
BuildRequires:  rpm-python
Provides:       spectool = %{spectool_version}
Requires:       diffutils
Requires:       fakeroot
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       rpm-build >= 4.4.2.1
Requires:       rpm-python
Requires:       sed
Requires:       wget
Requires:       man
# For _get_cword in bash completion snippet
Conflicts:      bash-completion < 20080705

%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
spectool            Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.


%prep
%setup -q -a 1
cp -p spectool-%{spectool_version}/README README.spectool


%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -pm 755 spectool-%{spectool_version}/spectool $RPM_BUILD_ROOT%{_bindir}

for dir in %{emacs_sitestart_d} %{xemacs_sitestart_d} ; do
  install -dm 755 $RPM_BUILD_ROOT$dir
  ln -s %{_datadir}/rpmdevtools/rpmdev-init.el $RPM_BUILD_ROOT$dir
  touch $RPM_BUILD_ROOT$dir/rpmdev-init.elc
done


%clean
rm -rf $RPM_BUILD_ROOT


%triggerin -- emacs-common
[ -d %{emacs_sitestart_d} ] && \
  ln -sf %{_datadir}/rpmdevtools/rpmdev-init.el %{emacs_sitestart_d} || :

%triggerin -- xemacs-common
[ -d %{xemacs_sitestart_d} ] && \
  ln -sf %{_datadir}/rpmdevtools/rpmdev-init.el %{xemacs_sitestart_d} || :

%triggerun -- emacs-common
[ $2 -eq 0 ] && rm -f %{emacs_sitestart_d}/rpmdev-init.el* || :

%triggerun -- xemacs-common
[ $2 -eq 0 ] && rm -f %{xemacs_sitestart_d}/rpmdev-init.el* || :


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README*
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_sysconfdir}/bash_completion.d/
%{_datadir}/rpmdevtools/
%{_bindir}/*
%{_bindir}/spectool
%ghost %{_datadir}/*emacs
%{_mandir}/man[18]/*.[18]*


%changelog
* Mon May 25 2009 Ville Skyttä <ville.skytta at iki.fi> - 7.3-1
- Update to 7.3.

* Wed May 20 2009 Ville Skyttä <ville.skytta at iki.fi> - 7.2-1
- Update to 7.2; fixes #498588.

* Sat Apr  4 2009 Ville Skyttä <ville.skytta at iki.fi> - 7.1-1
- Update to 7.1.

* Fri Dec 26 2008 Ville Skyttä <ville.skytta at iki.fi> - 7.0-1
- Update to 7.0; fixes #461177, #472641, #477055, fedorahosted#1,
  fedorahosted#6, fedorahosted#7.

* Sun Aug  3 2008 Ville Skyttä <ville.skytta at iki.fi> - 6.7-1
- Update to 6.7; fixes #442993, #443266.

* Thu Mar 27 2008 Ville Skyttä <ville.skytta at iki.fi> - 6.6-1
- Update to 6.6.

* Wed Mar 26 2008 Ville Skyttä <ville.skytta at iki.fi> - 6.5-1
- Update to 6.5; fixes #407781.

* Fri Oct 12 2007 Lubomir Kundrak <lkundrak@redhat.com> - 6.4-1
- Update to 6.4.

* Fri Oct 12 2007 Lubomir Kundrak <lkundrak@redhat.com> - 6.3-1
- Update to 6.3.

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 6.2-1
- Update to 6.2.

* Fri Aug 10 2007 Ville Skyttä <ville.skytta at iki.fi> - 6.1-1
- Update to 6.1; works around #250990.

* Thu Jul  5 2007 Ville Skyttä <ville.skytta at iki.fi> - 6.0-1
- Update to 6.0; fixes #213778, #243731.

* Wed Oct 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 5.3-1
- Update to 5.3; fixes #212108.

* Mon Oct  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 5.2-1
- Update to 5.2; fixes #208903.

* Sat Sep  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 5.1-1
- Update to 5.1; fixes #198706.

* Tue Aug 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 5.0-2
- Migrate rmdevelrpms config when upgrading from fedora-rpmdevtools.

* Sun Aug 20 2006 Ville Skyttä <ville.skytta at iki.fi> - 5.0-1
- Update to 5.0, rename to rpmdevtools; fixes #180066, #189947, #198706,
  #199909.

* Tue May 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6-1
- Update to 1.6; fixes #185606.

* Sun Feb 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.5-1
- Update to 1.5; fixes #162253, #178636, #180066.

* Sat Feb  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-2
- Fix rpath checker tests with bash 3.1 (#178636, Enrico Scholz).

* Fri Dec 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.4-1
- Update to 1.4; fixes #176521.

* Thu Oct 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3-1
- Update to 1.3; fixes #169298, #170902.

* Fri Oct  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2-1
- Update to 1.2; fixes #169298.

* Fri Jul  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1-1
- Update to 1.1.

* Thu Mar 24 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0-1
- Update to 1.0.

* Sun Feb  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.1-1
- Update to 0.3.1; fixes #147014.

* Tue Jan 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.3.0-1
- Update to 0.3.0; fixes fedora.us#2351.
