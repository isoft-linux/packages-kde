#kdelibs also need HUPNP optional
Summary:    The KDE libraries provide a powerful framework to make writing applications easier
Name: kdelibs 
Version: 4.14.14
Release: 2
License: GPL
Source0: %{name}-%{version}.tar.xz
Source1: macros.kdelibs4


# fix http://bugs.kde.org/149705
Patch2: kdelibs-4.10.0-kde149705.patch

# install all .css files and Doxyfile.global in kdelibs-common to build
# kdepimlibs-apidocs against
Patch8: kdelibs-4.3.90-install_all_css.patch

# patch KStandardDirs to use %{_libexecdir}/kde4 instead of %{_libdir}/kde4/libexec
Patch14: kdelibs-4.11.3-libexecdir.patch

# kstandarddirs changes: search /etc/kde, find %{_kde4_libexecdir}
Patch18: kdelibs-4.11.97-kstandarddirs.patch

# set build type
Patch20: kdelibs-4.10.0-cmake.patch

# die rpath die, since we're using standard paths, we can avoid
# this extra hassle (even though cmake is *supposed* to not add standard
# paths (like /usr/lib64) already! With this, we can drop
# -DCMAKE_SKIP_RPATH:BOOL=ON (finally)
Patch27: kdelibs-4.10.0-no_rpath.patch

## upstreamable
# knewstuff2 variant of:
# https://git.reviewboard.kde.org/r/102439/
Patch50: kdelibs-4.7.0-knewstuff2_gpg2.patch

# fix hunspell/myspell dict paths
Patch51: kdelibs-4.14.9-myspell_paths.patch

# add s390/s390x support in kjs
Patch53: kdelibs-4.7.2-kjs-s390.patch

# return valid locale (RFC 1766)
Patch54: kdelibs-4.8.4-kjs-locale.patch

# borrow from  opensuse
# https://build-test.opensuse.org/package/view_file/home:coolo:test/kdelibs4/0001-Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch
#Patch55: Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES.patch

# candidate fix for: kde deamon crash on wakeup
# https://bugs.kde.org/show_bug.cgi?id=288410
Patch56: kdelibs-kdebug288410.patch

# make filter working, TODO: upstream?  -- rex
Patch59: kdelibs-4.9.3-kcm_ssl.patch

# disable dot to reduce apidoc size
Patch61: kdelibs-4.12.90-dot.patch

# workaround for bz#969524 on arm
Patch62: kdelibs-4.11.3-arm.patch


# set QT_NO_GLIB in klauncher_main.cpp as a possible fix/workaround for #983110
Patch63: kdelibs-4.11.3-klauncher-no-glib.patch

# opening a terminal in Konqueror / Dolphin does not inherit environment variables
Patch64: kdelibs-4.13.2-invokeTerminal.patch

## upstream
# 4.14 branch

# revert these commits for
#https://bugs.kde.org/315578
# for now, causes regression,
#https://bugs.kde.org/317138
Patch090: return-not-break.-copy-paste-error.patch
Patch091: coding-style-fixes.patch
Patch092: return-application-icons-properly.patch

# revert disabling of packagekit
Patch093: turn-the-packagekit-support-feature-off-by-default.patch

# plasma5 places syncing problems
Patch094: 0015-Remove-bookmarks-syncing-from-KFilePlacesModel-and-u.patch

 
Requires: qt4
Requires: attica
Requires: dbusmenu-qt
Requires: systemd-libs
Requires: libxml2
Requires: libxslt
Requires: libpng
Requires: pcre

Requires: udisks2
Requires: upower
Requires: polkit-qt
Requires: phonon
Requires: oxygen-icon-theme

BuildRequires: cmake gettext
BuildRequires: kde-filesystem

BuildRequires: qt4-devel
BuildRequires: attica-devel
BuildRequires: automoc4
BuildRequires: dbusmenu-qt-devel
BuildRequires: systemd-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libpng-devel
BuildRequires: pcre-devel
BuildRequires: polkit-qt-devel
BuildRequires: phonon-devel
BuildRequires: strigi-devel
BuildRequires: aspell-devel
BuildRequires: bzip2-devel
BuildRequires: enchant-devel
BuildRequires: giflib-devel
BuildRequires: ilmbase-devel
BuildRequires: jasper-devel
BuildRequires: krb5-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libICE-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXft-devel
BuildRequires: libXpm-devel
BuildRequires: libXrender-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXtst-devel
BuildRequires: OpenEXR-devel
BuildRequires: qca-devel
BuildRequires: qt4-devel
BuildRequires: strigi-devel
BuildRequires: systemd-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel

Provides:   kdelibs4 = %{version}-%{release}

#kdelibs had no configure option to disable gamin
#we use BuildConflicts to disbale gamin support 
BuildConflicts: gamin-devel

%description
The KDE libraries build on the Qt framework to provide a powerful framework to make writing applications easier, and provide consistency across the KDE desktop environment.

