%define flags 1
%define webkit 0 
%define plasma5 1

Name:    kde-runtime
Summary: KDE Runtime
Version: 15.12.0
Release: 2 

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPLv2+ and GPLv2+
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/kde-runtime-%{version}.tar.xz

# add shortcuts for search provider
Patch1: kdebase-runtime-4.1.x-searchproviders-shortcuts.patch

# support kdesud -Wl,-z,relro,-z,now linker flags
Patch2: kde-runtime-kdesud_relro.patch

# add OnlyShowIn=KDE  to Desktop/Home.desktop (like trash.desktop)
Patch6: kdebase-runtime-4.3.3-home_onlyshowin_kde.patch

# correct path for htsearch
Patch7: kdebase-runtime-4.5.3-htsearch.patch

# Launch compiz via compiz-manager so we get window decorations and
# other such decadent luxuries (AdamW 2011/01)
Patch8: kdebase-runtime-4.5.95-compiz.patch

# add overrides in default manpath
Patch9: kdebase-runtime-4.3.4-man-overrides.patch

# disable making files read only when moving them into trash
# (Upstream wouldn't accept this)
Patch11: kde-runtime-4.10.4-trash-readonly.patch

## upstreamable patches
# make installdbgsymbols.sh use pkexec instead of su 
# increase some timeouts in an effort to see (some) errors before close
Patch50: kde-runtime-4.9.0-installdbgsymbols.patch

# use packagekit to install a possibly-missing gdb
Patch51: kde-runtime-4.11.2-install_gdb.patch

## upstream patches

Patch300: kde-runtime-4.9.2-webkit.patch

Obsoletes: kdebase-runtime < 4.7.97-10
Provides:  kdebase-runtime = %{version}-%{release}
Obsoletes: kdebase4-runtime < %{version}-%{release}
Provides:  kdebase4-runtime = %{version}-%{release}

Obsoletes: nepomukcontroller < 1:0.2

# knotify4 provides dbus service org.freedesktop.Notifications too 
Provides: desktop-notification-daemon

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
# http://bugzilla.redhat.com/794958
Requires: dbus-x11
%ifnarch s390 s390x
Requires: eject
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# not *strictly* required, but didn't want to rely on comps -- rex
Requires: %{name}-drkonqi = %{version}-%{release}
%if 0%{?flags}
Requires: %{name}-flags = %{version}-%{release}
%endif

# ensure default/fallback icon theme present
# beware of bootstrapping, there be dragons
Requires: oxygen-icon-theme 

BuildRequires: cmake
#for kde rpm macros
BuildRequires: kde-filesystem

BuildRequires: bzip2-devel
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: kdelibs-devel >= 4.14.4
# kdepimlibs' kxmlrpcclient used for drkonqi, ok to leave unversioned
BuildRequires: kdepimlibs-devel
BuildRequires: kactivities-devel
BuildRequires: libgcrypt-devel >= 1.5.0
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(polkit-qt-1) 
BuildRequires: pkgconfig(libattica)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libstreamanalyzer) pkgconfig(libstreams)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(NetworkManager)
#BuildRequires: pkgconfig(qca2)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(smbclient)
#BuildRequires: pkgconfig(soprano) >= 2.6.50
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: openslp-devel
BuildRequires: libssh-devel >= 0.6
BuildRequires: xorg-x11-font-utils
BuildRequires: zlib-devel
BuildRequires: docbook-dtds docbook-style-xsl

# some items moved -workspace -> -runtime
Conflicts: kdebase-workspace < 4.5.80
# plasmapkg moved -workspace -> -runtime
Conflicts: kde-workspace < 4.9.60

%description
Core runtime for KDE 4.

%package devel
Summary:  Developer files for %{name}
Obsoletes: kdebase-runtime-devel < 4.7.97-10
Provides:  kdebase-runtime-devel = %{version}-%{release} 
Requires: %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%package drkonqi
Summary: DrKonqi KDE crash handler
Requires: %{name} = %{version}-%{release}
# drkonqi patch50 uses pkexec
Requires: polkit
%description drkonqi
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Obsoletes: kdebase-runtime-libs < 4.7.97-10
Provides:  kdebase-runtime-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%{?kdelibs4_requires}
%description libs
%{summary}.

