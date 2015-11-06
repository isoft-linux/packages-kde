Name:           kinfocenter
Version:        5.4.2
Release:        6
Summary:        KDE Info Center

License:        GPLv2+ and LGPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/kinfocenter

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# about-distro isoft-logo
Patch1: 0001-about-distro-isoft-logo.patch


BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kpackage-devel

BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libX11-devel
BuildRequires:  pciutils-devel
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif

BuildRequires:  kf5-kwayland-devel

Requires:       kf5-filesystem

# When kinfocenter was split out from kde-workspace
Conflicts:      kde-workspace < 4.11.15-3

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 .isoft-logo


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kinfocenter5 --all-name


%files -f kinfocenter5.lang
%doc COPYING COPYING.DOC
%{_bindir}/kinfocenter
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/kcms/*.so
%ifnarch s390 s390x
%{_datadir}/kcmview1394/
%endif
%{_datadir}/kcmusb/
%{_sysconfdir}/xdg/menus/kinfocenter.menu
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_kf5_datadir}/kxmlgui5/kinfocenter/
%{_kf5_datadir}/kpackage/kcms/kcm_energyinfo/
%lang(ca) %{_datadir}/doc/HTML/ca/kinfocenter/
%lang(de) %{_datadir}/doc/HTML/de/kinfocenter/
%lang(en) %{_datadir}/doc/HTML/en/kinfocenter/
%lang(it) %{_datadir}/doc/HTML/it/kinfocenter/
%lang(nl) %{_datadir}/doc/HTML/nl/kinfocenter/
%lang(pt_BR) %{_datadir}/doc/HTML/pt_BR/kinfocenter/
%lang(sv) %{_datadir}/doc/HTML/sv/kinfocenter/
%lang(uk) %{_datadir}/doc/HTML/uk/kinfocenter/


%changelog
* Fri Nov 06 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add start-here-isoft 
- Change start-here-isoft to isoft-logo.

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

