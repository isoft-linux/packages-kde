Name:           kwrited
Version:        5.8.3
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

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kpty-devel >= 5.13.0
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

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
%{_kf5_qtplugindir}/kf5/kded/kwrited.so
%{_kf5_datadir}/knotifications5/kwrited.notifyrc

%changelog
* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

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

