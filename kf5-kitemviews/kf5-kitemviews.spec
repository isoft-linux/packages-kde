%global framework kitemviews

Name:           kf5-%{framework}
Version:        5.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with item views

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

BuildRequires:  kf5-rpm-macros >= %{version}
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 1 addon with item views.


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
%find_lang kitemviews5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kitemviews5_qt.lang
%doc COPYING COPYING.LIB README.md
%{_kf5_libdir}/libKF5ItemViews.so.*

%files devel
%doc
%{_kf5_includedir}/kitemviews_version.h
%{_kf5_includedir}/KItemViews
%{_kf5_libdir}/libKF5ItemViews.so
%{_kf5_libdir}/cmake/KF5ItemViews
%{_kf5_archdatadir}/mkspecs/modules/qt_KItemViews.pri


%changelog
* Tue Jan 17 2017 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.30.0-1
- 5.30.0-1

* Tue Dec 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Tue Nov 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-2
- 5.28.0-2

* Mon Nov 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Mon Oct 31 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.27.0-1
- 5.27.0

* Tue Sep 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.26.0-1
- 5.26.0

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

* Fri Jan 15 2016 <ming.wang@i-soft.com.cn> - 5.16.0-4
- Amend: Modify KTreWwidgetSearchLine.

* Fri Jan 15 2016 <ming.wang@i-soft.com.cn> - 5.16.0-3
- Modify KTreWwidgetSearchLine.

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
