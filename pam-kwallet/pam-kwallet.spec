Name:    pam-kwallet
Summary: PAM module for KWallet
Version: 0
Release: 0.8.git

License: LGPLv2+
URL:     http://www.kde.org/

# git clone git://anongit.kde.org/scratch/afiestas/pam-kwallet.git
Source0: pam-kwallet.tar.gz

Patch0: pam-kwallet-kwallet5.patch

BuildRequires: cmake >= 2.8
BuildRequires: libgcrypt-devel >= 1.5.0
BuildRequires: pam-devel

Requires: socat

%description
%{summary}.


%prep
%setup -q -n %{name}
%patch0 -p1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
/%{_lib}/security/pam_kwallet.so


%changelog
* Thu Jul 16 2015 Cjacker <cjacker@foxmail.com>
- patch to meet kwalletd kf5 requires.
