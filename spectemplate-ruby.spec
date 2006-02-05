%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitedir']")}
%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

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
# %{ruby_sitelib} for noarch, %{ruby_sitearch} for non-noarch
Requires:       %{ruby_sitelib}
Requires:       %{ruby_sitearch}

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
# For noarch packages: sitelib
%{ruby_sitelib}/*
# For arch-specific packages: sitearch
%{ruby_sitearch}/*


%changelog
