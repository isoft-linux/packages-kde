%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


Name:           libdmtx
Version:        0.7.2
Release:        18
Summary:        Library for working with Data Matrix 2D bar-codes

License:        LGPLv2+
URL:            http://www.libdmtx.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-0.7.2-php54.patch
Patch1:         %{name}-0.7.2-ruby19.patch

BuildRequires:  ImageMagick-devel
# required for tests
BuildRequires:  SDL_image-devel
BuildRequires:  libGLU-devel
BuildRequires:  libpng-devel
# language bindings
BuildRequires:  python-devel


%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.

The included utility programs, dmtxread and dmtxwrite, provide the official
interface to libdmtx from the command line, and also serve as a good reference
for programmers who wish to write their own programs that interact with
libdmtx. All of the software in the libdmtx package is distributed under
the LGPLv2 and can be used freely under these terms.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        utils
Summary:        Utilities for %{name}
Requires:       %{name} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities that use %{name}.

# language bindings
%package -n     php-libdmtx
Summary:        PHP bindings for %{name}
License:        GPLv2+
Requires:       %{name} = %{version}-%{release}
Requires:       php-common

%description -n php-libdmtx
The php-%{name} package contains bindings for using %{name} from PHP.

%package -n     python-libdmtx
Summary:        Python bindings for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n python-libdmtx
The python-%{name} package contains bindings for using %{name} from Python.


%prep
%setup -q

# fix permissions
chmod a-x wrapper/{php,python}/README


%build
%configure --disable-static
make %{?_smp_mflags}

# temporary installation required by the language wrappers
make install DESTDIR=/tmp

# language wrappers must be built separately
pushd wrapper
pushd python
# fix paths
sed -i.orig -e "s|/usr/local/include|/tmp%{_includedir}|" -e "s|/usr/local/lib|/tmp%{_libdir}|" setup.py
python setup.py build
chmod 0755 build/lib.*/*.so
popd
popd


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

pushd wrapper
pushd python
python setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
popd


%check
make check
pushd test
for t in simple unit
do
    ./${t}_test/${t}_test
done
popd


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3*

%files utils
%defattr(-,root,root,-)
%{_bindir}/dmtx*
%{_mandir}/man1/dmtx*.1*

%files -n python-libdmtx
%defattr(-,root,root,-)
%doc wrapper/python/README
%{python_sitearch}/*

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.7.2-18
- Rebuild for new 4.0 release

