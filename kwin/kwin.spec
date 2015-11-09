%global         wayland 1

Name:           kwin
Version:        5.4.3
Release:        2
Summary:        KDE Window manager

# all sources are effectively GPLv2+, except for:
# scripts/enforcedeco/contents/code/main.js
# KDE e.V. may determine that future GPL versions are accepted
License:        GPLv2 or GPLv3
URL:            https://projects.kde.org/projects/kde/workspace/kwin

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# Base
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros


# Qt
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

# X11/OpenGL
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXcursor-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  libepoxy-devel

# Wayland (optional)
%if 0%{?wayland}
BuildRequires:  kf5-kwayland-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  libwayland-cursor-devel
BuildRequires:  mesa-libwayland-egl-devel
BuildRequires:  libxkbcommon-devel >= 0.4
BuildRequires:  pkgconfig(libinput) >= 0.10
BuildRequires:  pkgconfig(libudev)
%endif

# KF5
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kinit-devel >= 5.10.0-3
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kiconthemes-devel

BuildRequires:  kdecoration-devel

## Runtime deps
Requires:       kf5-filesystem
# Runtime-only dependency for effect video playback
Requires:       qt5-qtmultimedia
# libkdeinit5_kwin*
%{?kf5_kinit_requires}

# Before kwin was split out from kde-workspace into a subpackage
Conflicts:      kde-workspace%{?_isa} < 4.11.14-2

Provides: firstboot(windowmanager) = kwin_x11
Provides: firstboot(windowmanager) = kwin

%description
%{summary}.

%if 0%{?wayland}
%package        wayland
Summary:        KDE Window Manager with experimental Wayland support
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# libkdeinit5_kwin*
%{?kf5_kinit_requires}
%description    wayland
%{summary}.
%endif

%package        libs
Summary:        KWin runtime libraries
# Before kwin-libs was split out from kde-workspace into a subpackage
Conflicts:      kde-workspace-libs%{?_isa} < 4.11.14-2
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kservice-devel
Requires:       kf5-kwindowsystem-devel
Conflicts:      kde-workspace-devel < 5.0.0-1
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        User manual for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kwin5 --with-qt --with-kde --all-name

# temporary(?) hack to allow initial-setup to use /usr/bin/kwin too
ln -s kwin_x11 %{buildroot}%{_bindir}/kwin


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f kwin5.lang
%{_sysconfdir}/xdg/org_kde_kwin.categories
%{_bindir}/kwin
%{_bindir}/kwin_x11
%{_kf5_libdir}/libkdeinit5_kwin_x11.so
%{_kf5_libdir}/libkdeinit5_kwin_rules_dialog.so
%{_datadir}/kwin
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/kwin
%{_kf5_qtplugindir}/org.kde.kdecoration2/*.so
%{_kf5_qtplugindir}/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
%{_qt5_prefix}/qml/org/kde/kwin
%{_kf5_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin_rules_dialog
%{_datadir}/kwincompositing
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/kwin
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/knotifications5/kwin.notifyrc
%{_kf5_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/icons/hicolor/*/apps/kwin.*
# note: these are for reference (to express config defaults), they are
# not config files themselves (so don't use %%config tag)
%{_sysconfdir}/xdg/*.knsrc

%if 0%{?wayland}
%files wayland
%{_bindir}/kwin_wayland
%{_kf5_qtplugindir}/org.kde.kwin.waylandbackends/KWinWaylandDrmBackend.so
%{_kf5_qtplugindir}/org.kde.kwin.waylandbackends/KWinWaylandFbdevBackend.so
%{_kf5_qtplugindir}/org.kde.kwin.waylandbackends/KWinWaylandWaylandBackend.so
%{_kf5_qtplugindir}/org.kde.kwin.waylandbackends/KWinWaylandX11Backend.so
%endif

%files libs
# these dbus xml files probably ought to be moved to -devel, kde-sig needs agreed policy first -- rex
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/libkwin.so.*
%{_libdir}/libkwinxrenderutils.so.*
%{_libdir}/libkwineffects.so.*
%{_libdir}/libkwinglutils.so.*
%{_libdir}/libkwin4_effect_builtins.so.*

%files devel
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/libkwinxrenderutils.so
%{_libdir}/libkwineffects.so
%{_libdir}/libkwinglutils.so
%{_libdir}/libkwin4_effect_builtins.so
%{_includedir}/kwin*.h

%files doc
%{_docdir}/HTML/en/kcontrol/


%changelog
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

