%global framework frameworkintegration

Name:           kf5-%{framework}
Version:        5.25.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 4 workspace and cross-framework integration plugins
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

# upstream patches

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}

BuildRequires:  oxygen-fonts-devel

BuildRequires:  libXcursor-devel

Requires:       kf5-filesystem
Requires:       oxygen-fonts

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}.
# last version of the main package before the split
Conflicts:      %{name} < 5.3.0-2
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kiconthemes-devel
Requires:       kf5-kconfigwidgets-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc COPYING.LIB README.md
%{_kf5_datadir}/kf5/infopage/
%{_kf5_datadir}/knotifications5/plasma_workspace.notifyrc

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kf5_libdir}/libKF5Style.so.*
%{_kf5_plugindir}/FrameworkIntegrationPlugin.so

%files devel
%{_kf5_includedir}/frameworkintegration_version.h
%{_kf5_includedir}/KStyle
%{_kf5_libdir}/libKF5Style.so
%{_kf5_libdir}/cmake/KF5FrameworkIntegration


%changelog
* Wed Aug 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Wed Jun 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Fri Apr 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Wed Dec 02 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Add patch to fix two 'quit' menu item in qt systemtray

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Thu Aug 13 2015 Cjacker <cjacker@foxmail.com>
- modify patch0, pure qt application under kf5 always call "show" then "exec"
- if show first and hide then in exec, the dialog may not show at all.

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
