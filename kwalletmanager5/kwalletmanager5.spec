%global         git_commit bd78050

Name:           kwalletmanager5
Summary:        Manage KDE passwords
Version:        15.04.0
Release:        3.20150501git%{?dist}

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/kdeutils/kwalletmanager
# %global revision %(echo %{version} | cut -d. -f3)
# %if %{revision} >= 50
# %global stable unstable
# %else
# %global stable stable
# %endif
# Source0:        http://download.kde.org/%{stable}/applications/%{version}/src/kwalletmanager-%{version}.tar.xz

# Package from git snapshots using releaseme scripts
Source0:        %{name}-%{version}-git%{git_commit}.tar.xz

## upstream patches

BuildRequires:  desktop-file-utils
BuildRequires:  polkit-qt5-1-devel
BuildRequires:  qt5-qtbase-devel

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kwallet-devel

%description
KDE Wallet Manager is a tool to manage the passwords on your KDE system.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# Add Comment key to .desktop file
grep '^Comment=' %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop || \
desktop-file-install \
  --dir=%{buildroot}%{_kf5_datadir}/applications \
  --set-comment="%{summary}" \
  %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null ||:

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null ||:
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null ||:
update-desktop-database -q &> /dev/null ||:
fi

%files
%doc COPYING
%{_bindir}/kwalletmanager5
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/doc/HTML/en/*
%{_datadir}/icons/hicolor/*/apps/kwalletmanager*.*
%{_datadir}/kwalletmanager5/icons/hicolor/*/actions/folder*.*
%{_datadir}/kservices5/*.desktop
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_kf5_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_datadir}/kxmlgui5/kwalletmanager5/kwalletmanager.rc
%{_libexecdir}/kf5/kauth/kcm_kwallet_helper5
%{_kf5_qtplugindir}/kcm_kwallet5.so
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf


%changelog