%package flags
Summary: Geopolitical flags
Obsoletes: kdebase-runtime-flags < 4.7.97-10
Provides:  kdebase-runtime-flags = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description flags
%{summary}.

%package docs
Summary: User documentation and manuals
Obsoletes: %{name} < 4.13.3-3
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description docs
%{summary}.

%package kio-smb
Summary: Samba KIO slave
# upgrade path
Obsoletes: kde-runtime < 4.9.2-5
Requires: %{name} = %{version}-%{release}
%description kio-smb
%{summary}.

%package -n kdesu
Summary: Runs a program with elevated privileges
# upgrade path, when kdesu was introduced
Obsoletes: kde-runtime < 14.12.3-2
# needed for non-conflicting libexec bits
Requires: %{name} = %{version}-%{release}
%description -n kdesu
%{summary}.

%package -n khelpcenter
Summary: KDE Help Center
# upgrade path
Obsoletes: kde-runtime < 4.13.3-3
Requires: %{name} = %{version}-%{release}
%description -n khelpcenter
%{summary}.


%prep
%setup -q -n kde-runtime-%{version}

%patch1 -p1 -b .searchproviders-shortcuts
%patch6 -p1 -b .home_onlyshowin_kde
%patch7 -p1 -b .htsearch
%patch8 -p1 -b .config
%patch9 -p1 -b .man-overrides
%patch11 -p1 -b .trash-readonly
%patch50 -p1 -b .installdgbsymbols
%patch51 -p1 -b .install_gdb

%if ! 0%{?webkit}
%patch300 -p1 -b .webkit
%global no_webkit -DKDERUNTIME_NO_WEBKIT:BOOL=ON -DPLASMA_NO_KDEWEBKIT:BOOL=ON
%endif


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  -DCMAKE_MINIMUM_REQUIRED_VERSION=3.0 \
  %{?no_webkit} \
  .. 
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# fix documentation multilib conflict in index.cache
for f in kioslave/nepomuksearch kcontrol/spellchecking kcontrol/performance \
   kcontrol/kcmnotify kcontrol/kcmcss kcontrol/ebrowsing; do
   bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache.bz2
   sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
done

# kdesu symlink
ln -s %{_kde4_libexecdir}/kdesu %{buildroot}%{_kde4_bindir}/kdesu

# omit hicolor index.theme, use one from hicolor-icon-theme
rm -f %{buildroot}%{_kde4_iconsdir}/hicolor/index.theme

