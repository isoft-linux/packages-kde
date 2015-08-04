Name:           bluedevil
Summary:        Bluetooth stack for KDE
Version:        5.3.2
Release:        1

License:        GPLv2+
URL:            https://projects.kde.org/projects/extragear/base/bluedevil

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Patch0:  bluedevil-5.3-adapt-to-bluez-qt-5-11-API-changes.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
# 5.11 is when kf5-bluez-qt became Framework and changed API
BuildRequires:  kf5-bluez-qt-devel >= 5.11
BuildRequires:  kf5-kded-devel

BuildRequires:  shared-mime-info

BuildRequires:  desktop-file-utils

Provides:       dbus-bluez-pin-helper

Obsoletes:      kbluetooth < 0.4.2-3
Obsoletes:      bluedevil-devel < 2.0.0-0.10

Requires:       pulseaudio-module-bluetooth
Requires:       kf5-kded

# When -autostart was removed
Obsoletes:      bluedevil-autostart < 5.2.95

%description
BlueDevil is the bluetooth stack for KDE.


%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .kf5bluezAPI


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang bluedevil5  --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.bluedevilsendfile.desktop
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.bluedevilwizard.desktop


%post
touch --no-create %{_datadir}/mime/packages &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
update-desktop-database -q &> /dev/null
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
update-desktop-database -q &> /dev/null
update-mime-database %{_datadir}/mime &> /dev/null || :

%files -f bluedevil5.lang
%doc README
%{_kf5_bindir}/bluedevil-sendfile
%{_kf5_bindir}/bluedevil-wizard
%{_libexecdir}/bluedevil-*
%{_kf5_qtplugindir}/kcm_*.so
%{_kf5_qtplugindir}/kio_*.so
%{_kf5_plugindir}/kded/*.so
%{_kf5_qtplugindir}/bluetoothfileitemaction.so
%{_kf5_datadir}/remoteview/bluetooth-network.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/knotifications5/bluedevil.notifyrc
%{_kf5_datadir}/applications/org.kde.bluedevilsendfile.desktop
%{_kf5_datadir}/applications/org.kde.bluedevilwizard.desktop
%{_kf5_datadir}/bluedevilwizard/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%{_kf5_qmldir}/org/kde/plasma/private/bluetooth/
%{_datadir}/mime/packages/*.xml


%changelog
