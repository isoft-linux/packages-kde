%define framework kpackage

Name:           kf5-%{framework}
Version:        5.16.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 2 library to load and install packages as plugins

License:        LGPLv2+
URL:            https://projects.kde.org/projects/frameworks/kpackage

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

BuildRequires:  kf5-karchive-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 2 library to load and install non-binary packages as
if they were plugins.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kcoreaddons-devel

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
%find_lang kpackage5_qt --with-qt --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kpackage5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Package.so.*
%{_kf5_bindir}/kpackagetool5
%{_kf5_datadir}/kservicetypes5/kpackage-packagestructure.desktop
%{_mandir}/man1/kpackagetool5.1.gz

%files devel
%{_kf5_includedir}/kpackage_version.h
%{_kf5_includedir}/KPackage
%{_kf5_libdir}/libKF5Package.so
%{_kf5_libdir}/cmake/KF5Package


%changelog
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
