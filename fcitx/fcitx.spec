#gtk2/3 im module requires glib version >= build time version.
#so we had added a requirement to gtk2/3 immodule.

%global build_time_glib_version %(pkg-config --modversion glib-2.0)
 
%define nam             fcitx 
%define ver             4.2.9
%define rel             2 


%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx.conf


Summary:        FCITX input framework
Name:           %{nam}
Version:        %{ver}
Release:        %{rel}.2
License:        GPL

Source0:        %{name}-%{version}_dict.tar.xz
Source10:       xinput-fcitx

Patch0:         fcitx-tweak.patch

BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  opencc-devel
BuildRequires:  qt4-devel
BuildRequires:  cmake
Obsoletes:      scim

%description
Fcitx is an input method framework with extension support. Currently it
supports Linux and Unix systems like FreeBSD.

Fcitx tries to provide a native feeling under all desktop as well as a light
weight core. You can easily customize it to fit your requirements.


%package gtk2-im-module 
Summary:        Gtk2 im module of fcitx
Requires:       %{name} = %{version}
Requires:	glib2 
#>= %{build_time_glib_version}
Requires(pre):       gtk2

%description gtk2-im-module
Gtk2 im module of fcitx

%package gtk3-im-module
Summary:        Gtk3 im module of fcitx
Requires:       %{name} = %{version}
#Requires:	glib2 >= %{build_time_glib_version}
Requires:	glib2
Requires(pre):       gtk3
%description gtk3-im-module
Gtk3 im module of fcitx

%package qt-im-module
Summary:        qt4 im module of fcitx
Requires:       %{name} = %{version}
Requires:       qt4
%description qt-im-module
qt4 im module of fcitx


%package devel
Summary:        Development libraries for FCITX
Requires:       %{name} = %{version}

%description devel
The fcitx-devel package includes the static libraries and header files
for the fcitx package.

%prep
%setup -n %{name}-%{version}
%patch0 -p1

%build
mkdir build
pushd build
cmake .. \
    -DSYSCONFDIR=%{_sysconfdir} \
    -DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DLIB_INSTALL_DIR=%{_prefix}/%{_lib} \
    -DENABLE_PANGO=on \
    -DENABLE_TABLE=on \
    -DENABLE_GTK2_IM_MODULE=on \
    -DENABLE_GTK3_IM_MODULE=on \
    -DENABLE_QT_IM_MODULE=on \
    -DENABLE_QT=on \
    -DENABLE_QT_GUI=on \
    -DENALE_OPENCC=on \
    -DENABLE_DBUS=on \
    -DENABLE_PANGO=on \
    -DENABLE_XDGAUTOSTART=off

make %{?_smp_mflags}
popd

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
pushd build
make DESTDIR=${RPM_BUILD_ROOT} install
popd

#revert default skin
pushd $RPM_BUILD_ROOT/usr/share/fcitx/skin
rm -rf dark
cp default/keyboard.png classic/
rm -rf default
mv classic default
popd

#install xinput config file
install -pm 644 -D %{SOURCE10} %{buildroot}%{_xinputconf}

rm -rf $RPM_BUILD_ROOT/usr/share/applications

#######################
#######################
%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig ||:
update-mime-database %{_datadir}/mime
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 80 || :


%postun
/sbin/ldconfig ||:
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
update-mime-database %{_datadir}/mime

%post gtk2-im-module
gtk-query-immodules-2.0 >%{_libdir}/gtk-2.0/2.10.0/immodules.cache

%postun gtk2-im-module
gtk-query-immodules-2.0 >%{_libdir}/gtk-2.0/2.10.0/immodules.cache

%post gtk3-im-module
gtk-query-immodules-3.0 >%{_libdir}/gtk-3.0/3.0.0/immodules.cache

%postun gtk3-im-module
gtk-query-immodules-3.0 >%{_libdir}/gtk-3.0/3.0.0/immodules.cache


%files
%defattr(-, root, root)
%config %{_xinputconf}
%{_bindir}/*
%{_mandir}/*
#%{_sysconfdir}/xdg/autostart/*
%{_datadir}/icons/*
%{_datadir}/locale/*
#%{_datadir}/applications/*
%{_datadir}/fcitx/*
%{_libdir}/fcitx/*
%{_libdir}/*so.*
%{_docdir}/*
%{_datadir}/mime/packages/x-fskin.xml
%{_libdir}/girepository-?.?/*
%{_datadir}/dbus-1/services/org.fcitx.Fcitx.service

%files gtk2-im-module 
%defattr(-, root, root)
%{_libdir}/gtk-2*/*

%files gtk3-im-module
%defattr(-, root, root)
%{_libdir}/gtk-3*/*

%files qt-im-module
%defattr(-, root, root)
%{_libdir}/qt*/plugins/inputmethods/*so

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/cmake/*
%{_datadir}/gir-?.?/*

%changelog
* Fri Dec 16 2016 sulit - 4.2.9-2.2
- rebuild fcitx

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 4.2.9-2.1
- Rebuild for new 4.0 release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

