#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	pdir	Term
%define	pnam	Table
Summary:	Term::Table - Format a header and rows into a table
Summary(pl.UTF-8):	Term::Table - formatowanie nagłówka i wierszy w tabelę
Name:		perl-Term-Table
Version:	0.012
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a38cad6182e2c4864752746f1035abbd
URL:		https://metacpan.org/release/Term-Table
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
%if %{with tests}
BuildRequires:  perl-Test-Simple >= 1.302097
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Format a header and rows into a table. This is used by some failing
tests to provide diagnostics about what has gone wrong. This module is
able to generic format rows of data into tables.

%description -l pl.UTF-8
Formatowanie nagłówka i wierszy w tabelę. Jest to używane przez
niektóre testy do dostarczenia informacji diagnostycznych, co poszło
nie tak w przypadku niepowodzenia. Ten moduł potrafi ogólnie
formatować wiersze danych w tabele.

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
%{perl_vendorlib}/Term/Table.pm
%{perl_vendorlib}/Term/Table
%{_mandir}/man3/Term::Table*.3pm*
