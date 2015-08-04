Name:    ksystemlog
Summary: System Log Viewer for KDE
Version: 15.04.3
Release: 2.git%{?dist}

License: GPLv2+
URL:     http://www.kde.org/applications/system/ksystemlog/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

Source0:ksystemlog.tar.gz

# fix ksystemlog to find log files correctly
Patch1: kdeadmin-4.8.4-syslog.patch

%description
This program is developed for beginner users, who don't know how to find
information about their Linux system, and don't know where log files are.

It is also of course designed for advanced users, who quickly want to understand
problems of their machine with a more powerful and graphical tool than tail -f
and less commands.


%prep
%setup -q -n %{name}
git checkout frameworks

%patch1 -p2 -b .logfile_loc


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
