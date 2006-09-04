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
%setup -q -n Foo_Bar-%{version}
mv ../package.xml .


%build


%install
rm -rf $RPM_BUILD_ROOT docdir
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT package.xml

# Move documentation
mkdir -p docdir
mv $RPM_BUILD_ROOT%{pear_docdir}/* docdir

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_phpdir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 package.xml $RPM_BUILD_ROOT%{pear_xmldir}/Foo_Bar.xml


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
%doc docdir/Foo_Bar/*
%{pear_xmldir}/Foo_Bar.xml
%{pear_testdir}/Foo_Bar
%{pear_datadir}/Foo_Bar
%{pear_phpdir}/Foo
%{pear_phpdir}/Foo_Bar.php


%changelog
