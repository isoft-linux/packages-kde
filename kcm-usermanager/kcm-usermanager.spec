Name:           kcm-usermanager
Version:        1.2.0
Release:        3
Summary:        User management tool for plasma workspace 

License:        GPLv3+
Source0:        user-manager_5.2.90+git20150330.orig.tar.xz
Patch0:         user-manager-faceicon-follow-kde-requires.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  boost-devel
# we need the unified libsystemd.so, which was introduced in systemd 209
BuildRequires:  systemd-devel >= 209
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-rpm-macros
Requires:   accountsservice
%description
user management tool for the Plasma workspace.
A System Settings module for managing users on your system.

%prep
%setup -q -n user-manager-5.2.90+git20150330/
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ../
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
/
#%license LICENSE
#%doc NEWS README.md
#%{_kf5_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf
#%{_kf5_qtplugindir}/kcm_systemd.so
#%{_kf5_libexecdir}/kauth/kcmsystemdhelper
#%{_kf5_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
#%{_kf5_datadir}/kservices5/kcm_systemd.desktop
#%{_kf5_datadir}/kservices5/settings-system-administration.desktop
#%{_kf5_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy

%changelog
