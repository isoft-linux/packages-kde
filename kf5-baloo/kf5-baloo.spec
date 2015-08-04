%define         framework baloo
%define         plasma_version 5.3.0

Name:           kf5-%{framework}
Version:        5.9.2
Release:        1
Summary:        A Tier 3 KDE Frameworks 5 module that provides indexing and search functionality
License:        LGPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/baloo
# backup URL: https://community.kde.org/Baloo

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{plasma_version}/%{framework}-%{version}.tar.xz

Source1: 97-kde-baloo-filewatch-inotify.conf

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  xapian-core-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kfilemetadata-devel

Requires:       kf5-filesystem

Obsoletes:      kf5-baloo-tools < 5.5.95-1
Obsoletes:      baloo < 5
Provides:       baloo = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-file%{?_isa} = %{version}-%{release}
Requires:       kf5-kfilemetadata-devel
Requires:       xapian-core-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        file
Summary:        File indexing and search for Baloo
Obsoletes:      %{name} < 5.0.1-2
Obsoletes:      baloo-file < 5.0.1-2
Provides:       baloo-file = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
%description    libs
%{summary}.


%prep
%setup -qn %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

install -p -m644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf

%find_lang balooctl --with-qt
%find_lang kio_baloosearch --with-qt
%find_lang baloo_file --with-qt
%find_lang kio_tags --with-qt
%find_lang baloosearch --with-qt
%find_lang kio_timeline --with-qt
%find_lang baloo_file_extractor --with-qt
%find_lang balooshow --with-qt

cat kio_tags.lang kio_baloosearch.lang kio_timeline.lang \
    > %{name}-libs.lang

cat baloo_file.lang baloo_file_extractor.lang \
    > %{name}-file.lang

cat baloosearch.lang balooshow.lang balooctl.lang \
    > %{name}.lang


%post
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/hicolor &> /dev/null || :
fi

%files -f %{name}.lang
%{_kf5_bindir}/baloosearch
%{_kf5_bindir}/balooshow
%{_kf5_bindir}/balooctl
%{_kf5_plugindir}/kio/baloosearch.so
%{_kf5_plugindir}/kio/tags.so
%{_kf5_plugindir}/kio/timeline.so
%{_kf5_qtplugindir}/kded_baloosearch_kio.so
%{_kf5_qmldir}/org/kde/baloo
%{_kf5_datadir}/kservices5/baloosearch.protocol
%{_kf5_datadir}/kservices5/tags.protocol
%{_kf5_datadir}/kservices5/timeline.protocol
%{_kf5_datadir}/kservices5/kded/baloosearchfolderupdater.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/baloo.png

%files file -f %{name}-file.lang
%{_prefix}/lib/sysctl.d/97-kde-baloo-filewatch-inotify.conf
%{_kf5_bindir}/baloo_file
%{_kf5_bindir}/baloo_file_extractor
%{_kf5_bindir}/baloo_file_cleaner
%{_kf5_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_kf5_sysconfdir}/dbus-1/system.d/org.kde.baloo.filewatch.conf
%{_kf5_libexecdir}/kauth/kde_baloo_filewatch_raiselimit
%{_kf5_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_kf5_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f %{name}-libs.lang
%{_kf5_libdir}/libKF5Baloo.so.*
%{_kf5_libdir}/libKF5BalooXapian.so.*

%files devel
%{_kf5_libdir}/libKF5Baloo.so
%{_kf5_libdir}/libKF5BalooXapian.so
%{_kf5_libdir}/cmake/KF5Baloo
%{_kf5_includedir}/Baloo
%{_kf5_includedir}/baloo_version.h


%changelog
