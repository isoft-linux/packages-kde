%define         base_name systemsettings

Name:           plasma-%{base_name}
Version:        5.4.2
Release:        4 
Summary:        KDE's System Settings application

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/systemsettings

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

#we adjust some categories.
#move bluetooth from network to hardware.
Source1: settings-hardware-bluetooth.desktop

#add a new category proxy to support proxy.desktop we modified(in kio package).
Source2: settings-network-proxy.desktop

#add system administration top category.
Source3: settings-system-administration.desktop

Patch0: systemsettings-fine-icon-mode-size.patch

BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel

BuildRequires:  desktop-file-utils

Requires:       kf5-filesystem

# kde-cli-tools provides kcmshell5, which is not directly needed by
# systemsettings, but is an addition expected by users
Requires:       kde-cli-tools

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{base_name}-%{version}
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

#install our own settings category
install -m 0644 %{SOURCE1} %{buildroot}%{_kf5_datadir}/kservices5/
install -m 0644 %{SOURCE2} %{buildroot}%{_kf5_datadir}/kservices5/
install -m 0644 %{SOURCE3} %{buildroot}%{_kf5_datadir}/kservices5/
#remove original bluetooth category
rm -rf %{buildroot}%{_kf5_datadir}/kservices5/settings-network-bluetooth.desktop

%find_lang systemsettings5 --with-qt --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kdesystemsettings.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/systemsettings.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f systemsettings5.lang
%doc COPYING COPYING.DOC
%{_bindir}/systemsettings5
%{_libdir}/libsystemsettingsview.so.*
%{_kf5_qtplugindir}/*.so
%{_datadir}/systemsettings
%{_datadir}/applications/kdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/kxmlgui5/systemsettings
%{_docdir}/HTML/*/systemsettings

%files devel
%{_includedir}/systemsettingsview
%{_libdir}/libsystemsettingsview.so

%changelog
* Mon Oct 19 2015 Cjacker <cjacker@foxmail.com>
- Patch10 to fine the iconview item size.
- Do not wrap Chinese words too much.

* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- adjust some categories.

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

