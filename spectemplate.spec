Name:           <app name>
Version:        <app version>
Release:        0.fdr.x
Epoch:          0
Summary:        <summary>

Group:          <group>
License:        <license>
URL:            http://
Source0:        <method>://<primary source>
#Source99:       <for original Red Hat or other upstream spec>
#Patch0:         
#Patch1:         
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#---For kernel modules------------------------------------------------
# # "uname -r" output of the kernel to build for, the running one
# # if none was specified with "--define 'kernel <uname -r>'"
# %{!?kernel: %{expand: %%define        kernel          %(uname -r)}}
#
# %define       kversion        %(echo %{kernel} | sed -e s/smp// -)
# %define       krelver         %(echo %{kversion} | tr -s '-' '_')
# %if %(echo %{kernel} | grep -c smp)
#       %{expand:%%define ksmp -smp}
# %endif
#---------------------------------------------------------------------

BuildRequires:  
Requires:       <requirements>
#Conflicts:      
#Obsoletes:      
#BuildConflicts: 
#Requires(pre,post): 

%description
<Long description of package here>
<Multiple lines are fine>

#%package        devel
#Summary:        
#Group:          Development/Libraries
#Requires:       %{name} = %{epoch}:%{version}-%{release}

#%description    devel
#<Long description of sub-package here>
#<Multiple lines are fine>


%prep
%setup -q


%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%configure
make %{?_smp_mflags}

#make test
#make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


# ldconfig's for packages that install %{_libdir}/*.so.*
# -> Don't forget Requires(post,postun): /sbin/ldconfig
# ...and install-info's for ones that install %{_infodir}/*.info*
# -> Don't forget Requires(post,preun): /sbin/install-info

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi

%postun
/sbin/ldconfig


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
* Fri May 03 2003 Your Name <you[AT]your.domain> - epoch:version-release
- Initial RPM release.
