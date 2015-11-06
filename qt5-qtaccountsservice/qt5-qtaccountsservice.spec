%global qt_module qtaccountsservice

Name:           qt5-%{qt_module}
Summary:        Qt5 - AccountService addon
Version:        0.6.1
Release:        1
License:        LGPLv2+
#URL:            https://github.com/hawaii-desktop/qt-accountsservice-addon
#git@git.isoft.zhcn.cc:zhaixiang/qtaccountsservice.git
Source0:        %{qt_module}-%{version}.tar.bz2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

%description
Qt-style API for freedesktop.org's AccountsService DBus service (see 
http://www.freedesktop.org/wiki/Software/AccountsService).


%package devel
Summary:    Development files for Qt Account Service Addon
Requires:   %{name}%{?isa} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description devel
Files for development using Qt Account Service Addon.


%prep
%setup -q -n %{qt_module}-%{version}


%build
%cmake_kf5
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

#sed -i 's#get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)#get_filename_component(PACKAGE_PREFIX_DIR "/usr" ABSOLUTE)#g' $RPM_BUILD_ROOT%{_libdir}/cmake/QtAccountsService/QtAccountsServiceConfig.cmake

#mv %{buildroot}%{_libdir}/qt %{buildroot}%{_libdir}/qt5
%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{_libdir}/libQtAccountsService.so.*
%{_libdir}/qt5/qml/QtAccountsService/libdeclarative_accountsservice.so
%{_libdir}/qt5/qml/QtAccountsService/plugins.qmltypes
%{_libdir}/qt5/qml/QtAccountsService/qmldir

%doc README.md


%files devel
%{_includedir}/QtAccountsService
%{_libdir}/cmake/QtAccountsService
%{_libdir}/libQtAccountsService.so


%changelog
* Fri Nov 06 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add oslogo path. 

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.6.0-3
- Rebuild for new 4.0 release

* Sun Sep 06 2015 Cjacker <cjacker@foxmail.com>
- update for support project with QT_NO_CAST_FROM_ASCII 
