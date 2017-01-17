Name:           kf5
Version:        5.30.0
Release:        1
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
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_includedir}/KF5
mkdir -p %{buildroot}%{_datadir}/{kconf_update,kf5,kservicetypes5}
mkdir -p %{buildroot}%{_datadir}/kservices5/ServiceMenus
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_libexecdir}/kf5
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}

install -Dpm644 %{_sourcedir}/macros.kf5 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5
sed -i \
  -e "s|@@KF5_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf5


%files filesystem
%{_sysconfdir}/xdg/plasma-workspace/
%{_prefix}/lib/qt5/plugins/kf5/
%{_prefix}/%{_lib}/qt5/plugins/kf5/
%{_prefix}/lib/kconf_update_bin/
%{_prefix}/%{_lib}/kconf_update_bin/
%{_includedir}/KF5/
%{_libexecdir}/kf5/
%{_datadir}/kconf_update/
%{_datadir}/kf5/
%{_datadir}/kservices5/
%{_datadir}/kservicetypes5/
%{_datadir}/solid/

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf5

%changelog
* Tue Jan 17 2017 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.30.0-1
- 5.30.0-1

* Tue Dec 13 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.29.0-1
- 5.29.0-1

* Tue Nov 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.28.0-1
- 5.28.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-4
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
