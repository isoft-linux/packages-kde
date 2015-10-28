Name:           qt-gstreamer
Version:        1.2.0
Release:        5
Summary:        C++ bindings for GStreamer with a Qt-style API
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/modules/qt-gstreamer.html
#http://cgit.freedesktop.org/gstreamer/qt-gstreamer/
#git clone git://anongit.freedesktop.org/gstreamer/qt-gstreamer
Source0:        http://gstreamer.freedesktop.org/src/%{name}/%{name}.tar.gz
Patch0:         qt-gstreamer-hack-with-new-gstreamer-include-path.patch
Patch1:         qt-gstreamer-fix-build-with-new-boost.patch

BuildRequires:  automoc
BuildRequires:  boost-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquick1-devel

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt4 applications.


%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
%description devel
This package contains the header files and development documentation
for %{name}.

%package -n qt5-gstreamer
Summary:        C++ bindings for GStreamer with a Qt5-style API
%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}
%description -n qt5-gstreamer
QtGStreamer provides C++ bindings for GStreamer with a Qt-style
API, plus some helper classes for integrating GStreamer better
in Qt5 applications.

%package -n qt5-gstreamer-devel
Summary:        Header files and development documentation for qt5-gstreamer
Requires:       qt5-gstreamer%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
%description -n qt5-gstreamer-devel
This package contains the header files and development documentation
for qt5-gstreamer.

%prep
%setup -q -n qt-gstreamer
%patch0 -p1
#%patch1 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DQT_VERSION=4 ..
popd

make %{?_smp_mflags} -C %{_target_platform}

mkdir -p %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} -DQT_VERSION=5 ..
popd

make %{?_smp_mflags} -C %{_target_platform}-qt5


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/gstreamer-1.0/libgstqtvideosink.so
%{_libdir}/libQtGLib-2.0.so.0
%{_libdir}/libQtGLib-2.0.so.1*
%{_libdir}/libQtGStreamer-1.0.so.0
%{_libdir}/libQtGStreamer-1.0.so.1*
%{_libdir}/libQtGStreamerUi-1.0.so.0
%{_libdir}/libQtGStreamerUi-1.0.so.1*
%{_libdir}/libQtGStreamerUtils-1.0.so.0
%{_libdir}/libQtGStreamerUtils-1.0.so.1*
%{_libdir}/qt4/imports/QtGStreamer/

%files devel
%doc HACKING
%{_includedir}/QtGStreamer
%{_libdir}/cmake/QtGStreamer
%{_libdir}/libQtGLib-2.0.so
%{_libdir}/libQtGStreamer-1.0.so
%{_libdir}/libQtGStreamerUi-1.0.so
%{_libdir}/libQtGStreamerUtils-1.0.so
%{_libdir}/pkgconfig/QtGLib-2.0.pc
%{_libdir}/pkgconfig/QtGStreamer-1.0.pc
%{_libdir}/pkgconfig/QtGStreamerUi-1.0.pc
%{_libdir}/pkgconfig/QtGStreamerUtils-1.0.pc

%post -n qt5-gstreamer -p /sbin/ldconfig
%postun -n qt5-gstreamer -p /sbin/ldconfig

%files -n qt5-gstreamer
%doc COPYING README
%{_libdir}/gstreamer-1.0/libgstqt5videosink.so
%{_libdir}/libQt5GLib-2.0.so.0
%{_libdir}/libQt5GLib-2.0.so.1*
%{_libdir}/libQt5GStreamer-1.0.so.0
%{_libdir}/libQt5GStreamer-1.0.so.1*
%{_libdir}/libQt5GStreamerUi-1.0.so.0
%{_libdir}/libQt5GStreamerUi-1.0.so.1*
%{_libdir}/libQt5GStreamerUtils-1.0.so.0
%{_libdir}/libQt5GStreamerUtils-1.0.so.1*
%{_libdir}/libQt5GStreamerQuick-1.0.so.0
%{_libdir}/libQt5GStreamerQuick-1.0.so.1*
%{_libdir}/qt5/imports/QtGStreamer/
%{_libdir}/qt5/qml/QtGStreamer/

%files -n qt5-gstreamer-devel
%doc HACKING
%{_includedir}/Qt5GStreamer
%{_libdir}/cmake/Qt5GStreamer
%{_libdir}/libQt5GLib-2.0.so
%{_libdir}/libQt5GStreamer-1.0.so
%{_libdir}/libQt5GStreamerUi-1.0.so
%{_libdir}/libQt5GStreamerUtils-1.0.so
%{_libdir}/libQt5GStreamerQuick-1.0.so
%{_libdir}/pkgconfig/Qt5GLib-2.0.pc
%{_libdir}/pkgconfig/Qt5GStreamer-1.0.pc
%{_libdir}/pkgconfig/Qt5GStreamerUi-1.0.pc
%{_libdir}/pkgconfig/Qt5GStreamerUtils-1.0.pc
%{_libdir}/pkgconfig/Qt5GStreamerQuick-1.0.pc
%{_libdir}/pkgconfig/Qt5GStreamerQuick-1.0.pc


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.2.0-5
- Rebuild for new 4.0 release

