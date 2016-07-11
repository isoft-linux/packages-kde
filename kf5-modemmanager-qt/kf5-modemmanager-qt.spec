%global framework modemmanager-qt

Name:           kf5-%{framework}
Version:        5.24.0
Release:        1%{?dist}
Summary:        A Tier 1 KDE Frameworks module wrapping ModemManager DBus API

License:        LGPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/modemmanager-qt

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/modemmanager-qt-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ModemManager-devel >= 1.0.0

Requires:       kf5-filesystem

Obsoletes:      kf5-libmm-qt < 5.1.95
Provides:       kf5-libmm-qt%{?_isa} = %{version}-%{release}

Provides:       libmm-qt%{?_isa} = %{version}-%{release}

%description
A Qt 5 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-libmm-qt-devel < 5.1.95
Provides:       kf5-libmm-qt-devel = %{version}-%{release}
Provides:       libmm-qt-devel%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
Qt 5 libraries and header files for developing applications
that use ModemManager.

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
%doc README README.md COPYING.LIB
%{_kf5_libdir}/libKF5ModemManagerQt.so.*

%files devel
%{_kf5_libdir}/libKF5ModemManagerQt.so
%{_kf5_libdir}/cmake/KF5ModemManagerQt
%{_kf5_includedir}/ModemManagerQt
%{_kf5_includedir}/modemmanagerqt_version.h
%{_kf5_archdatadir}/mkspecs/modules/qt_ModemManagerQt.pri

%changelog
* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Wed Jun 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- 5.20.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
