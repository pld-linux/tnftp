
%define		_ver	20070806

Summary:	The enhanced FTP client
Summary(pl.UTF-8):	Rozszerzony klient FTP
Name:		tnftp
Version:	2.0
Release:	0.%{_ver}.1
License:	BSD
Group:		Applications/Networking
Vendor:		Luke Mewburn <lukem@netbsd.org>
Source0:	ftp://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{_ver}.tar.gz
# Source0-md5:	bc78ddc857156f8bc4222d15cce6f76d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.2
Obsoletes:	ftp
Obsoletes:	ftp6
Obsoletes:	lukemftp
Provides:	lukemftp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The enhancements over the standard FTP client include:
- command-line fetching of URLs, including support for:
	- HTTP and FTP proxies
	- authentication
- dynamic progress bar
- IPv6 support
- paging of local and remote files, and of directory listings
- socks4/socks5 support
- TIS Firewall Toolkit gate FTP proxy support
- transfer-rate throttling
- other

%description -l pl.UTF-8
Dodatkowe rozszerzenia w stosunku do standardowego klienta to:
- obsługa URLi w linii poleceń włączając wsparcie dla:
	- HTTP i FTP proxy
	- autoryzacje
- dynamiczny wskaźnik postępu
- stronicowanie lokalnych i zdalnych listingów plików i katalogów
- wsparcie dla IPv6
- wsparcie dla socks4/socks5
- wsparcie dla bramki FTP w TIS Firewall Toolkit
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
