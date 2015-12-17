%global kf5 1

Name:    kmix 
Summary: KDE volume control 
Version: 15.12.0
Release: 3

License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdemultimedia/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches
Patch0: 0001-drop-shortcut-setting.patch


BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(alsa)
# FIXME/TODO: kf5 build seems to expects libcanberra cmake support, update? -- rex
BuildRequires: glib2-devel
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(phonon)
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kinit-devel >= 5.10.0-3
BuildRequires: kf5-plasma-devel
BuildRequires: pkgconfig(Qt5Gui)
%{?kf5_kinit_requires}

%description
%{summary}.


%prep
%setup -q
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} -DKMIX_KF5_BUILD:BOOL=ON ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

echo "NoDisplay=true" >>$RPM_BUILD_ROOT%{_datadir}/applications/kmix.desktop
#plasma-5.4 have plasma-pa, drop autostart of kmix.
#rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kmix.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%{_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml
%{_datadir}/icons/hicolor/*/*/kmix.*
%{_kf5_bindir}/kmix
%{_kf5_bindir}/kmixctrl
%{_kf5_bindir}/kmixremote
%{_kf5_datadir}/applications/kmix.desktop
%{_kf5_datadir}/kmix/
%{_kf5_datadir}/kxmlgui5/kmix/kmixui.rc
%{_kf5_libdir}/libkdeinit5_kmix.so
%{_kf5_libdir}/libkdeinit5_kmixctrl.so
%{_qt5_plugindir}/libkded_kmixd.so
%{_sysconfdir}/xdg/autostart/restore_kmix_volumes.desktop
%{_sysconfdir}/xdg/autostart/kmix_autostart.desktop
%{_kf5_datadir}/kservices5/kded/kmixd.desktop
%{_kf5_datadir}/kservices5/kmixctrl_restore.desktop
%{_kf5_qtplugindir}/plasma/dataengine/plasma_engine_mixer.so
%{_kf5_datadir}/kservices5/plasma-dataengine-mixer.desktop
%{_kf5_datadir}/plasma/services/mixer.operations


%changelog
* Thu Dec 17 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Drop shortcut setting, but please use kcmkeys instead.

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-4
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

