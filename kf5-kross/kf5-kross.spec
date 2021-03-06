%global framework kross

Name:           kf5-%{framework}
Version:        5.29.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 solution for multi-language application scripting

License:        LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel

BuildRequires:  kf5-kcompletion-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}

Requires:       %{name}-core%{_isa} = %{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{version}-%{release}

%description
Kross is a scripting bridge to embed scripting functionality into an
application. It supports QtScript as a scripting interpreter backend.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-ki18n-devel
Requires:       kf5-kiconthemes-devel
Requires:       kf5-kio-devel
Requires:       kf5-kparts-devel
Requires:       kf5-kwidgetsaddons-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtscript-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core
Summary:        Non-gui part of the Kross framework
Requires:       kf5-filesystem
%description    core
Non-gui part of the Kross framework.

%package        ui
Summary:        Gui part of the Kross framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       kf5-filesystem
%description    ui
Gui part of the Kross framework.

%package        doc
Summary:        Documentation and user manuals for the Kross framework
%description    doc
Documentation and user manuals for the Kross framework


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kross5_qt --with-qt --all-name


%files

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig

%files core -f kross5_qt.lang
%{_kf5_bindir}/kf5kross
%{_kf5_libdir}/libKF5KrossCore.so.*
%{_kf5_qtplugindir}/krossqts.so
%{_kf5_qtplugindir}/script/krossqtsplugin.so

%post ui -p /sbin/ldconfig
%postun ui -p /sbin/ldconfig

%files ui
%{_kf5_libdir}/libKF5KrossUi.so.*
%{_kf5_qtplugindir}/krossmoduleforms.so
%{_kf5_qtplugindir}/krossmodulekdetranslation.so

%files doc
%doc COPYING.LIB README.md
%{_kf5_datadir}/man/man1/*

%files devel
%{_kf5_includedir}/kross_version.h
%{_kf5_includedir}/KrossUi
%{_kf5_includedir}/KrossCore
%{_kf5_libdir}/libKF5KrossCore.so
%{_kf5_libdir}/libKF5KrossUi.so
%{_kf5_libdir}/cmake/KF5Kross
%{_kf5_archdatadir}/mkspecs/modules/qt_KrossCore.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KrossUi.pri


%changelog
* Wed Dec 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Wed Nov 23 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Thu Nov 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Tue Nov 01 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Wed Aug 17 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Wed Jun 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Tue Apr 12 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- 5.20.0

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
