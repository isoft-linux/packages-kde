%define checksum d2ddcc7caef4c1c2833e05ce161e2ae7
Name:           isoft-artwork
Version:        1.2.1
Release:        1%{?dist}
Summary:        isoft linux artwork

License:        GPL
URL:            http://i-soft.com.cn
Source0:	http://pkgs.isoft.zhcn.cc/repo/pkgs/%{name}/%{name}-%{version}.tar.gz/%{checksum}/%{name}-%{version}.tar.xz
BuildArch: noarch

%description
isoft linux artwork, include isoft logo, backgrounds.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_datadir}/isoft-artwork/*

%changelog
* Mon Jan 04 2016 xiaotian.wu@i-soft.com.cn - 1.2.1-1
- new version

* Thu Nov 19 2015 xiaotian.wu@i-soft.com.cn - 1.2-1
- new version

* Fri Nov 06 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 1.1-1
- new version

* Fri Nov 06 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 1-2
- rebuilt

* Fri Nov  6 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn>
- init. 
