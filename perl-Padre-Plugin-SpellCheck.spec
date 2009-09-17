%define upstream_name    Padre-Plugin-SpellCheck
%define upstream_version 1.1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Check spelling in Padre
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Padre)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Aspell)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


