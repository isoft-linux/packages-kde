Summary: Bidirectional data relay between two data channels ('netcat++')
Name: socat
Version: 1.7.2.4
Release: 6
License: GPLv2
Url:  http://www.dest-unreach.org/%{name}
Source: http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.gz

BuildRequires: openssl-devel readline-devel ncurses-devel
BuildRequires: autoconf kernel-headers > 2.6.18
# for make test
BuildRequires: iproute net-tools coreutils procps-ng openssl iputils
Patch1: socat-1.7.2.4-test.patch
Patch2: socat-1.7.2.4-errqueue.patch

%description
Socat is a relay for bidirectional data transfer between two independent data
channels. Each of these data channels may be a file, pipe, device (serial line
etc. or a pseudo terminal), a socket (UNIX, IP4, IP6 - raw, UDP, TCP), an
SSL socket, proxy CONNECT connection, a file descriptor (stdin etc.), the GNU
line editor (readline), a program, or a combination of two of these. 


%prep
%setup -q 
iconv -f iso8859-1 -t utf-8 CHANGES > CHANGES.utf8
mv CHANGES.utf8 CHANGES
%patch1 -p1
%patch2 -p1

%build
%configure  \
        --enable-help --enable-stdio \
        --enable-fdnum --enable-file --enable-creat \
        --enable-gopen --enable-pipe --enable-termios \
        --enable-unix --enable-ip4 --enable-ip6 \
        --enable-rawip --enable-tcp --enable-udp \
        --enable-listen --enable-proxy --enable-exec \
        --enable-system --enable-pty --enable-readline \
        --enable-openssl --enable-sycls --enable-filan \
        --enable-retry --enable-libwrap --enable-fips

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}/%{_docdir}/socat
install -m 0644 *.sh %{buildroot}/%{_docdir}/socat/

%check
export TERM=ansi
export OD_C=/usr/bin/od
# intermittently, a test sometimes just fails and hangs, mostly on arm
#timeout 30m make test

%files 
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ PORTING
%doc COPYING* README SECURITY testcert.conf
%doc %{_docdir}/socat/*.sh
%{_bindir}/socat
%{_bindir}/filan
%{_bindir}/procan
%doc %{_mandir}/man1/socat.1*

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.7.2.4-6
- Rebuild for new 4.0 release

