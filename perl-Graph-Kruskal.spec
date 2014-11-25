%define		pdir	Graph
%define		pnam	Kruskal
%include	/usr/lib/rpm/macros.perl
Summary:	Graph::Kruskal - Kruskal's algorithm for Minimal Spanning Trees in graphs
Summary(pl.UTF-8):	Graph::Kruskal - algorytm Kruskala do tworzenia minimalnych drzew rozpinających w grafach
Name:		perl-Graph-Kruskal
Version:	2.0
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04abf8673b5a6dcc865981a856fd0b7f
URL:		http://search.cpan.org/dist/Graph-Kruskal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph::Kruskal Perl module implements the Kruskal's algorithm for
Minimal Spanning Trees in graphs.

Computes the Minimal Spanning Tree of a given graph according to some
cost function defined on the edges of the graph.

%description -l pl.UTF-8
Moduł Perla Graph::Kruskal stanowi implementację algorytmu Kruskala do
tworzenia minimalnych drzew rozpinających w grafach.

Oblicza minimalne drzewo rozpinające dla zadanego grafu w odniesieniu
do pewnej funkcji kosztu zdefiniowanej dla krawędzi grafu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Graph/Kruskal.pm
%{_mandir}/man3/*
