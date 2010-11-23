%define upstream_name    Crypt-Simple
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Encrypt stuff simply
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Crypt::Blowfish)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(FreezeThaw)
BuildRequires: perl(MIME::Base64)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Maybe you have a web application and you need to store some session data at
the client side (in a cookie or hidden form fields) but you don't want the
user to be able to mess with the data. Maybe you want to save secret
information to a text file. Maybe you have better ideas of what to do with
encrypted stuff!

This little module will convert all your data into nice base64 text that
you can save in a text file, send in an email, store in a cookie or web
page, or bounce around the Net. The data you encrypt can be as simple or as
complicated as you like.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


