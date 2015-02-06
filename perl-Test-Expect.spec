%define upstream_name    Test-Expect
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

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


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 664906
- mass rebuild

* Sat Aug 01 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.0
+ Revision: 406186
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.31-2mdv2009.0
+ Revision: 268733
- rebuild early 2009.0 package (before pixel changes)

* Sat May 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.0
+ Revision: 205398
- update to new version 0.31

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.30-3mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.30-3mdv2008.0
+ Revision: 23808
- rebuild


* Fri Apr 28 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.30-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Mar 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-1mdk
- 0.30

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.29-4mdk
- Do not ship empty dir

* Mon Oct 03 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.29-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.29-2mdk
- Buildrequires fix

* Sat Sep 24 2005 Michael Scherer <misc@mandriva.org> 0.29-1mdk
- First mandriva package

