%include	/usr/lib/rpm/macros.perl
%define	pdir	Graph
%define	pnam	Kruskal
Summary:	Graph::Kruskal perl module
Summary(pl):	Modu³ perla Graph::Kruskal
Name:		perl-Graph-Kruskal
Version:	2.0
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04abf8673b5a6dcc865981a856fd0b7f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph::Kruskal - Kruskal's Algorithm.

%description -l pl
Graph::Kruskal - algorytm Kruskala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Graph/Kruskal.pm
%{_mandir}/man3/*
