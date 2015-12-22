%global framework kdelibs4support

Name:           kf5-%{framework}
Version:        5.16.0
Release:        3%{?dist}
Summary:        KDE Frameworks 5 Tier 4 module with porting aid from KDELibs 4
License:        GPLv2+ and LGPLv2+ and BSD
URL:            https://projects.kde.org/projects/frameworks/kdelibs4support

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/portingAids/%{framework}-%{version}.tar.xz

Patch0: kdelibs4support-to-5.17.patch
Patch1: kdelibs4support-hide-kcm_ssl.patch

BuildRequires:  ca-certificates
BuildRequires:  libX11-devel
BuildRequires:  libSM-devel
BuildRequires:  openssl-devel
BuildRequires:  gettext-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  kf5-kdbusaddons-devel >= %{version}

BuildRequires:  kf5-kcompletion-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdesignerplugin-devel >= %{version}
BuildRequires:  kf5-kglobalaccel-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-kguiaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-knotifications-devel >= %{version}
BuildRequires:  kf5-kparts-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-ktextwidgets-devel >= %{version}
BuildRequires:  kf5-kunitconversion-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       ca-certificates
Requires:       kf5-filesystem

%description
This framework provides code and utilities to ease the transition from kdelibs 4
to KDE Frameworks 5. This includes CMake macros and C++ classes whose
functionality has been replaced by code in CMake, Qt and other frameworks.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name} = %{version}-%{release}
# When the split occured
Conflicts:      %{name} < 5.4.0-1
%description    libs
%{summary}.

%package        doc
Summary:        Documentation and user manuals for %{name}
Requires:       %{name} = %{version}-%{release}
Conflicts:      %{name} < 5.4.0-1
BuildArch:      noarch
%description    doc
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kauth-devel
Requires:       kf5-kconfigwidgets-devel
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-kcrash-devel
Requires:       kf5-kdesignerplugin-devel
Requires:       kf5-kdoctools-devel
Requires:       kf5-kemoticons-devel
Requires:       kf5-kguiaddons-devel
Requires:       kf5-kiconthemes-devel
Requires:       kf5-kinit-devel
Requires:       kf5-kitemmodels-devel
Requires:       kf5-knotifications-devel
Requires:       kf5-kparts-devel
Requires:       kf5-ktextwidgets-devel
Requires:       kf5-kunitconversion-devel
Requires:       kf5-kwindowsystem-devel
Requires:       qt5-qtbase-devel
Requires:       kf5-kdbusaddons-devel
Requires:       kf5-karchive-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
# Set absolute BIN_INSTALL_DIR, otherwise CMake will complain about mixed use of
# absolute and relative paths for some reason
# Remove once fixed upstream
%{cmake_kf5} .. \
        -DBIN_INSTALL_DIR=%{_kf5_bindir}
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

#remove taiwan flag and replace it with P.R.C.
rm -rf %{buildroot}%{_kf5_datadir}/kf5/locale/countries/tw/flag.png
cp %{buildroot}%{_kf5_datadir}/kf5/locale/countries/cn/flag.png %{buildroot}%{_kf5_datadir}/kf5/locale/countries/tw

%find_lang kdelibs4support5_qt --with-qt --all-name

#in kde-settings
rm -rf %{buildroot}%{_sysconfdir}/xdg/kdebugrc

%files -f kdelibs4support5_qt.lang
%doc COPYING.LIB README.md
#%{_sysconfdir}/xdg/kdebugrc
%{_kf5_bindir}/kf5-config
%{_kf5_bindir}/kdebugdialog5
%{_kf5_libexecdir}/fileshareset
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/qimageioplugins/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
#%{_kf5_datadir}/kservices5/kded/networkstatus.desktop
%{_kf5_datadir}/kf5/kdoctools/customization
%{_kf5_datadir}/kf5/locale/*
%{_kf5_datadir}/locale/kf5_all_languages
%{_kf5_datadir}/kf5/widgets/
%{_kf5_datadir}/kf5/kssl/ca-bundle.crt
%config %{_kf5_sysconfdir}/xdg/colors
%config %{_kf5_sysconfdir}/xdg/kdebug.areas
# not sure how this is used exactly yet -- rex
%config %{_kf5_sysconfdir}/xdg/ksslcalist

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kf5_libdir}/libKF5KDELibs4Support.so.*
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/designer/*.so
%{_kf5_plugindir}/kio/metainfo.so
%{_kf5_plugindir}/kded/networkstatus.so

%files doc
%{_kf5_docdir}/HTML/*/kdebugdialog5
%{_kf5_docdir}/HTML/*/kcontrol/kcm_ssl/
%{_kf5_mandir}/man1/*
%{_kf5_mandir}/*/man1/*
%exclude %{_kf5_mandir}/man1

%files devel
%{_kf5_libdir}/libKF5KDELibs4Support.so
%{_kf5_libdir}/cmake/KF5KDELibs4Support/
%{_kf5_libdir}/cmake/KF5KDE4Support/
%{_kf5_libdir}/cmake/KDELibs4/
%{_kf5_includedir}/kdelibs4support_version.h
%{_kf5_includedir}/KDELibs4Support/
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Backport from 5.17.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-5
- Rebuild for new 4.0 release

* Fri Oct 16 2015 Cjacker <cjacker@foxmail.com>
- replace taiwan flag.
* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- hide kcm_ssl systemsettings module.

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
