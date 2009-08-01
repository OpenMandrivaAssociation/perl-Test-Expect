%define upstream_name    Test-Expect
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Automated driving and testing of terminal-based programs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Expect::Simple)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Class::Accessor::Chained)
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Test::Expect is a module for automated driving and testing of terminal-based
programs. It is handy for testing interactive programs which have a prompt, and
is based on the same concepts as the Tcl Expect tool.

Test::Expect is intended for use in a test script.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
