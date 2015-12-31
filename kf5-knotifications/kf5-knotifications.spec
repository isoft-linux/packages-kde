%global framework knotifications

Name:           kf5-%{framework}
Version:        5.16.0
Release:        4%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution with abstraction for system notifications

License:        LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

# KDEBUG-357091 QSystemTrayIcon has no API to control status 
# http://code.qt.io/cgit/qt/qtbase.git/tree/src/platformsupport/dbustray/qdbustrayicon.cpp#n76
# so if default status is Passive, QSystemTrayIcon will be hided into systemtray
# applet's ExpandedRepresentation area, it is visible only by click on the 
# expanding triangle.
#Patch0: 0001-default-status-active.patch

BuildRequires:  libX11-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  phonon-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qttools-devel

BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcodecs-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 solution with abstraction for system
notifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang knotifications5_qt --with-qt --all-name

# We own the folder
mkdir -p %{buildroot}/%{_kf5_datadir}/knotifications5


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f knotifications5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Notifications.so.*
%{_kf5_datadir}/kservicetypes5/knotificationplugin.desktop
%{_kf5_datadir}/knotifications5

%files devel
%{_kf5_includedir}/knotifications_version.h
%{_kf5_includedir}/KNotifications
%{_kf5_libdir}/libKF5Notifications.so
%{_kf5_libdir}/cmake/KF5Notifications
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{_kf5_archdatadir}/mkspecs/modules/qt_KNotifications.pri


%changelog
* Thu Dec 31 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Drop set Active status by default patch.

* Thu Dec 24 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix KDEBUG-357091 QSystemTrayIcon default status is Active now.

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
