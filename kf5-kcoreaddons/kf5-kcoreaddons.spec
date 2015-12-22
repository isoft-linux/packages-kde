%global framework kcoreaddons

Name:           kf5-%{framework}
Version:        5.16.0
Release:        3%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore

License:        GPLv2+ and GPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz
Patch0: kcoreaddons-backport-from-5.17.0.patch

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  shared-mime-info

Requires:       kf5-filesystem

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel

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
%make_install -C %{_target_platform}
%find_lang kcoreaddons5_qt --with-qt --all-name


%post
/sbin/ldconfig
touch --no-create %{_datadir}/mime/packages &> /dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
update-mime-database  %{_datadir}/mime &> /dev/null || :

%files -f kcoreaddons5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/desktoptojson
%{_kf5_libdir}/libKF5CoreAddons.so.*
%{_kf5_datadir}/mime/packages/kde5.xml

%files devel
%{_kf5_includedir}/kcoreaddons_version.h
%{_kf5_includedir}/KCoreAddons/
%{_kf5_libdir}/libKF5CoreAddons.so
%{_kf5_libdir}/cmake/KF5CoreAddons
%{_kf5_archdatadir}/mkspecs/modules/qt_KCoreAddons.pri


%changelog
* Mon Dec 21 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Backport from 5.17.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-4
- Add some patches from reviewboard

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
