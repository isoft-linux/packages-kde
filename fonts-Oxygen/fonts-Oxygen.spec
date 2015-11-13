%global fontname oxygen
%global fontconf 61-%{fontname}

Name:           fonts-Oxygen
Version:        5.4.3
Release:        2
Summary:        Oxygen fonts created by the KDE Community

License:        OFL or GPLv3 with exceptions
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/plasma/%{version}/oxygen-fonts-%{version}.tar.xz

#apply this patch to skip font build. it needs fontforge
Patch0:         oxygen-directly-use-prebuild-fonts.patch

Source1:        61-oxygen-mono.conf
Source2:        61-oxygen-sans.conf

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Provides:   oxygen-fonts = %{version}

BuildArch: noarch

%description
Oxygen fonts created by the KDE Community.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

Provides:   oxygen-fonts-devel = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n oxygen-fonts-%{version}
%patch0 -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. -DOXYGEN_FONT_INSTALL_DIR=%{_datadir}/fonts -DKDE_INSTALL_INCLUDEDIR=%{_includedir} -DKDE_INSTALL_BINDIR=%{_bindir} -DKDE_INSTALL_LIBDIR=%{_libdir}
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -m 0755 -d %{buildroot}/%{_datadir}/fontconfig/conf.avail \
                   %{buildroot}/%{_sysconfdir}/fonts/conf.d

install -m 0644 -p %{SOURCE1} %{SOURCE2} \
        %{buildroot}/%{_datadir}/fontconfig/conf.avail/

ln -s %{_datadir}/fontconfig/conf.avail/61-oxygen-mono.conf \
      %{buildroot}/etc/fonts/conf.d/61-oxygen-mono.conf
ln -s %{_datadir}/fontconfig/conf.avail/61-oxygen-sans.conf \
      %{buildroot}/etc/fonts/conf.d/61-oxygen-sans.conf

%files
%{_sysconfdir}/fonts/conf.d/*
%{_datadir}/fontconfig/conf.avail/*
%{_datadir}/fonts/*.ttf

%files devel
%{_libdir}/cmake/OxygenFont/

%changelog
* Sat Nov 07 2015 Cjacker <cjacker@foxmail.com> - 5.4.3-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.2-3
- Rebuild for new 4.0 release

* Wed Oct 07 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.2

* Wed Sep 09 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.1

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

* Wed Aug 12 2015 Cjacker <cjacker@foxmail.com>
- update to 5.3.95

