Name:           ksshaskpass
Version:        5.4.2
Release:        2 
Summary:        A ssh-add helper that uses kwallet and kpassworddialog

License:        GPLv2
URL:            https://projects.kde.org/projects/kde/workspace/ksshaskpass
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  pkgconfig(Qt5Core)

%description
%{summary}.


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang ksshaskpass

# Setup environment variables
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/
cat >    %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh << EOF
SSH_ASKPASS=%{_kf5_bindir}/ksshaskpass
export SSH_ASKPASS
EOF

echo "NoDisplay=true" >> %{buildroot}%{_kf5_datadir}/applications/org.kde.ksshaskpass.desktop
%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.ksshaskpass.desktop

%files -f ksshaskpass.lang
%doc ChangeLog COPYING
%{_kf5_bindir}/ksshaskpass
%config(noreplace) %{_sysconfdir}/xdg/plasma-workspace/env/ksshaskpass.sh
%{_mandir}/man1/ksshaskpass.1*
%{_kf5_datadir}/applications/org.kde.ksshaskpass.desktop


%changelog
* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

