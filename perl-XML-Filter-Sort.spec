#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-Sort
Summary:	XML::Filter::Sort - SAX filter for sorting elements in XML
Summary(pl):	XML::Filter::Sort - filtr SAX sortuj±cy sk³adniki w XML-u
Name:		perl-XML-Filter-Sort
Version:	0.91
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72a342b5fdefea3769506870d47d615e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.41
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a SAX filter for sorting 'records' in XML documents
(including documents larger than available memory). The xmlsort
utility which is included with this distribution can be used to sort
an XML file from the command line without writing Perl code (see
perldoc xmlsort).

%description -l pl
Ten modu³ jest filtrem SAX do sortowania "rekordów" w dokumentach XML
(w³±cznie z dokumentami wiêkszymi od dostêpnej pamiêci). Narzêdzie
xmlsort za³±czone w pakiecie mo¿e byæ u¿ywane do sortowania pliku
XML z linii poleceñ bez pisania kodu w Perlu (wiêcej informacji w
perldoc xmlsort).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/*/*
%{_mandir}/man1/*
%{_mandir}/man3/*
