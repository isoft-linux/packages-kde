Name:    dolphin-plugins
Summary: Dolphin plugins for revision control systems
Version: 15.08.2
Release: 3%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdesdk/dolphin-plugins
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

#git://anongit.kde.org/dolphin-plugins
#git checkout frameworks
#Source0: %{name}.tar.gz

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

%{_kf5_datadir}/kservices5/fileviewdropboxplugin.desktop
%{_kf5_datadir}/kservices5/fileviewgitplugin.desktop
%{_kf5_datadir}/kservices5/fileviewsvnplugin.desktop
%{_kf5_datadir}/kservices5/fileviewbazaarplugin.desktop
%{_kf5_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kf5_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-3
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

