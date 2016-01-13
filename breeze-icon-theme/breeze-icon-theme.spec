%define framework breeze-icons

Name:    breeze-icon-theme
Summary: Breeze icon theme for KF5
Version: 5.16.0
EPoch: 2 
Release: 4
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
Provides: breeze-icons = %{version}-%{release}

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
/usr/sbin/hardlink -c -v %{buildroot}%{_datadir}/icons/breeze

# %%ghost icon.cache
touch  %{buildroot}%{_datadir}/icons/breeze/icon-theme.cache
touch  %{buildroot}%{_datadir}/icons/breeze-dark/icon-theme.cache


%post 
touch --no-create %{_datadir}/icons/breeze &> /dev/null || :
touch --no-create %{_datadir}/icons/breeze-dark &> /dev/null || :

%posttrans 
gtk-update-icon-cache %{_datadir}/icons/breeze &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/breeze-dark &> /dev/null || :

%postun 
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/breeze &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/breeze &> /dev/null || :
touch --no-create %{_datadir}/icons/breeze-dark &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/breeze-dark &> /dev/null || :
fi

%files 
%dir %{_datadir}/icons/breeze/
%ghost %{_datadir}/icons/breeze/icon-theme.cache
%{_datadir}/icons/breeze/index.theme
%{_datadir}/icons/breeze/{actions,apps,categories,devices,emblems,emotes,mimetypes,places,status}

%dir %{_datadir}/icons/breeze-dark/
%ghost %{_datadir}/icons/breeze-dark/icon-theme.cache
%{_datadir}/icons/breeze-dark/index.theme
%{_datadir}/icons/breeze-dark/{actions,apps,categories,devices,emblems,emotes,mimetypes,places,status}


%changelog
* Wed Jan 13 2016 fj <fujiang.zhu@i-soft.com.cn>  - 2:5.16.0-4
- Add new icons:security-high-red.svg(64*64,22*22)

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.04.3-3
- Rebuild for new 4.0 release

