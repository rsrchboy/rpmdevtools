# --- For kernel modules ------------------------------------------------------
# # "uname -r" output of the kernel to build for, the running one
# # if none was specified with "--define 'kernel <uname -r>'"
# %{!?kernel: %{expand: %%define        kernel          %(uname -r)}}
# 
# %define       kversion        %(echo %{kernel} | sed -e s/smp// -)
# %define       krelver         %(echo %{kversion} | tr -s '-' '_')
# %if %(echo %{kernel} | grep -c smp)
#       %{expand:%%define ksmp -smp}
# %endif
# -----------------------------------------------------------------------------

Summary:        <summary>
Name:           <app name>
Version:        <app version>
Release:        0.fdr.x
Epoch:          0
URL:            http://
License:        <license>
Group:          <group>
Source0:        <primary source> 
#Source99:       <for original Red Hat spec>
#Patch0:         
#Patch1:         
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:
Requires:       <requirements>
#Conflicts:      
#Obsoletes:      
#BuildConflicts:  
#Requires(pre,post): 

%description

#%package        devel
#Summary:        
#Group:          Development/Libraries
#Requires:       %{name} = %{epoch}:%{version}-%{release}

#%description    devel

# -----------------------------------------------------------------------------

%prep
%setup -q

# -----------------------------------------------------------------------------

%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%configure
make %{?_smp_mflags}
  
#make test
#make check

# -----------------------------------------------------------------------------

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

# -----------------------------------------------------------------------------

%clean
rm -rf %{buildroot}

# -----------------------------------------------------------------------------

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

# -----------------------------------------------------------------------------

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

%exclude %{_libdir}/*.la
%exclude %{_infodir}/dir

# -----------------------------------------------------------------------------

%changelog
* Fri Apr 04 2003 Your Name <you[AT]your.domain> - epoch:version-release
- Initial RPM release.
