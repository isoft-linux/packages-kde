Name:           qrencode
Version:        3.4.2
Release:        6
Summary:        Generate QR 2D barcodes
Summary(fr):    Génère les code-barres en 2D QR

License:        LGPLv2+
URL:            http://fukuchi.org/works/qrencode/
Source0:        http://fukuchi.org/works/qrencode/%{name}-%{version}.tar.bz2

BuildRequires:	chrpath
BuildRequires:	libpng-devel

%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%description -l fr
Qrencode est un logiciel utilitaire utilisant libqrencode pour encoder
les données dans un QR Code et sauvegarde dans une image PNG.


%package        devel
Summary:        QR Code encoding library - Development files
Summary(fr):    Bibliothèque d'encodage QR Code - Fichiers de développement
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.

%description    devel -l fr
Le paquet qrencode-devel contient les bibliothèques et les fichiers d'en-tête
pour le développement d'applications utilisant qrencode.


%package        libs
Summary:        QR Code encoding library - Shared libraries
Summary(fr):    Bibliothèque d'encodage QR Code - Bibliothèque partagée

%description    libs
The qrencode-libs package contains the shared libraries and header files for
applications that use qrencode.

%description    libs -l fr
Le paquet qrencode-libs contient les bibliothèques partagées et les fichiers
d'en-tête pour les applications utilisant qrencode.


%prep
%setup -q


%build
%configure --with-tests --without-sdl
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT%{_libdir}/libqrencode.la
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/qrencode


%check
cd ./tests
sh test_all.sh


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%{_bindir}/qrencode
%{_mandir}/man1/qrencode.1*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NEWS README TODO
%{_libdir}/libqrencode.so.*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 3.4.2-6
- Rebuild for new 4.0 release

