%global kf5_version 5.29.0

Name:           ksysguard
Version:        5.8.5
Release:        1
Summary:        KDE Process Management application

License:        GPLv2
URL:            https://projects.kde.org/projects/kde/workspace/ksysguard

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtwebkit-devel

BuildRequires:  cmake
BuildRequires:  kf5-rpm-macros >= %{kf5_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}

BuildRequires:  kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  kf5-kitemviews-devel >= %{kf5_version}
BuildRequires:  kf5-knewstuff-devel >= %{kf5_version}
BuildRequires:  kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_version}

BuildRequires:  libksysguard-devel >= %{version}

BuildRequires:  lm_sensors-devel
BuildRequires:  desktop-file-utils

Requires:       kf5-filesystem

Requires:       ksysguardd = %{version}-%{release}

%description
%{summary}.

%package -n    ksysguardd
Summary: Performance monitor daemon
%description -n ksysguardd
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang ksysguard5 --with-qt --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.ksysguard.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f ksysguard5.lang
%doc COPYING COPYING.DOC README
%{_bindir}/ksysguard
%{_kf5_libdir}/libkdeinit5_ksysguard.so
%{_datadir}/ksysguard
%config %{_sysconfdir}/xdg/ksysguard.knsrc
%{_datadir}/applications/org.kde.ksysguard.desktop
%{_docdir}/HTML/*/ksysguard
%{_datadir}/icons/hicolor/*/apps/*.png
%{_kf5_datadir}/knotifications5/ksysguard.notifyrc
%{_kf5_datadir}/kxmlgui5/ksysguard

%files -n ksysguardd
%{_bindir}/ksysguardd
%config %{_sysconfdir}/ksysguarddrc


%changelog
* Thu Dec 29 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.5-1
- 5.8.5-1

* Thu Nov 03 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.8.3-1
- 5.8.3

* Thu Aug 25 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.7.4-1
- 5.7.4

* Fri Dec 04 2015 kun.li@i-soft.com.cn - 5.4.3-3
- add change-memory-show.patch  

* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

