%define realname libkipi
%global kf5_version 5.28.0

Name:    kf5-libkipi
Summary: Common plugin infrastructure for KDE image applications
Version: 16.08.3
Release: 1%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegraphics/libs/libkexiv2
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{realname}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules >= %{kf5_version}
BuildRequires: gettext
BuildRequires: kf5-rpm-macros >= %{kf5_version}
BuildRequires: kf5-kconfig-devel >= %{kf5_version}
BuildRequires: kf5-ki18n-devel >= %{kf5_version}
BuildRequires: kf5-kservice-devel >= %{kf5_version}
BuildRequires: kf5-kxmlgui-devel >= %{kf5_version}
BuildRequires: qt5-qtbase-devel qt5-qttools-devel

%description
%{summary}

%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%autosetup -n %{realname}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_kf5_libdir}/libKF5Kipi.so.*
%{_kf5_datadir}/kservicetypes5/kipiplugin.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/kipi.*
#%{_kf5_datadir}/kf5/kipi

%files devel
%{_kf5_libdir}/libKF5Kipi.so
%{_libdir}/cmake/KF5Kipi/
%{_kf5_includedir}/libkipi_version.h
%{_kf5_includedir}/KIPI/

%changelog
* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 16.08.3-1
- 16.08.3-1

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.0.0-4.git
- Rebuild for new 4.0 release

