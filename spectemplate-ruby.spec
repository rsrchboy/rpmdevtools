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


%install
rm -rf $RPM_BUILD_ROOT

 
%check


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
# Include files and dirs below %{ruby_sitelib} (for noarch packages) and
# %{ruby_sitearch} (for arch-dependent packages) as appropriate


%changelog
