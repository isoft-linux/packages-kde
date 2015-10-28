%global framework bluez-qt
%global plasma_version 5.3.0

Name:           kf5-%{framework}
Summary:        A Qt wrapper for Bluez
Version:        5.15.0
Release:        3%{?dist}

License:        LGPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/bluez-qt

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{plasma_version}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

# For %%{_udevrulesdir}
BuildRequires:  systemd

Requires:       kf5-filesystem
Requires:       bluez >= 5

%description
BluezQt is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}
Obsoletes:      libbluedevil-devel < 5.2.90
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
Development files for %{name}.


%prep
%setup -q -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING.LIB README.md
%{_libdir}/libKF5BluezQt.so.*
%{_kf5_qmldir}/org/kde/bluezqt/
%{_udevrulesdir}/61-kde-bluetooth-rfkill.rules

%files devel
%{_kf5_includedir}/BluezQt
%{_kf5_includedir}/bluezqt_version.h
%{_kf5_libdir}/libKF5BluezQt.so
%{_kf5_libdir}/cmake/KF5BluezQt
%{_qt5_archdatadir}/mkspecs/modules/qt_BluezQt.pri


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
