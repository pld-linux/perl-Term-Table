#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	pdir	Term
%define	pnam	Table
%include	/usr/lib/rpm/macros.perl
Summary:	Term::Table - Format a header and rows into a table
Name:		perl-Term-Table
Version:	0.012
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a38cad6182e2c4864752746f1035abbd
URL:		http://search.cpan.org/dist/Term-Table/
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
able to generic format rows of data into tables

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
