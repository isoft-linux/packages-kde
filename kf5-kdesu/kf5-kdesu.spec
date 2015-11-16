%global framework kdesu

Name:           kf5-%{framework}
Version:        5.16.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 3 integration with su

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
#if user in wheel group, use sudo as default command, fix 'need root password' issue.
#also add '-E' arg to sudo, fix gtk/qt/kde theme issue.
Patch0: kdesu-if-user-in-wheel-default-to-sudo.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  libX11-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kpty-devel >= %{version}

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 integration with su for elevated privileges.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kpty-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kdesu5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdesu5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5Su.so.*
%{_kf5_libexecdir}/kdesu_stub
%{_kf5_libexecdir}/kdesud

%files devel
%doc
%{_kf5_includedir}/kdesu_version.h
%{_kf5_includedir}/KDESu
%{_kf5_libdir}/libKF5Su.so
%{_kf5_libdir}/cmake/KF5Su
%{_kf5_archdatadir}/mkspecs/modules/qt_KDESu.pri


%changelog
* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Tue Nov 10 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-4
- If user in wheel group, use sudo as default

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
