Name:           <app name>
Version:        <app version>
Release:        x
Summary:        <summary>

Group:          <group>
License:        <license>
URL:            http://
Source0:        <method>://<primary source>
#Source99:       <for original Red Hat or upstream spec as *.spec.upstream>
#Patch0:         
#Patch1:         
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  
Requires:       <requirements>
#Requires(pre):  
#Requires(post): 
#Conflicts:      
#Obsoletes:      
#BuildConflicts: 

%description
<Long description of package here>
<Multiple lines are fine>

#%package        devel
#Summary:        
#Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

#%description    devel
#<Long description of subpackage here>
#<Multiple lines are fine>


%prep
%setup -q


%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
# For GConf apps: prevent schemas from being installed at this stage
#export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
# Note: the find_lang macro requires gettext
%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%check || :
#make test
#make check


%clean
rm -rf $RPM_BUILD_ROOT


# ldconfig's for packages that install %{_libdir}/*.so.*
# -> Don't forget Requires(post) and Requires(postun): /sbin/ldconfig
# ...and install-info's for ones that install %{_infodir}/*.info*
# -> Don't forget Requires(post) and Requires(preun): /sbin/install-info

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
# For GConf apps: install schemas as system default
#export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
#gconftool-2 --makefile-install-rule \
#  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi
# For GConf apps: uninstall app's system default schemas
#export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
#gconftool-2 --makefile-uninstall-rule \
#  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_mandir}/man[^3]/*

#%files devel
#%defattr(-,root,root,-)
#%doc HACKING
#%{_libdir}/*.a
#%{_libdir}/*.so
#%{_mandir}/man3/*


%changelog
* Fri May 03 2003 Your Name <you[AT]your.domain> - (epoch:)version-release
- Initial RPM release.
