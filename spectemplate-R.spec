%global packname %(echo %{name} | sed -e 's/^R-//')
%global packrel 1
%ifarch noarch
%global rlibdir %{_datadir}/R/library
%else
%global rlibdir %{_libdir}/R/library
%endif

Name:           
Version:        
Release:        1%{?dist}
Summary:        

Group:          Applications/Engineering
License:        
URL:            http://cran.r-project.org/web/packages/%{packname}/
Source0:        ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}-%{packrel}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      
BuildRequires:  R-devel
BuildRequires:  tetex-latex
Requires(post): R
Requires(postun): R
Requires:       R

%description


%prep
%setup -q -c -n %{packname}


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{rlibdir}
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f $RPM_BUILD_ROOT%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%clean
rm -rf $RPM_BUILD_ROOT


%post
%{_R_make_search_index}

%postun
%{_R_make_search_index}


%files
%defattr(-,root,root,-)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/latex
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/man
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/CONTENTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/R-ex
%{rlibdir}/%{packname}/help


%changelog
