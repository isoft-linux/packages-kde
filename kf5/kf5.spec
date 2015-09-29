Name:           kf5
Version:        5.14.0
Release:        3
Summary:        Filesystem and RPM macros for KDE Frameworks 5
License:        BSD
URL:            http://www.kde.org

Source0:        macros.kf5

%description
Filesystem and RPM macros for KDE Frameworks 5

%package        filesystem
Summary:        Filesystem for KDE Frameworks 5
# noarch -> arch transition
Obsoletes:      kf5-filesystem < 5.10.0-2
%description    filesystem
Filesystem for KDE Frameworks 5.

%package        rpm-macros
Summary:        RPM macros for KDE Frameworks 5
BuildArch: noarch
%description    rpm-macros
RPM macros for building KDE Frameworks 5 packages.


%install
# See macros.kf5 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/plugins/kf5/
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_datadir}/{kconf_update,kf5}
mkdir -p %{buildroot}%{_libexecdir}/kf5
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}

install -Dpm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5


%files filesystem
%{_sysconfdir}/xdg/plasma-workspace/
%{_prefix}/lib/qt5/plugins/kf5/
%{_prefix}/%{_lib}/qt5/plugins/kf5/
%{_includedir}/KF5/
%{_libexecdir}/kf5/
%{_datadir}/kconf_update/
%{_datadir}/kf5/

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf5

%changelog
* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
