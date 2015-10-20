Name:           kwrited
Version:        5.4.2
Release:        1
Summary:        KDE Write Daemon

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/kwrited

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

Patch0:         kwrited-call-setgroups.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kpty-devel
BuildRequires:  kf5-kdelibs4support-devel

Requires:       kf5-filesystem

# Owns /usr/share/knotifications5
Requires:       kf5-knotifications

# TODO: Remove once kwrited is split from kde-workspace
Conflicts:      kde-workspace < 5.0.0-1

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .setgroups

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%doc COPYING
%{_bindir}/kwrited
%{_sysconfdir}/xdg/autostart/kwrited-autostart.desktop
%{_kf5_datadir}/knotifications5/kwrited.notifyrc


%changelog
* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

