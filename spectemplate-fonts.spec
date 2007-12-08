%define fontname        FONTNAME
%define fontdir         %{_datadir}/fonts/%{fontname}
%define fontconfdir     %{_sysconfdir}/fonts/conf.d

Name:           %{fontname}-fonts
Version:        
Release:        1%{?dist}
Summary:        

Group:          User Interface/X
License:        
URL:            
Source0:        
Source1:        %{name}-fontconfig.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  

%description


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

install -dm 755 $RPM_BUILD_ROOT%{fontdir}
# for example: install -pm 644 *.ttf *.otf $RPM_BUILD_ROOT%{fontdir}

install -dm 755 $RPM_BUILD_ROOT%{fontconfdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{fontconfdir}/<XX>-%{fontname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ -x %{_bindir}/fc-cache ] ; then
    %{_bindir}/fc-cache -f %{fontdir} || :
fi

%postun
if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then
    %{_bindir}/fc-cache -f %{fontdir} || :
fi


%files
%defattr(644,root,root,755)
%doc
%config(noreplace) %{fontconfdir}/XX-%{fontname}.conf
%dir %{fontdir}/
%{fontdir}/*.ttf
%{fontdir}/*.otf


%changelog
