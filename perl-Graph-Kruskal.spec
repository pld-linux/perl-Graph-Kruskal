%include	/usr/lib/rpm/macros.perl
Summary:	Graph-Kruskal perl module
Summary(pl):	Modu³ perla Graph-Kruskal
Name:		perl-Graph-Kruskal
Version:	2.0
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Graph/Graph-Kruskal-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph-Kruskal - Kruskal's Algorithm.

%description -l pl
Graph-Kruskal - algorytm Kruskala.

%prep
%setup -q -n Graph-Kruskal-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Graph/Kruskal.pm
%{_mandir}/man3/*
