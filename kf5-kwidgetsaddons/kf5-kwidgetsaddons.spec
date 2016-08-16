%global framework kwidgetsaddons

Name:           kf5-%{framework}
Version:        5.25.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets

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

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets.


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
%find_lang kwidgetsaddons5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kwidgetsaddons5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5WidgetsAddons.so.*
%{_kf5_datadir}/kf5/kcharselect

%files devel
%{_kf5_includedir}/kwidgetsaddons_version.h
%{_kf5_includedir}/KWidgetsAddons
%{_kf5_libdir}/libKF5WidgetsAddons.so
%{_kf5_libdir}/cmake/KF5WidgetsAddons
%{_kf5_archdatadir}/mkspecs/modules/qt_KWidgetsAddons.pri


%changelog
* Tue Aug 16 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.25.0-1
- 5.25.0

* Mon Jul 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.24.0-1
- 5.24.0

* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Mon Jan 18 2016 x - 5.16.0-6
- Edit date by lineedit.

* Fri Jan 15 2016 <ming.wang@i-soft.com.cn> - 5.16.0-5
- Amend: Set KDatePicker disedit from lineedit.

* Fri Jan 15 2016 <ming.wang@i-soft.com.cn> - 5.16.0-4
- Set KDatePicker disedit from lineedit.

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Backport from 5.17

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
