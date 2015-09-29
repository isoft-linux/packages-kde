#NOTE, this is not the original release of kscreen.
#It's isoft forked version with OSD support.

Name:           kscreen
Epoch:          1
Version:        5.4.0
Release:        3%{?dist}
Summary:        KDE Display Management software

License:        GPLv2 or GPLv3
URL:            https://projects.kde.org/projects/playground/base/kscreen

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

#Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

#git@git.isoft.zhcn.cc:zhaixiang/kscreen.git
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  libkscreen-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel

Requires:       kf5-filesystem
Requires:       qt5-qtgraphicaleffects

%description
KCM and KDED modules for managing displays in KDE.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-kde --with-qt --all-name


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files -f %{name}.lang
%doc COPYING
%{_bindir}/kscreen-console
%{_bindir}/kscreen-osd
%{_kf5_qtplugindir}/kcm_kscreen.so
%{_kf5_qtplugindir}/kded_kscreen.so
%{_datadir}/kcm_kscreen/
%{_kf5_datadir}/kservices5/kcm_kscreen.desktop
%{_kf5_datadir}/kservices5/kded/kscreen.desktop
%{_datadir}/icons/hicolor/*/actions/*


%changelog
* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Fri Aug 07 2015 Cjacker <cjacker@foxmail.com>
- taken codes from Leslie Zhai.
- Kscreen-OSD should works.
