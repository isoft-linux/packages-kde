Name:    kpat
Summary: A selection of solitaire card games
Version: 15.12.0
Release: 3%{?dist}

License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdegames/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0: kpat-tune-desktop.patch
Patch1: kpat-fix-zh-i18n.patch 

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
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(Qt5Widgets) pkgconfig(Qt5Qml) pkgconfig(Qt5Quick) pkgconfig(Qt5QuickWidgets) pkgconfig(Qt5Svg) pkgconfig(Qt5Test)

#BuildRequires: libappstream-glib
BuildRequires: libkdegames-devel >= %{version}

%description
%{summary}.
To play patience you need, as the name suggests, patience. For simple
games, where the way the game goes depends only upon how the cards fall,
your patience might be the only thing you need.  There are also patience
games where you must plan your strategy and think ahead in order to win.
A theme common to all the games is the player must put the cards in a
special order — moving, turning and reordering them.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# fix icon mis-naming
mv -f icons/hi64-apps-kpats.png icons/hi64-apps-kpat.png ||:
sed -i -e "s|hi64-apps-kpats.png|hi64-apps-kpat.png|" icons/CMakeLists.txt


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
#appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/appdata/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop ||:


%post
/sbin/ldconfig
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
/sbin/ldconfig
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-mime-database  %{_datadir}/mime &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
update-mime-database  %{_datadir}/mime &> /dev/null || :


%files
%doc COPYING*
#doc README
%{_kf5_bindir}/%{name}
%{_sysconfdir}/xdg/kcardtheme.knsrc
%{_sysconfdir}/xdg/%{name}.knsrc
%{_kf5_datadir}/applications/org.kde.%{name}.desktop
#{_kf5_datadir}/appdata/org.kde.%{name}.appdata.xml
%{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf5_datadir}/%{name}/
%{_kf5_docdir}/HTML/en/%{name}/
#{_kf5_datadir}/kconf_update/%{name}*
%{_kf5_datadir}/kxmlgui5/%{name}/
#{_kf5_datadir}/sounds/%{name}/
%{_kf5_datadir}/config.kcfg/%{name}.kcfg
%{_kf5_libdir}/libkcardgame.so
%{_datadir}/mime/packages/kpatience.xml


%changelog
* Fri Jan 08 2016 kun.li@i-soft.com.cn - 15.12.0-3
- add kpat-fix-zh-i18n.patch 

* Thu Dec 17 2015 Cjacker <cjacker@foxmail.com> - 15.12.0-2
- Update

* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 15.11.80-2
- Update

* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.08.2-4
- Rebuild for new 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- tune desktop file.

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.2

