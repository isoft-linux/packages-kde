%define framework oxygen-icons5

Name:    oxygen-icon-theme
Summary: Oxygen icon theme for KF5
Version: 5.16.0
EPoch: 2 
Release: 3
License: LGPLv3+ 

URL:     http://www.kde.org/
%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/portingAids/%{framework}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: cmake
BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules >= %{version}

BuildRequires: hardlink
BuildRequires: kde-filesystem

# upstream name
Provides: oxygen-icons = %{version}-%{release}
Provides: oxygen-icons5 = %{version}-%{release}
Provides: system-kde-icon-theme = %{version}-%{release}

%description
%{summary}.


%prep
%setup -q -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
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
/usr/sbin/hardlink -c -v %{buildroot}%{_datadir}/icons/oxygen

# create/own all potential dirs
mkdir -p %{buildroot}%{_datadir}/icons/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}

# %%ghost icon.cache
touch  %{buildroot}%{_datadir}/icons/oxygen/icon-theme.cache


%post 
touch --no-create %{_datadir}/icons/oxygen &> /dev/null || :

%posttrans 
gtk-update-icon-cache %{_datadir}/icons/oxygen &> /dev/null || :

%postun 
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/oxygen &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/oxygen &> /dev/null || :
fi

%files 
%doc AUTHORS CONTRIBUTING COPYING
%dir %{_datadir}/icons/oxygen/
%ghost %{_datadir}/icons/oxygen/icon-theme.cache
%{_datadir}/icons/oxygen/index.theme
%{_datadir}/icons/oxygen/*x*/
%{_datadir}/icons/oxygen/scalable/


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.04.3-3
- Rebuild for new 4.0 release

