Name:    konsole5
Summary: KDE Terminal emulator
Version: 15.12.0
Release: 2%{?dist}

# sources: MIT and LGPLv2 and LGPLv2+ and GPLv2+
License: GPLv2 and GFDL
URL:     http://konsole.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/konsole-%{version}.tar.xz

#set default font size to 11.
Patch0: konsole-set-default-font.patch

Obsoletes: konsole < 14.12
Provides:  konsole = %{version}-%{release}

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel >= 5.10.0-3
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
## TODO?
#BuildRequires: kf5-konq-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel

Requires: %{name}-part%{?_isa} = %{version}-%{release}

%{?kf5_kinit_requires}

%description
%{summary}.

%package part
Summary: Konsole5 kpart plugin
%description part
%{summary}.


%prep
%setup -q -n konsole-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop


%files
%doc README
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_libdir}/libkdeinit5_konsole.so
%{_kf5_datadir}/applications/org.kde.konsole.desktop
%{_datadir}/appdata/org.kde.konsole.appdata.xml
%{_kf5_datadir}/knotifications5/konsole.notifyrc
%{_kf5_datadir}/kservices5/ServiceMenus/konsolehere.desktop
%{_kf5_datadir}/kservices5/ServiceMenus/konsolerun.desktop
%{_kf5_datadir}/kservicetypes5/terminalemulator.desktop
%{_kf5_datadir}/kxmlgui5/konsole/konsoleui.rc
%{_kf5_datadir}/kxmlgui5/konsole/sessionui.rc
%{_kf5_docdir}/HTML/en/konsole/

%post part -p /sbin/ldconfig
%postun part -p /sbin/ldconfig

%files part
%doc COPYING*
%{_kf5_datadir}/konsole/
%{_kf5_libdir}/libkonsoleprivate.so.15*
%{_kf5_qtplugindir}/konsolepart.so
%{_kf5_datadir}/kservices5/konsolepart.desktop
%{_kf5_datadir}/kxmlgui5/konsole/partui.rc


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

