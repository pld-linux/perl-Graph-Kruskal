%include	/usr/lib/rpm/macros.perl
Summary:	Graph-Kruskal perl module
Summary(pl):	Modu³ perla Graph-Kruskal
Name:		perl-Graph-Kruskal
Version:	2.0
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Graph/Graph-Kruskal-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph-Kruskal - Kruskal's Algorithm.

%description -l pl
Graph-Kruskal - algorytm Kruskala.

%prep
%setup -q -n Graph-Kruskal-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Graph/Kruskal
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Graph/Kruskal.pm
%{perl_sitearch}/auto/Graph/Kruskal

%{_mandir}/man3/*