Among other things, the KDE libraries provide:

    standard user interface elements, on top of those provided by Qt (KDEUI)
    a standard configuration format and method of reading and writing configuration data (KConfig)
    site-independent access to standard directories, for finding resources such as icons (KStandardDirs)
    network transparent input and output (KIO)
    a method of embedding application components in other applications (KParts)
    straightforward multimedia and hardware interaction (Phonon and Solid)
    fully-fledged JavaScript and HTML engines (KJS and KHTML)
    an application scripting framework (Kross)
    semantic information and tagging (Nepomuk)


%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: qt4-devel
Requires: attica-devel
Requires: automoc4
Requires: dbusmenu-qt-devel
Requires: systemd-devel
Requires: libxml2-devel
Requires: libxslt-devel
Requires: libpng-devel
Requires: pcre-devel
Requires: polkit-qt-devel
Requires: phonon-devel

Provides:   kdelibs4-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%patch2 -p1 -b .kde149705
%patch8 -p1 -b .install_all_css
%patch14 -p1 -b .libexecdir
%patch18 -p1 -b .kstandarddirs
%patch20 -p1 -b .xxcmake

%patch27 -p1 -b .no_rpath

# upstreamable patches
%patch50 -p1 -b .knewstuff2_gpg2
%patch51 -p1 -b .myspell_paths
%patch53 -p1 -b .kjs-s390
%patch54 -p1 -b .kjs-locale
#%patch55 -p1 -b .Drop-Nepomuk-from-KParts-LINK_INTERFACE_LIBRARIES
%patch56 -p1 -b .kdebug288410
%patch59 -p1 -b .filter
%patch61 -p1 -b .dot
%patch62 -p1 -b .arm-plasma
#%patch63 -p1 -b .klauncher-no-glib
%patch64 -p1 -b .invokeTerminal

%patch090 -p1 -R -b .return-not-break.-copy-paste-error
%patch091 -p1 -R -b .coding-style-fixes.patch
%patch092 -p1 -R -b .return-application-icons-properly


%build
mkdir build

pushd build
%{cmake_kde4} \
  -DKAUTH_BACKEND:STRING="PolkitQt-1" \
  -DKIO_NO_SOPRANO:BOOL=ON \
  -DWITH_SOLID_UDISKS2:BOOL=ON \
  ..
popd

make %{_smp_mflags} -C build

%install

mkdir -p $RPM_BUILD_ROOT
make install/fast DESTDIR=$RPM_BUILD_ROOT -C build


# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.kdelibs4
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  -e "s|@@KDE_APPLICATIONS_VERSION@@|%{apps_version}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.kdelibs4


%clean
rm -rf %{buildroot}

%post
%postun

%files
%defattr(-,root,root)
%{_sysconfdir}/dbus-1/system.d/*
%{_sysconfdir}/xdg/menus/*
%{_bindir}/*
%dir %{_libdir}/kde4
%{_libdir}/kde4/*
%{_libdir}/*.so.*
%{_libdir}/libkdeinit4_*.so

%{_libexecdir}/kde4

%dir %{_datadir}/applications/kde4
%{_datadir}/applications/kde4/*
%{_datadir}/kde4/apps/*
%{_datadir}/config/*
%{_datadir}/dbus-1/interfaces/*
%dir %{_docdir}/HTML
%{_docdir}/HTML/*
%{_datadir}/icons/hicolor/*/actions/*

%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%{_datadir}/kde4/services/*
%dir %{_datadir}/kde4/servicetypes
%{_datadir}/kde4/servicetypes/*
%{_datadir}/locale/*
%{_mandir}/*/*
%{_datadir}/mime/packages/*

%exclude %{_datadir}/kde4/apps/cmake
%exclude %{_datadir}/kde4/apps/ksgmltools2

%exclude %{_bindir}/kde4-config
#%exclude %{_bindir}/nepomuk-rcgen
%exclude %{_bindir}/checkXML

%exclude %{_mandir}/man1/kde4-config*
%exclude %{_mandir}/man1/checkXML*

%files devel
%defattr(-,root,root)
%{_bindir}/checkXML
%{_bindir}/kde4-config
#%{_bindir}/nepomuk-rcgen

%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/cmake/*
%{_datadir}/kde4/apps/cmake
%{_datadir}/kde4/apps/ksgmltools2

%{_mandir}/man1/kde4-config*
%{_mandir}/man1/checkXML*
%exclude %{_libdir}/libkdeinit4_*.so


%changelog
* Wed Nov 11 2015 Cjacker <cjacker@foxmail.com> - 4.14.14-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 4.14.12-3
- Rebuild for new 4.0 release

* Sat Dec 21 2013 Cjacker <cjacker@gmail.com>
- fix some systemtray tooltip wrong position when no active window opened.
- https://bugs.kde.org/show_bug.cgi?id=317783
- add some patches from other dists.

