%define nepomuk 0 
%define plasma5 1

Name:    kactivities
Summary: API for using and interacting with Activities 
Version: 4.13.3
Release: 11

License: GPLv2+ and LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdelibs/kactivities
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz
Patch0: kactivities-fix-cmake-err.patch

BuildRequires: kdelibs-devel >= %{version}
%if ! 0%{?nepomuk}
Obsoletes: %{name}-nepomuk < %{version}-%{release}
%endif

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime 
Conflicts: kdebase-runtime < 4.7.3-10

Obsoletes: libkactivities < 6.1-100
Provides:  libkactivities = 6.2-1

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
API for using and interacting with Activities as a consumer, 
application adding information to them or as an activity manager.

%package libs
Summary: Runtime libraries for %{name}
Requires: kdelibs%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
# upgrade path, -libs was originally split out in 4.13.1-3, but bumping
# due to one irc user who somehow still had 4.13.3-1.i686 (on x86_64)
# bumped again to -7 for bug#1172523
Obsoletes: kactivities < 4.13.3-7
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: libkactivities-devel < 6.1-100
Provides:  libkactivities-devel = 6.2-1
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if ! 0%{?nepomuk}
Obsoletes: %{name}-nepomuk-devel < %{version}-%{release}
%endif
Requires: kdelibs-devel
%description devel
%{summary}.

%if 0%{?nepomuk}
%package nepomuk
Summary: KActivities nepomuk support
BuildRequires: nepomuk-core-devel >= %{version}
BuildRequires: pkgconfig(soprano)
# upgrade path
Obsoletes: kactivities < 4.13.0-2
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# not sure if an explicit dep is needed or worth it -- rex
#Requires: nepomuk-core%{?_isa} >= %{version}
%description nepomuk
%{summary}.

%package nepomuk-devel
Summary: KActivities nepomuk development files
Obsoletes: kactivities-devel < 4.13.3-2
Requires: %{name}-nepomuk%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description nepomuk-devel
%{summary}.
%endif


%prep
%setup -q 
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

## unpackaged files
%if ! 0%{?nepomuk}
rm -rfv %{buildroot}%{_kde4_datadir}/ontology/kde/
%endif
%if 0%{?plasma5}
rm -fv %{buildroot}%{_kde4_bindir}/kactivitymanagerd
rm -fv %{buildroot}%{_kde4_libdir}/kde4/activitymanager_plugin_{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.so
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/activitymanager-plugin-{activityranking,globalshortcuts,slc,sqlite,virtualdesktopswitch}.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
rm -fv %{buildroot}%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif


%if ! 0%{?plasma5}
%files
%{_kde4_bindir}/kactivitymanagerd
%{_kde4_libdir}/kde4/activitymanager_plugin_activityranking.so
%{_kde4_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%{_kde4_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde4_libdir}/kde4/activitymanager_plugin_sqlite.so
%{_kde4_libdir}/kde4/activitymanager_plugin_virtualdesktopswitch.so
%{_kde4_datadir}/kde4/services/activitymanager-plugin-activityranking.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-sqlite.desktop
%{_kde4_datadir}/kde4/services/activitymanager-plugin-virtualdesktopswitch.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde4_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%endif

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kde4_libdir}/libkactivities.so.6*
%{_kde4_libdir}/kde4/kcm_activities.so
%{_kde4_datadir}/kde4/services/kcm_activities.desktop
%{_kde4_appsdir}/activitymanager/

%files devel
%{_kde4_libdir}/libkactivities.so
%{_kde4_libdir}/cmake/KActivities/
%{_kde4_libdir}/pkgconfig/libkactivities.pc
%{_kde4_includedir}/KDE/KActivities/
%{_kde4_includedir}/kactivities/

%if 0%{?nepomuk}
%post nepomuk -p /sbin/ldconfig
%postun nepomuk -p /sbin/ldconfig

%files nepomuk
%{_kde4_libdir}/kde4/kio_activities.so
%{_kde4_libdir}/libkactivities-models.so.1*
%{_kde4_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde4_libdir}/kde4/kactivitymanagerd_fileitem_linking_plugin.so
%{_kde4_datadir}/kde4/services/activities.protocol
%{_kde4_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde4_datadir}/kde4/services/kactivitymanagerd_fileitem_linking_plugin.desktop
%{_kde4_datadir}/ontology/kde/
%dir %{_kde4_libdir}/kde4/imports/org/kde
%{_kde4_libdir}/kde4/imports/org/kde/activities

%files nepomuk-devel
%{_kde4_libdir}/libkactivities-models.so
%{_kde4_libdir}/cmake/KActivities-Models/
%{_kde4_libdir}/pkgconfig/libkactivities-models.pc
%{_kde4_includedir}/kactivities-models/
%endif


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 4.13.3-11
- Rebuild for new 4.0 release

