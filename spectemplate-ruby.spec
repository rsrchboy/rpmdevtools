%{!?ruby_sitelib: %global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

Name:           
Version:        
Release:        1%{?dist}
Summary:        

Group:          Development/Languages

License:        
URL:            
Source0:        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      
BuildRequires:  ruby ruby-devel
Requires:       ruby(abi) = 1.8
# If this package is mainly a ruby library, it should provide
# whatever people have to require in their ruby scripts to use the library
# For example, if people use this lib with "require 'foo'", it should provide
# ruby(foo)
Provides:       ruby(LIBNAME)

%description


%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT

 
%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
# For noarch packages: ruby_sitelib
%{ruby_sitelib}/*
# For arch-specific packages: ruby_sitearch
%{ruby_sitearch}/*


%changelog
