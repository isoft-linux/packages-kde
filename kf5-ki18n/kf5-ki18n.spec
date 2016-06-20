%global framework ki18n

Name:           kf5-%{framework}
Version:        5.23.0
Release:        1%{?dist}
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

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gettext
BuildRequires:  perl
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtdeclarative-devel

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

mkdir -p %{buildroot}%{_datadir}/locale/zh_CN/LC_SCRIPTS/ki18n5/
mkdir -p %{buildroot}%{_datadir}/locale/zh_TW/LC_SCRIPTS/ki18n5/
mkdir -p %{buildroot}%{_datadir}/locale/ja/LC_SCRIPTS/ki18n5/

#remove below languages, they will be used to detect installed translations.
#also they will affect nls settings in systemsettings.
#by cjacker.
pushd %{buildroot}%{_kf5_datadir}/locale
mkdir -p ../locale.bak
mv zh* ../locale.bak
mv ja* ../locale.bak
mv ko* ../locale.bak
rm -rf *
mv ../locale.bak/* .
rm -rf ../locale.bak
popd
 
%find_lang ki18n5_qt --with-qt --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f ki18n5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_qtplugindir}/kf5/ktranscript.so
#%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n5/
#%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n5/
#%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n5/
#%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n5/
#%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/
#%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/
#%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n5/
#%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n5/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n5/
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_SCRIPTS/ki18n5/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n5/
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_SCRIPTS/ki18n5/

%files devel
%{_kf5_includedir}/ki18n_version.h
%{_kf5_includedir}/KI18n/
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_libdir}/cmake/KF5I18n/
%{_kf5_archdatadir}/mkspecs/modules/qt_KI18n.pri


%changelog
* Mon Jun 20 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.23.0-1
- 5.23.0

* Wed Apr 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.21.0-1
- 5.21.0

* Thu Apr 07 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-3
- Backport from 5.17.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-5
- Rebuild for new 4.0 release

* Fri Oct 16 2015 Cjacker <cjacker@foxmail.com>
- fix zh_CN/zh_TW/ja ki18n5.js issue.

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
