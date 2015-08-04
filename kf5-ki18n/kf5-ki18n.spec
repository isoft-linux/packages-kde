%global framework ki18n

Name:           kf5-%{framework}
Version:        5.12.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon for localization

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
Patch0:         ki18n-less-warning-to-stdout.patch

BuildRequires:  perl

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  gettext

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 1 addon for localization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gettext
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
%find_lang ki18n5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f ki18n5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_qtplugindir}/kf5/ktranscript.so
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n5/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n5/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n5/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n5/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n5/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n5/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n5/

%files devel
%{_kf5_includedir}/ki18n_version.h
%{_kf5_includedir}/KI18n/
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_libdir}/cmake/KF5I18n/
%{_kf5_archdatadir}/mkspecs/modules/qt_KI18n.pri


%changelog
