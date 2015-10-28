%global framework networkmanager-qt

Name:           kf5-%{framework}
Version:        5.15.0
Release:        3%{?dist}
Summary:        A Tier 1 KDE Frameworks 5 module that wraps NetworkManager DBus API

License:        LGPLv2+
URL:            https://projects.kde.org/projects/frameworks/networkmanager-qt

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

BuildRequires:  pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:  pkgconfig(libnm)

Requires:       NetworkManager >= 0.9.9.0
Requires:       kf5-filesystem

%description
A Tier 1 KDE Frameworks 5 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       pkgconfig(libnm)
Provides:       libnm-qt-devel%{?_isa} = %{version}-%{release}

%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.

%prep
%setup -qn %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5NetworkManagerQt.so.*

%files devel
%{_kf5_libdir}/libKF5NetworkManagerQt.so
%{_kf5_libdir}/cmake/KF5NetworkManagerQt
%{_kf5_includedir}/NetworkManagerQt
%{_kf5_includedir}/networkmanagerqt_version.h
%{_kf5_archdatadir}/mkspecs/modules/qt_NetworkManagerQt.pri

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
