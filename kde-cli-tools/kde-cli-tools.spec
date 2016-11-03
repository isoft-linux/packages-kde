%global kf5_version 5.27.0

Name:           kde-cli-tools
Version:        5.8.3
Release:        1%{?dist}
Summary:        Tools based on KDE Frameworks 5 to better interact with the system

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/kde-cli-tools

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Patch0: konqueror.patch

BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-rpm-macros

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires:  kf5-kinit-devel >= %{kf5_version}
BuildRequires:  kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  kf5-kcmutils-devel >= %{kf5_version}
BuildRequires:  kf5-kdesu-devel >= %{kf5_version}
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-kwindowsystem-devel >= %{kf5_version}

Requires:       kf5-filesystem

# probably could be unversioned, but let's play it safe so we can avoid adding Conflicts: -- rex
Requires:       kdesu = 1:%{version}-%{release}

# libkdeinit5_kcmshell5
%{?kf5_kinit_requires}

%description
Provides several KDE and Plasma specific command line tools to allow
better interaction with the system.

%package -n kdesu
Summary: Runs a program with elevated privileges
Epoch: 1
Conflicts: kde-runtime < 14.12.3-2
Conflicts: kde-runtime-docs < 14.12.3-2
## added deps below avoidable to due main pkg Requires: kdesu -- rex
# upgrade path, when kdesu was introduced
#Obsoletes: kde-cli-tools < 5.2.1-3
#Requires: %{name} = %{version}-%{release}
%description -n kdesu
%{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kdeclitools_qt --with-qt --with-kde --all-name

ln -s %{_kf5_libexecdir}/kdesu %{buildroot}%{_bindir}/kdesu

%files -f kdeclitools_qt.lang
%{_bindir}/kcmshell5
%{_bindir}/kde-open5
%{_bindir}/kdecp5
%{_bindir}/kdemv5
%{_bindir}/keditfiletype5
%{_bindir}/kioclient5
%{_bindir}/kmimetypefinder5
%{_bindir}/kstart5
%{_bindir}/ksvgtopng5
%{_bindir}/ktraderclient5
%{_kf5_libexecdir}/kdeeject
%{_kf5_libdir}/libkdeinit5_kcmshell5.so
%{_kf5_qtplugindir}/kcm_filetypes.so
%{_kf5_datadir}/kservices5/filetypes.desktop

%files -n kdesu
%{_bindir}/kdesu
%{_kf5_libexecdir}/kdesu
%{_mandir}/man1/kdesu.1.gz
%{_datadir}/doc/HTML/*/kdesu


%changelog
* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Tue Dec 01 2015 kun.li@i-soft.com.cn - 5.4.3-3
- add konqueror.patch

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

