%global framework knewstuff

Name:           kf5-%{framework}
Version:        5.14.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 module for downloading application assets

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

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-attica-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}

BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-kcompletion-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kiconthemes-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kitemviews-devel >= %{version}
BuildRequires:  kf5-ktextwidgets-devel >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:  kf5-kxmlgui-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 module for downloading and sharing additional
application data like plugins, themes, motives, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-attica-devel
Requires:       kf5-kxmlgui-devel
Requires:       qt5-qtbase-devel
Requires:       kf5-kservice-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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
%find_lang knewstuff5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f knewstuff5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5NewStuff.so.*
%{_kf5_datadir}/kf5/knewstuff/
%{_kf5_datadir}/kf5/kmoretools/

%files devel
%{_kf5_includedir}/knewstuff_version.h
%{_kf5_includedir}/KNewStuff3
%{_kf5_libdir}/libKF5NewStuff.so
%{_kf5_libdir}/cmake/KF5NewStuff
%{_kf5_archdatadir}/mkspecs/modules/qt_KNewStuff.pri


%changelog
* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
