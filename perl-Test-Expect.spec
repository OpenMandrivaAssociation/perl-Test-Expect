%define realname   Test-Expect

Name:		perl-%{realname}
Version:	0.31
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Automated driving and testing of terminal-based programs
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl(Expect::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Class::Accessor::Chained)
BuildArch:      noarch

%description
Test::Expect is a module for automated driving and testing of terminal-based
programs. It is handy for testing interactive programs which have a prompt, and
is based on the same concepts as the Tcl Expect tool.

Test::Expect is intended for use in a test script.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Build.PL INSTALLDIRS=vendor

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=%buildroot installdirs=vendor
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

