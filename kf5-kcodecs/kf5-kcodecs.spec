%global framework kcodecs

Name:           kf5-%{framework}
Version:        5.14.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with string manipulation methods

License:        GPLv2+ and LGPLv2+ and BSD
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
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 1 addon with string manipulation methods.


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
%make_install -C %{_target_platform}

%find_lang kcodecs5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kcodecs5_qt.lang
%doc COPYING COPYING.LIB README.md
%{_kf5_libdir}/libKF5Codecs.so.*

%files devel
%{_kf5_includedir}/kcodecs_version.h
%{_kf5_includedir}/KCodecs
%{_kf5_libdir}/libKF5Codecs.so
%{_kf5_libdir}/cmake/KF5Codecs
%{_kf5_archdatadir}/mkspecs/modules/qt_KCodecs.pri


%changelog
* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
