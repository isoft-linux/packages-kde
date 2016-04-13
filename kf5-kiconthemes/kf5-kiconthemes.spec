%global framework kiconthemes

Name:           kf5-%{framework}
Version:        5.21.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 3 integration module with icon themes

License:        LGPLv2+ and GPLv2+
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
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel

BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kconfigwidgets-devel  >= %{version}
BuildRequires:  kf5-kwidgetsaddons-devel  >= %{version}
BuildRequires:  kf5-kitemviews-devel  >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 integration module with icon themes


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

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
%find_lang kiconthemes5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kiconthemes5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/kiconfinder5
%{_kf5_libdir}/libKF5IconThemes.so.*

%files devel
%{_kf5_includedir}/kiconthemes_version.h
%{_kf5_includedir}/KIconThemes
%{_kf5_libdir}/libKF5IconThemes.so
%{_kf5_libdir}/cmake/KF5IconThemes
%{_kf5_archdatadir}/mkspecs/modules/qt_KIconThemes.pri


%changelog
* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

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
