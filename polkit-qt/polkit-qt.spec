
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global qt5 1

Name:            polkit-qt
Version:         0.112.0
Release:         7%{?dist}
Summary:         Qt bindings for PolicyKit

License:         GPLv2+
URL:             https://projects.kde.org/projects/kdesupport/polkit-qt-1 
Source0:         http://download.kde.org/stable/apps/KDE4.x/admin/polkit-qt-1-%{version}.tar.bz2 
Source1:         Doxyfile

Patch0:          polkit-qt-0.95.1-install-cmake-find.patch

## upstream patches

# Change ConsoleKit to systemd-logind
# KDEBUG-356984
Patch1:          change-consolekit-to-systemd-logind.patch

Source10:        macros.polkit-qt

BuildRequires:   automoc4
BuildRequires:   cmake
BuildRequires:   doxygen
BuildRequires:   pkgconfig(polkit-agent-1) pkgconfig(polkit-gobject-1)
BuildRequires:   pkgconfig(QtDBus) pkgconfig(QtGui) pkgconfig(QtXml)
%if 0%{?qt5}
BuildRequires:   pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Xml)
%endif

Obsoletes:       polkit-qt-examples < 0.10

Provides:        polkit-qt-1 = %{version}-%{release}

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package devel
Summary: Development files for PolicyKit Qt bindings
Provides: polkit-qt-1-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Doxygen documentation for the PolkitQt API
BuildArch: noarch
%description doc
%{summary}.

%if 0%{?qt5}
%package -n polkit-qt5-1
Summary: PolicyKit Qt5 bindings
Provides: polkit-qt5 = %{version}-%{release}
%description -n polkit-qt5-1
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package -n polkit-qt5-1-devel
Summary: Development files for PolicyKit Qt5 bindings
Provides: polkit-qt5-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n polkit-qt5-1-devel
%{summary}.
%endif


%prep
%setup -q -n %{name}-1-%{version}

# temporary patch - installs FindPolkitQt-1.cmake until we decide how to deal with cmake 
# module installation
%patch0 -p1 -b .install-cmake-find

%patch1 -p1

%build
mkdir -p %{_target_platform}
pushd    %{_target_platform}
%{cmake} \
  -DUSE_QT4:BOOL=ON -DUSE_QT5:BOOL=OFF \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DDATA_INSTALL_DIR:PATH=%{_datadir} \
  ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%if 0%{?qt5}
mkdir -p %{_target_platform}-qt5
pushd    %{_target_platform}-qt5
%{cmake} \
  -DUSE_QT4:BOOL=OFF -DUSE_QT5:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DDATA_INSTALL_DIR:PATH=%{_datadir} \
  ..
popd
make %{?_smp_mflags} -C %{_target_platform}-qt5
%endif

## build docs
doxygen %{SOURCE1}
# Remove installdox file - it is not necessary here
rm -fv html/installdox


%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -p -m644 -D %{SOURCE10} %{buildroot}%{rpm_macros_dir}/macros.polkit-qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README
%{_libdir}/libpolkit-qt-core-1.so.1*
%{_libdir}/libpolkit-qt-gui-1.so.1*
%{_libdir}/libpolkit-qt-agent-1.so.1*

%files devel
%{rpm_macros_dir}/macros.polkit-qt
%{_includedir}/polkit-qt-1/
%{_libdir}/libpolkit-qt-core-1.so
%{_libdir}/libpolkit-qt-gui-1.so
%{_libdir}/libpolkit-qt-agent-1.so
%{_libdir}/pkgconfig/polkit-qt-1.pc
%{_libdir}/pkgconfig/polkit-qt-core-1.pc
%{_libdir}/pkgconfig/polkit-qt-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt-agent-1.pc
%{_libdir}/cmake/PolkitQt-1/
%{_datadir}/cmake/Modules/*.cmake

%files doc
%doc html/*

%if 0%{?qt5}
%post -n polkit-qt5-1 -p /sbin/ldconfig
%postun -n polkit-qt5-1 -p /sbin/ldconfig

%files -n polkit-qt5-1
%doc AUTHORS COPYING README
%{_libdir}/libpolkit-qt5-core-1.so.1*
%{_libdir}/libpolkit-qt5-gui-1.so.1*
%{_libdir}/libpolkit-qt5-agent-1.so.1*

%files -n polkit-qt5-1-devel
%{rpm_macros_dir}/macros.polkit-qt
%{_includedir}/polkit-qt5-1/
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/cmake/PolkitQt5-1/
%endif


%changelog
* Mon Dec 21 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Change ConsoleKit to systemd-logind to fix KDEBUG-356984.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.112.0-6
- Rebuild for new 4.0 release

