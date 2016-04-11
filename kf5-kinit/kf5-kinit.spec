%global framework kinit
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           kf5-%{framework}
Version:        5.20.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 tier 3 solution for process launching

License:        LGPLv2+ and BSD
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

Source10:       macros.kf5-kinit

# backport hack to workaround klauncher/SM issues, see bug http://bugzilla.redhat.com/983110
#Patch1:  kinit-5.10.0-klauncher-qt_no_glib.patch

BuildRequires:  libX11-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  qt5-qtbase-devel

BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}

Requires:       kf5-filesystem

%description
kdeinit is a process launcher somewhat similar to the famous init used for
booting UNIX.

It launches processes by forking and then loading a dynamic library which should
contain a 'kdemain(...)' function.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{framework}-%{version}

#%patch1 -p1 -b .klauncher-qt_no_glib


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kinit5_qt --with-man --with-qt --all-name

# rpm macros
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.%{name}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kinit5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_bindir}/*
%{_kf5_libdir}/libkdeinit5_klauncher.so
%{_kf5_libexecdir}/*
%{_kf5_mandir}/man8/kdeinit5.8*

%files devel
%{_kf5_libdir}/cmake/KF5Init/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{rpm_macros_dir}/macros.%{name}


%changelog
* Mon Apr 11 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 5.20.0-1
- Release 5.20.0

* Sat Nov 14 2015 Cjacker <cjacker@foxmail.com> - 5.16.0-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.15.0-3
- Rebuild for new 4.0 release

* Sun Oct 11 2015 Cjacker <cjacker@foxmail.com>
- update to 5.15.0

* Sun Sep 13 2015 Cjacker <cjacker@foxmail.com>
- update to 5.14.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.13.0