# remove country flags because some people/countries forbid some other
# people/countries' flags :-(
%{!?flags:rm -f %{buildroot}%{_kde4_datadir}/locale/l10n/*/flag.png}

# install this service for KDE 3 applications too
mkdir %{buildroot}%{_datadir}/services
ln -s %{_kde4_datadir}/kde4/services/khelpcenter.desktop \
      %{buildroot}%{_datadir}/services/khelpcenter.desktop

# FIXME: -devel type files, omit for now
rm -vf  %{buildroot}%{_kde4_libdir}/lib{kwalletbackend,molletnetwork}.so

# rpaths
# use chrpath hammer for now, find better patching solutions later -- Rex
chrpath --list   %{buildroot}%{_libdir}/kde4/plugins/phonon_platform/kde.so ||:
chrpath --delete %{buildroot}%{_libdir}/kde4/plugins/phonon_platform/kde.so

%if 0%{?plasma5}
#Hide this menu item.
echo "NoDisplay=true" >> %{buildroot}%{_kde4_datadir}/applications/kde4/knetattach.desktop

rm -rf %{buildroot}%{_kde4_docdir}/HTML/en/kcontrol/
rm -rf %{buildroot}%{_kde4_docdir}/HTML/en/kdebugdialog/
rm -rf %{buildroot}%{_kde4_docdir}/HTML/en/kioslave/
rm -rf %{buildroot}%{_kde4_docdir}/HTML/en/knetattach/

rm -fv  %{buildroot}%{_kde4_bindir}/{kdesu,khelpcenter}
rm -fv  %{buildroot}%{_kde4_libexecdir}/khc_*
rm -fv  %{buildroot}%{_kde4_libdir}/libkdeinit4_khelpcenter.so
rm -frv %{buildroot}%{_kde4_docdir}/HTML/en/{kdesu,khelpcenter,fundamentals,onlinehelp}
rm -frv %{buildroot}%{_kde4_appsdir}/khelpcenter/
rm -fv  %{buildroot}%{_kde4_datadir}/services/khelpcenter.desktop
rm -fv  %{buildroot}%{_kde4_datadir}/config.kcfg/khelpcenter.kcfg
rm -fv  %{buildroot}%{_mandir}/man1/kdesu.1*
%endif


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
    update-desktop-database -q &> /dev/null ||:
    touch --no-create %{_datadir}/mime/packages &> /dev/null || :
    update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%files
%{_kde4_bindir}/kcmshell4
%{_kde4_bindir}/kde-cp
%{_kde4_bindir}/kde-mv
%{_kde4_bindir}/kde-open
%{_kde4_bindir}/kde4
%{_kde4_bindir}/kde4-menu
%{_kde4_bindir}/kdebugdialog
%{_kde4_bindir}/keditfiletype
%{_kde4_bindir}/kfile4
%{_kde4_bindir}/kglobalaccel
%{_kde4_bindir}/khotnewstuff-upload
%{_kde4_bindir}/khotnewstuff4
%{_kde4_bindir}/kiconfinder
%{_kde4_bindir}/kioclient
%{_kde4_bindir}/kmimetypefinder
%{_kde4_bindir}/knotify4
%{_kde4_bindir}/kquitapp
%{_kde4_bindir}/kreadconfig
%{_kde4_bindir}/kstart
%{_kde4_bindir}/ksvgtopng
%{_kde4_bindir}/ktraderclient
%{_kde4_bindir}/ktrash
%{_kde4_bindir}/kuiserver
%{_kde4_bindir}/kwalletd
%{_kde4_bindir}/kwriteconfig
%{_kde4_bindir}/plasma-remote-helper
%{_kde4_bindir}/plasmapkg
%{_mandir}/man1/plasmapkg.1*
%{_kde4_bindir}/solid-hardware
%{_kde4_appsdir}/desktoptheme/
%{_kde4_appsdir}/hardwarenotifications/
%{_kde4_appsdir}/kcm_componentchooser/
%{_kde4_appsdir}/kcmlocale/
%{_kde4_appsdir}/kcm_phonon/
%{_kde4_appsdir}/kconf_update/*
%{_kde4_appsdir}/kde/
%{_kde4_appsdir}/kglobalaccel/
%{_kde4_appsdir}/kio_bookmarks/
%{_kde4_appsdir}/kio_desktop/
%{_kde4_appsdir}/kio_docfilter/
%{_kde4_appsdir}/kio_finger/
%{_kde4_appsdir}/kio_info/
%{_kde4_appsdir}/konqsidebartng/
%{_kde4_appsdir}/ksmserver/
%{_kde4_appsdir}/kwalletd/
%{_kde4_appsdir}/libphonon/
%{_kde4_appsdir}/phonon/
%dir %{_kde4_appsdir}/remoteview/
%{_kde4_appsdir}/remoteview/network.desktop
%{_kde4_configdir}/*.knsrc
%{_kde4_datadir}/config.kcfg/jpegcreatorsettings.kcfg
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_kde4_datadir}/kde4/services/*.desktop
%exclude %{_kde4_datadir}/kde4/services/khelpcenter.desktop
%{_kde4_datadir}/kde4/services/qimageioplugins/webp.desktop
%{_kde4_datadir}/kde4/services/*.protocol
%{_kde4_datadir}/kde4/services/kded/
%{_kde4_datadir}/kde4/services/searchproviders/
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_datadir}/mime/packages/network.xml
%{_kde4_datadir}/mime/packages/webp.xml
%{_kde4_datadir}/sounds/*
%{_kde4_iconsdir}/default.kde4
%{_kde4_libdir}/kconf_update_bin/*
%{_kde4_libdir}/libkdeinit4_kcmshell4.so
%{_kde4_libdir}/libkdeinit4_kglobalaccel.so
%{_kde4_libdir}/libkdeinit4_kuiserver.so
%{_kde4_libdir}/libkdeinit4_kwalletd.so
%{_kde4_libdir}/kde4/platformimports/
%{_kde4_libdir}/kde4/kcm_*.so
%{_kde4_libdir}/kde4/kded_*.so
%{_kde4_libexecdir}/kcmremotewidgetshelper
%{_kde4_libexecdir}/kdeeject
%{_kde4_libexecdir}/kdesu
%attr(2755,root,nobody) %{_kde4_libexecdir}/kdesud
%{_kde4_libexecdir}/kdontchangethehostname
%{_kde4_libexecdir}/kioexec
%{_kde4_libexecdir}/knetattach
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_sysconfdir}/xdg/menus/kde-information.menu
%{_kde4_datadir}/applications/kde4/Help.desktop
%{_kde4_datadir}/applications/kde4/knetattach.desktop
%{_kde4_configdir}/kshorturifilterrc
%{_kde4_datadir}/desktop-directories/*.directory
%exclude %{_kde4_datadir}/desktop-directories/kde-information.directory
%{_kde4_datadir}/emoticons/kde4/
%{_kde4_datadir}/locale/l10n/
%{_kde4_datadir}/locale/currency/
%{?flags:%exclude %{_kde4_datadir}/locale/l10n/*/flag.png}
%{_polkit_qt_policydir}/*.policy
%{_sysconfdir}/dbus-1/system.d/*
#exclude %{_kde4_datadir}/kde4/services/smb.protocol

#files kio-smb
%dir %{_kde4_appsdir}/konqueror/dirtree/
%dir %{_kde4_appsdir}/konqueror/dirtree/remote/
%{_kde4_appsdir}/konqueror/dirtree/remote/smb-network.desktop
%dir %{_kde4_appsdir}/remoteview/
%{_kde4_appsdir}/remoteview/smb-network.desktop
%{_kde4_datadir}/kde4/services/smb.protocol
# dup'd in -libs glob
#{_kde4_libdir}/kde4/kio_smb.so

%files devel
%{_kde4_includedir}/*
%{_kde4_appsdir}/cmake/modules/*.cmake

%files drkonqi
%{_kde4_libexecdir}/drkonqi
#%{_kde4_libexecdir}/installdbgsymbols.sh
%{_kde4_appsdir}/drkonqi/

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
# unversioned plugin:
%{_kde4_libdir}/attica_kde.so
%{_kde4_libdir}/libknotifyplugin.so
%{_kde4_libdir}/libkwalletbackend.so.*
%{_kde4_libdir}/libmolletnetwork.so.*
%{_kde4_libdir}/kde4/*.so
%{_kde4_libdir}/kde4/imports/
# FIXME: Is this a good idea? Won't multilib apps need KCMs, too?
%exclude %{_kde4_libdir}/kde4/kcm_*.so
%exclude %{_kde4_libdir}/kde4/kded_*.so
%{_kde4_libdir}/kde4/plugins/phonon_platform/
%{_kde4_libdir}/kde4/plugins/imageformats/kimg_webp.so

%if 0%{?flags}
%files flags
%{_kde4_datadir}/locale/l10n/*/flag.png
%endif


