%global framework sonnet

Name:           kf5-%{framework}
Version:        5.16.0
Release:        3%{?dist}
Summary:        KDE Frameworks 5 Tier 1 solution for spell checking

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

# Fix failed to save ignore word to ~/.config/KDE/Sonnet.conf issue
Patch0: 0001-save-ignore-word-to-conf.patch

BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel
BuildRequires:  hunspell-devel
BuildRequires:  aspell-devel
BuildRequires:  zlib-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 5 Tier 1 solution for spell checking.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        core
Summary:        Non-gui part of the Sonnet framework

%description    core
Non-gui part of the Sonnet framework provides low-level spell checking tools

%package        ui
Summary:        GUI part of the Sonnet framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    ui
GUI part of the Sonnet framework provides widgets with spell checking support.


%prep
%setup -q -n %{framework}-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang_kf5 sonnet5_qt


%files
%doc COPYING.LIB README.md

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%files core
%{_kf5_libdir}/libKF5SonnetCore.so.*
%dir %{_kf5_plugindir}/sonnet/
%{_kf5_plugindir}/sonnet/hunspell.so
%{_kf5_plugindir}/sonnet/aspell.so
%dir %{_kf5_datadir}/kf5/sonnet/
%{_kf5_datadir}/kf5/sonnet/trigrams.map

%post ui -p /sbin/ldconfig
%postun ui -p /sbin/ldconfig

%files ui -f sonnet5_qt.lang
%{_kf5_libdir}/libKF5SonnetUi.so.*

%files devel
%{_kf5_includedir}/sonnet_version.h
%{_kf5_includedir}/SonnetCore
%{_kf5_includedir}/SonnetUi
%{_kf5_libdir}/libKF5SonnetCore.so
%{_kf5_libdir}/libKF5SonnetUi.so
%{_kf5_libdir}/cmake/KF5Sonnet
%{_kf5_archdatadir}/mkspecs/modules/qt_SonnetCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_SonnetUi.pri


%changelog
* Fri Nov 27 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix failed to add ignore word to ~/.config/KDE/Sonnet.conf issue.

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
