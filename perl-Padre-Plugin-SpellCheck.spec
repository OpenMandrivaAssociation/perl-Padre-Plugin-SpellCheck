%define upstream_name    Padre-Plugin-SpellCheck
%define upstream_version 1.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Check spelling in Padre
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-SpellCheck-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Padre)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Aspell)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: x11-server-xvfb
BuildArch:	noarch

%description
This plugins allows one to checking her text spelling within Padre using
'F7' (standard spelling shortcut accross text processors). One can change
the dictionary language used in the preferences window (menu Plugins /
SpellCheck / Preferences).

This plugin is using 'Text::Aspell' underneath, so check this module's pod
for more information.

Of course, you need to have the aspell binary and dictionnary installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.210.0-2mdv2011.0
+ Revision: 657816
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 622998
- new version

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 443969
- import perl-Padre-Plugin-SpellCheck


* Thu Sep 17 2009 cpan2dist 1.1.2-1mdv
- initial mdv release, generated with cpan2dist

