Name:    dolphin-plugins
Summary: Dolphin plugins for revision control systems
Version: 16.04.2
Release: 1%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdesdk/dolphin-plugins
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel

BuildRequires: dolphin-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ktexteditor-devel
BuildRequires: kf5-kunitconversion-devel
BuildRequires: qt5-qtbase-devel


Requires:       dolphin >= %{version}

%description
Plugins for the Dolphin file manager integrating the following revision control
systems:
* Dropbox
* Git
* Subversion (SVN)
* Bazaar (Bzr)
* Mercurial (Hg)

%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_kf5_qtplugindir}/fileviewdropboxplugin.so
%{_kf5_qtplugindir}/fileviewgitplugin.so
%{_kf5_qtplugindir}/fileviewsvnplugin.so
%{_kf5_qtplugindir}/fileviewbazaarplugin.so
%{_kf5_qtplugindir}/fileviewhgplugin.so

%{_kf5_datadir}/kservices5/fileviewdropboxplugin.desktop
%{_kf5_datadir}/kservices5/fileviewgitplugin.desktop
%{_kf5_datadir}/kservices5/fileviewsvnplugin.desktop
%{_kf5_datadir}/kservices5/fileviewbazaarplugin.desktop
%{_kf5_datadir}/kservices5/fileviewhgplugin.desktop
%{_kf5_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_kf5_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kf5_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg


%changelog
* Tue Jun 28 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 16.04.2-1
- 16.04.2

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

