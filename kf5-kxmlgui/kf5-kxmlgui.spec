%global framework kxmlgui

Name:           kf5-%{framework}
Version:        5.15.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for user-configurable main windows

License:        GPLv2+ and LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  libX11-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfig-devel >= %{version}

BuildRequires:  kf5-kitemviews-devel >= %{version}
# session mangement patch needs new api
BuildRequires:  kf5-kconfig-devel >= %{version}
Requires:       kf5-kconfig-core >= %{version}
BuildRequires:  kf5-kglobalaccel-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-ktextwidgets-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-attica-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 solution for user-configurable main windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kconfigwidgets-devel
Requires:       qt5-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kxmlgui5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kxmlgui5_qt.lang
%doc COPYING COPYING.LIB README.md
%config %{_kf5_sysconfdir}/xdg/ui/ui_standards.rc
%{_kf5_libdir}/libKF5XmlGui.so.*
%{_kf5_libexecdir}/ksendbugmail
%{_kf5_datadir}/kf5/kxmlgui/

%files devel
%{_kf5_includedir}/kxmlgui_version.h
%{_kf5_includedir}/KXmlGui
%{_kf5_libdir}/libKF5XmlGui.so
%{_kf5_libdir}/cmake/KF5XmlGui
%{_kf5_archdatadir}/mkspecs/modules/qt_KXmlGui.pri


%changelog
* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
