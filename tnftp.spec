
%define		_ver		20030825

Summary:	The enhanced ftp client
Summary(pl):	Rozszerzony klient ftp
Name:		tnftp
Version:	2.0
Release:	0.%{_ver}.1
License:	BSD
Group:		Applications/Networking
Vendor:		Luke Mewburn <lukem@netbsd.org>
Source0:	ftp://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{_ver}.tar.gz
# Source0-md5:	9b633ae6cacc01dbdadc6b9e3f180b4f
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ftp
Obsoletes:	ftp6
Obsoletes:	lukemftp
Provides:	lukemftp

%description
The enhancements over the standard ftp client include:
- command-line fetching of URLS, including support for:
     - http proxies
     - authentication
- dynamic progress bar
- IPv6 support
- paging of local and remote files, and of directory listings
- socks4/socks5 support
- TIS Firewall Toolkit gate ftp proxy support
- transfer-rate throttling
- other

%description -l pl
Dodatkowe rozszerzenia w stosunku do standardowego klienta to:
- obs³uga URL-i w linii poleceñ w³±czaj±c wsparcie dla:
     - http i ftp proxy
     - autoryzacje
- dynamiczny wska¼nik postêpu
- stronicowanie lokalnych i zdalnych listingów plików i katalogów
- wsparcie dla IPv6
- wsparcie dla socks4/socks5
- wsparcie dla bramki ftp w TIS Firewall Toolkit
- inne

%prep
%setup -q -n %{name}-%{_ver}

%build

%configure2_13 \
	--enable-editcomplete \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1
install src/ftp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS todo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ftp.1*
