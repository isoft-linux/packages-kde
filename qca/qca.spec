
# enable qt5 support
%define qt5 1

Name:    qca
Summary: Qt Cryptographic Architecture
Version: 2.1.0
Release: 14%{?dist}

License: LGPLv2+
URL:     http://delta.affinix.com/qca
Source0: http://delta.affinix.com/download/qca/2.0/qca-%{version}.tar.gz

## upstream patches
Patch1: 0001-dropped-unused-include.patch
Patch2: 0002-cmake-pkg-config-is-not-REQUIRED.patch
Patch3: 0003-qca-ossl-fixed-compilation-warnings.patch
Patch4: 0004-cmake-dropped-dead-variable.patch
Patch5: 0005-Fix-build-with-libressl.patch
Patch6: 0006-increased-minimum-cmake-version.patch
Patch7: 0007-cmake-warn-user-when-QCA_SUFFIX-is-not-set.patch
Patch8: 0008-cmake-apply-QCA_SUFFIX-for-cmake-config-module-names.patch
Patch9: 0009-cmake-build-for-android.patch
Patch10: 0010-fixed-compilation-on-android.patch
Patch11: 0011-simplified-md5_state_t-and-SHA1_CONTEXT-internal-str.patch
Patch12: 0012-cmake-fixed-warnings-on-android.patch
Patch13: 0013-docs-fixed-no-images-in-docs-when-build-out-of-sourc.patch
Patch14: 0014-cmake-fixed-cmake-config-module-when-used-QCA_SUFFIX.patch
Patch15: 0015-fix-library-name-in-prf-file-to-use-the-lib-name-var.patch
Patch16: 0016-move-QCA_CONFIG_NAME_BASE-definition-in-the-regular-.patch
Patch17: 0017-fixed-array-size-checking.patch
Patch18: 0018-add-a-reviewboardrc.patch
Patch19: 0019-prevent-filewatches-from-emitting-changes-when-there.patch
Patch20: 0020-put-headers-of-a-suffixed-build-in-a-suffixed-direct.patch
# qt5 branch
Patch21: 0021-properly-support-co-existing-qt4-and-qt5-versions.patch
Patch22: 0022-initialize-QCA_SUFFIX-cache-with-the-possibly-previo.patch

Patch23: qca-add-missing-header.patch
Patch24: qca-disable-bsd-source-warning.patch

#dirty, qca test take too much time to run.
Patch30: qca-disable-qca-test.patch

BuildRequires: cmake >= 2.8.12
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(botan-1.10)
BuildRequires: pkgconfig(libcrypto) pkgconfig(libssl)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libpkcs11-helper-1)
BuildRequires: pkgconfig(libsasl2)
BuildRequires: pkgconfig(QtCore)
# apidocs
# may need to add some tex-related ones too -- rex
BuildRequires: doxygen
BuildRequires: graphviz


# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package devel
Summary: Qt Cryptographic Architecture development files
# qca2 renamed qca
Obsoletes: qca2-devel < 2.1.0
Provides:  qca2-devel = %{version}-%{release}
Provides:  qca2-devel%{?_isa} = %{version}-%{release}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
This packages contains the development files for QCA.

%package doc
Summary: QCA API documentation
BuildArch: noarch
%description doc
This package includes QCA API documentation in HTML

%package botan
Summary: Botan plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description botan
%{summary}.

%package cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cyrus-sasl
%{summary}.

%package gcrypt
Summary: Gcrypt plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gcrypt
%{summary}.

%package gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnupg
%description gnupg
%{summary}.

%package logger
Summary: Logger plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description logger
%{summary}.

%package nss
Summary: Nss plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description nss
%{summary}.

%package ossl
Summary: Openssl plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description ossl
%{summary}.

%package pkcs11
Summary: Pkcs11 plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description pkcs11
%{summary}.

%package softstore
Summary: Pkcs11 plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description softstore
%{summary}.

%if 0%{?qt5}
%package qt5
Summary: Qt5 Cryptographic Architecture
BuildRequires: pkgconfig(Qt5Core)
%description qt5
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package qt5-devel
Summary: Qt5 Cryptographic Architecture development files
Requires:  %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt5-botan
Summary: Botan plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-botan
%{summary}.

%package qt5-cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-cyrus-sasl
%{summary}.

%package qt5-gcrypt
Summary: Gcrypt plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-gcrypt
%{summary}.

%package qt5-gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: gnupg
%description qt5-gnupg
%{summary}.

%package qt5-logger
Summary: Logger plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-logger
%{summary}.

%package qt5-nss
Summary: Nss plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-nss
%{summary}.

