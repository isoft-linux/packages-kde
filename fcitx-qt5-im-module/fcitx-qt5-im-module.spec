Summary:        Qt5 im module for fcitx 
Name:           fcitx-qt5-im-module 
Version:        1.0.3
Release:        1 
License:        GPL
URL:            https://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/fcitx-qt5/fcitx-qt5-%{version}.tar.xz
BuildRequires:  qt5-qtbase-devel 
BuildRequires:  fcitx-devel
BuildRequires:  cmake

%description
Qt5 im module for fcitx

%package devel
Summary:        Development libraries for FCITX Qt5 im module
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The devel package includes the static libraries and header files
for the fcitx qt5 immodule package.

%prep
%setup -n fcitx-qt5-%{version}
#%patch0 -p1
%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make
popd

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd


rpmclean

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_libdir}/qt5/plugins/platforminputcontexts/*
%{_libdir}/lib*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/FcitxQt5DBusAddons
%{_libdir}/cmake/FcitxQt5WidgetsAddons


