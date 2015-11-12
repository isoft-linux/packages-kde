Name:    ksystemlog
Summary: System Log Viewer for KDE
Version: 15.08.3
Release: 2.git%{?dist}

License: GPLv2+
URL:     http://www.kde.org/applications/system/ksystemlog/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif

#git
Source0: ksystemlog.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros

BuildRequires: pkgconfig
BuildRequires: qt5-qtbase-devel

BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: python

#for journald
BuildRequires: systemd-devel

%description
This program is developed for beginner users, who don't know how to find
information about their Linux system, and don't know where log files are.

It is also of course designed for advanced users, who quickly want to understand
problems of their machine with a more powerful and graphical tool than tail -f
and less commands.


%prep
%setup -q -n %{name}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.ksystemlog.desktop


%files
%doc COPYING
%{_bindir}/ksystemlog
%{_datadir}/applications/org.kde.ksystemlog.desktop
%{_datadir}/kxmlgui5/ksystemlog/ksystemlogui.rc
%{_docdir}/HTML/en/ksystemlog


%changelog
* Thu Nov 12 2015 Cjacker <cjacker@foxmail.com> - 15.08.3-2.git
- Update, enable systemd journald support. 

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 15.04.3-3.git
- Rebuild for new 4.0 release

