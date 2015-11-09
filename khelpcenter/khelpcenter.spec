Name:           khelpcenter
Version:        5.4.3
Release:        1%{?dist}
Summary:        Application to show KDE Application's documentation
# Override khelpcenter subpackage from kde-runtime-15.04 (no longer built)
Epoch:          1

License:        GPLv2 or GPLv3
URL:            https://projects.kde.org/projects/kde/workspace/khelpcenter

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kinit-devel >= 5.10.0-3
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kservice-devel

BuildRequires:  python

BuildRequires:  desktop-file-utils

# _kde4_* macros
BuildRequires:  kde-filesystem

Requires:       kf5-filesystem

# libkdeinit5_*
%{?kf5_kinit_requires}

%description
%{summary}.


%prep
%setup -q

mv doc/CMakeLists.txt doc/CMakeLists.txt.en_only
grep 'add_subdirectory(en)' doc/CMakeLists.txt.en_only > doc/CMakeLists.txt


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang khelpcenter5 --with-qt --all-name

# Provide khelpcenter service for KDE 3 and KDE 4 applications
mkdir -p %{buildroot}/%{_kde4_datadir}/services
cp %{buildroot}/%{_datadir}/kservices5/khelpcenter.desktop \
   %{buildroot}/%{_kde4_datadir}/services
mkdir -p %{buildroot}/%{_kde4_datadir}/kde4/services
cp %{buildroot}/%{_datadir}/kservices5/khelpcenter.desktop \
   %{buildroot}/%{_kde4_datadir}/kde4/services


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.Help.desktop


%files -f khelpcenter5.lang
%doc README.htdig README.metadata COPYING
%{_bindir}/khelpcenter
%{_libexecdir}/khc_indexbuilder
%{_libexecdir}/khc_htdig.pl
%{_libexecdir}/khc_htsearch.pl
%{_libexecdir}/khc_mansearch.pl
%{_libexecdir}/khc_docbookdig.pl
%{_kf5_libdir}/libkdeinit5_khelpcenter.so
%{_kf5_datadir}/khelpcenter/
%{_kf5_datadir}/kxmlgui5/khelpcenter/khelpcenterui.rc
%{_datadir}/applications/org.kde.Help.desktop
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/kservices5/khelpcenter.desktop
%{_datadir}/dbus-1/interfaces/org.kde.khelpcenter.kcmhelpcenter.xml
%{_kde4_datadir}/services/khelpcenter.desktop
%{_kde4_datadir}/kde4/services/khelpcenter.desktop
%lang(en) /usr/share/doc/HTML/en/fundamentals/
%lang(en) /usr/share/doc/HTML/en/khelpcenter/
%lang(en) /usr/share/doc/HTML/en/onlinehelp/


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1:5.4.2-2
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95
