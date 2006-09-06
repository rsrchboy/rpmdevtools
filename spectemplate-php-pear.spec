%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}

Name:           
Version:        
Release:        1%{?dist}
Summary:        

Group:          
License:        
URL:            http://pear.php.net/package/Foo_Bar
Source0:        http://pear.php.net/get/Foo_Bar-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  php-pear >= 1:1.4.9-1.2
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(Foo_Bar) = %{version}

%description


%prep
%setup -q -c
[ -f package2.xml ] || mv package.xml package2.xml
mv package2.xml Foo_Bar-%{version}/Foo_Bar.xml


%build
cd Foo_Bar-%{version}
# Empty build section, most likely nothing required.


%install
cd Foo_Bar-%{version}
rm -rf $RPM_BUILD_ROOT docdir
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT Foo_Bar.xml

# Move documentation
mkdir -p docdir
mv $RPM_BUILD_ROOT%{pear_docdir}/* docdir

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_phpdir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 Foo_Bar.xml $RPM_BUILD_ROOT%{pear_xmldir}


%clean
rm -rf $RPM_BUILD_ROOT


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/Foo_Bar.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        Foo_Bar >/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc Foo_Bar-%{version}/docdir/Foo_Bar/*
%{pear_xmldir}/Foo_Bar.xml
%{pear_testdir}/Foo_Bar
%{pear_datadir}/Foo_Bar
%{pear_phpdir}/Foo
%{pear_phpdir}/Foo_Bar.php


%changelog