%package qt5-ossl
Summary: Openssl plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-ossl
%{summary}.

%package qt5-pkcs11
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-pkcs11
%{summary}.

%package qt5-softstore
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-softstore
%{summary}.
%endif


%prep
%autosetup -p1


%build
%if 0%{?qt5}
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} .. \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt5_prefix}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt5_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt5_libdir} \
  -DQCA_SUFFIX:STRING="qt5" \
  -DQT4_BUILD:BOOL=OFF

make %{?_smp_mflags}
popd
%endif


mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DQCA_DOC_INSTALL_DIR:PATH=%{_docdir}/qca \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt4_prefix}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt4_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_libdir} \
  -DQT4_BUILD:BOOL=ON
popd

make %{?_smp_mflags} -C %{_target_platform}

make doc %{?_smp_mflags} -C %{_target_platform}


%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# no make install target for docs yet
mkdir -p %{buildroot}%{_docdir}/qca
cp -a %{_target_platform}/apidocs/html/ \
      %{buildroot}%{_docdir}/qca/


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion qca2)" = "%{version}"
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--timeout 600 --output-on-failure" -C %{_target_platform}
%if 0%{?qt5}
make test ARGS="--timeout 600 --output-on-failure" -C %{_target_platform}-qt5
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README TODO
%{_libdir}/libqca.so.2*
%{_bindir}/mozcerts
%{_bindir}/qcatool
%{_mandir}/man1/qcatool.1*
## HACK alert, quirk of recycling default %%_docdir below in -doc subpkg -- rex
%exclude %{_docdir}/qca/html/

%files doc
%{_docdir}/qca/html/

%files devel
%{_qt4_headerdir}/QtCrypto
%{_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_libdir}/cmake/Qca/
%{_qt4_prefix}/mkspecs/features/crypto.prf

%files botan
%doc plugins/qca-botan/README
%{_qt4_plugindir}/crypto/libqca-botan.so

%files cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt4_plugindir}/crypto/libqca-cyrus-sasl.so

%files gcrypt
%{_qt4_plugindir}/crypto/libqca-gcrypt.so

%files gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt4_plugindir}/crypto/libqca-gnupg.so

%files logger
%doc plugins/qca-logger/README
%{_qt4_plugindir}/crypto/libqca-logger.so

%files nss
%doc plugins/qca-nss/README
%{_qt4_plugindir}/crypto/libqca-nss.so

%files ossl
%doc plugins/qca-ossl/README
%{_qt4_plugindir}/crypto/libqca-ossl.so

%files pkcs11
%doc plugins/qca-pkcs11/README
%{_qt4_plugindir}/crypto/libqca-pkcs11.so

%files softstore
%doc plugins/qca-softstore/README
%{_qt4_plugindir}/crypto/libqca-softstore.so

%if 0%{?qt5}
%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%files qt5
%doc COPYING README TODO
%{_bindir}/mozcerts-qt5
%{_bindir}/qcatool-qt5
%{_mandir}/man1/qcatool-qt5.1*
%{_qt5_libdir}/libqca-qt5.so.2*

%files qt5-devel
%{_qt5_headerdir}/QtCrypto
%{_qt5_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/cmake/Qca-qt5/
%{_qt5_prefix}/mkspecs/features/crypto.prf

%files qt5-botan
%doc plugins/qca-botan/README
%{_qt5_plugindir}/crypto/libqca-botan.so

%files qt5-cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt5_plugindir}/crypto/libqca-cyrus-sasl.so

%files qt5-gcrypt
%{_qt5_plugindir}/crypto/libqca-gcrypt.so

%files qt5-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt5_plugindir}/crypto/libqca-gnupg.so

%files qt5-logger
%doc plugins/qca-logger/README
%{_qt5_plugindir}/crypto/libqca-logger.so

%files qt5-nss
%doc plugins/qca-nss/README
%{_qt5_plugindir}/crypto/libqca-nss.so

%files qt5-ossl
%doc plugins/qca-ossl/README
%{_qt5_plugindir}/crypto/libqca-ossl.so

%files qt5-pkcs11
%doc plugins/qca-pkcs11/README
%{_qt5_plugindir}/crypto/libqca-pkcs11.so

%files qt5-softstore
%doc plugins/qca-softstore/README
%{_qt5_plugindir}/crypto/libqca-softstore.so
%endif


%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 2.1.0-14
- Rebuild for new 4.0 release

* Thu Aug 13 2015 Cjacker <cjacker@foxmail.com>
- add patch23, fix missing header.
- add patch24, disable BSD_SOURCE warnings.
- enable botan/sasl plugin.
