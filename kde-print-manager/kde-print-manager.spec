Name:    kde-print-manager
Summary: Printer management for KDE
Version: 15.11.80
Release: 2 

License: GPLv2+ and LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdeutils/print-manager
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/print-manager-%{version}.tar.xz
# Plasma init/upgrade script
Source1: 01-print-manager.js

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-ki18n-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
# required because of Qt5Designer - should be removed in final release
BuildRequires: qt5-qttools-devel

BuildRequires: cups-devel >= 1.5.0

Requires: plasma-workspace

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# currently requires local cups for majority of proper function
Requires: cups
# required for the com.redhat.NewPrinterNotification D-Bus service
Requires: system-config-printer-libs

%description
Printer management for KDE.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n print-manager-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# show print-manager plasmoid by default
#install -m644 -p -D %{SOURCE1} %{buildroot}%{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/01-print-manager.js


%files
%{_bindir}/kde-add-printer
%{_bindir}/kde-print-queue
%{_bindir}/configure-printer
%{_qt5_prefix}/qml/org/kde/plasma/printmanager/
%{_kf5_datadir}/kservices5/kcm_printer_manager.desktop
%{_kf5_datadir}/kservices5/kded/printmanager.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.printmanager.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/
%{_datadir}/printmanager/
%{_datadir}/applications/*.desktop
#{_datadir}/plasma/shells/org.kde.plasma.desktop/updates/01-print-manager.js

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
# private unversioned library
%{_libdir}/libkcupslib.so
%{_kf5_qtplugindir}/kcm_printer_manager.so
%{_kf5_qtplugindir}/kded_printmanager.so


%changelog
* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-4
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

