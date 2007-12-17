%define name spellutils
%define version 0.7
%define release %mkrel 6

Summary: Programs for helping spell checking
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://home.worldonline.dk/byrial/spellutils/%{name}-%{version}.tar.bz2
License: GPL
URL: http://home.worldonline.dk/byrial/spellutils/
Group: Text tools
Obsoletes: pospell
Provides: pospell
Requires: common-licenses

%description
Spellutils is a suite of programs which are used to isolate some parts
or texts from various types of files and hand them over to another
program which may change the texts; it is typically a spell checker.
Afterwards the possibly changed text parts are copied back in place in the
original file.

The programs in the Spellutils package are:

* newsbody which can isolate your own text from headers, quotes and
  signature in e-mail or Usenet messages
* pospell which can isolate translations in .po files
* More programs are likely to follow

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README FILES NEWS
%{_mandir}/man1/*
%{_bindir}/*