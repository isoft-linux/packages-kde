Name:           isoft-artwork
Version:        1
Release:        2%{?dist}
Summary:        isoft linux artwork

License:        GPL
URL:            http://i-soft.com.cn
Source0:       isoft-artwork.tar.gz
BuildArch: noarch

%description
isoft linux artwork, include isoft logo, backgrounds.


%prep
%setup -q -n %{name}

%build
%install
pwd
ls
mkdir -p %{buildroot}%{_datadir}/isoft-artwork
cp -r logo %{buildroot}%{_datadir}/isoft-artwork

%files
%{_datadir}/isoft-artwork/*

%changelog
* Fri Nov 06 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 1-2
- rebuilt

* Fri Nov  6 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn>
- init. 
