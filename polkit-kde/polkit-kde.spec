%global         base_name polkit-kde-agent-1

Name:           polkit-kde
Summary:        PolicyKit integration for KDE Desktop
Version:        5.4.2
Release:        2

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/polkit-kde-agent-1

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz


BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-knotifications-devel

BuildRequires:  polkit-qt5-1-devel

Provides: PolicyKit-authentication-agent = %{version}-%{release}
Provides: polkit-kde-1 = %{version}-%{release}
Provides: polkit-kde-agent-1 = %{version}-%{release}

Obsoletes: PolicyKit-kde < 4.5

# Add explicit dependency on polkit, since polkit-libs were split out
Requires: polkit

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.


%prep
%setup -q -n %{base_name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang polkit-kde-authentication-agent-1 --with-kde

# Move the agent from libexec to libexec/kf5
sed -i "s/Exec=\/usr\/libexec\//Exec=\/usr\/libexec\/kf5\//" %{buildroot}/%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
mkdir -p %{buildroot}/%{_kf5_libexecdir}/
mv %{buildroot}/%{_libexecdir}/polkit-kde-authentication-agent-1 \
   %{buildroot}/%{_kf5_libexecdir}


%files -f polkit-kde-authentication-agent-1.lang
%doc COPYING
%{_kf5_libexecdir}/polkit-kde-authentication-agent-1
%{_sysconfdir}/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf5_datadir}/knotifications5/policykit1-kde.notifyrc


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