%if ! 0%{?plasma5}

%files docs
%{_kde4_docdir}/HTML/en/kcontrol/
%{_kde4_docdir}/HTML/en/kdebugdialog/
%{_kde4_docdir}/HTML/en/kioslave/
%{_kde4_docdir}/HTML/en/knetattach/

%files -n khelpcenter
%{_kde4_bindir}/khelpcenter
%{_kde4_libexecdir}/khc_*
%{_kde4_libdir}/libkdeinit4_khelpcenter.so
%{_kde4_docdir}/HTML/en/khelpcenter/
%{_kde4_docdir}/HTML/en/fundamentals/
%{_kde4_docdir}/HTML/en/onlinehelp/
%{_kde4_appsdir}/khelpcenter/
%{_kde4_datadir}/kde4/services/khelpcenter.desktop
%{_kde4_datadir}/services/khelpcenter.desktop
%{_kde4_datadir}/config.kcfg/khelpcenter.kcfg
%{_kde4_datadir}/desktop-directories/kde-information.directory

%files -n kdesu
%{_kde4_bindir}/kdesu
%{_kde4_docdir}/HTML/en/kdesu/
%{_mandir}/man1/kdesu.1*
## include non-conflicting libexec bits here too ? -- rex
%endif


%changelog
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

* Wed Sep 16 2015 Cjacker <cjacker@foxmail.com>
- update to 15.08.1
- add -DCMAKE_MINIMUM_REQUIRED_VERSION=3.0 to fix build with cmake-3.x
