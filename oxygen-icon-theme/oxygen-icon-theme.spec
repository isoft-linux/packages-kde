Name:    oxygen-icon-theme
Summary: Oxygen icon theme
Version: 15.04.3
Release: 2
License: LGPLv3+ 

URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

Source0: http://download.kde.org/%{stable}/applications/%{version}/src/oxygen-icons-%{version}.tar.xz
BuildArch: noarch

BuildRequires: cmake
BuildRequires: hardlink
BuildRequires: kde-filesystem

# upstream name
Provides: oxygen-icons = %{version}-%{release}
Provides: system-kde-icon-theme = %{version}-%{release}

%description
%{summary}.


%prep
%setup -q -n oxygen-icons-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# As of 4.12.3, hardlink reports
#Directories 78
#Objects 6926
#IFREG 6848
#Mmaps 902
#Comparisons 902
#Linked 902
#saved 8339456
/usr/sbin/hardlink -c -v %{buildroot}%{_kde4_iconsdir}/oxygen

# create/own all potential dirs
mkdir -p %{buildroot}%{_kde4_iconsdir}/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}

# %%ghost icon.cache
touch  %{buildroot}%{_kde4_iconsdir}/oxygen/icon-theme.cache


%post 
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans 
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :

%postun 
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
fi

%files 
%doc AUTHORS CONTRIBUTING COPYING
%dir %{_kde4_iconsdir}/oxygen/
%ghost %{_kde4_iconsdir}/oxygen/icon-theme.cache
%{_kde4_iconsdir}/oxygen/index.theme
%{_kde4_iconsdir}/oxygen/*x*/
%{_kde4_iconsdir}/oxygen/scalable/


%changelog
