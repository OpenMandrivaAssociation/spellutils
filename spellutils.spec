%define name spellutils
%define version 0.7

Summary: Programs for helping spell checking
Name: %{name}
Version: %{version}
Release: 22
Source0: http://home.worldonline.dk/byrial/spellutils/%{name}-%{version}.tar.bz2
License: GPL
URL: http://home.worldonline.dk/byrial/spellutils/
Group: Text tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-12mdv2011.0
+ Revision: 670009
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-11mdv2011.0
+ Revision: 607556
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-10mdv2010.1
+ Revision: 524119
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7-9mdv2010.0
+ Revision: 427208
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7-8mdv2009.0
+ Revision: 225471
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7-7mdv2008.1
+ Revision: 179518
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7-6mdv2008.0
+ Revision: 74770
- Import spellutils



* Sat May 27 2006 Stefan van der Eijk <stefan@eijk.nu> 0.7-6mdk
- %%mkrel
- fix URL

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.7-5mdk
- Rebuild

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.7-4mdk
- rebuild
- drop Prefix tag and redundant buildrequires

* Sat Jan 19 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 0.7-3mdk
- rebuild
- use %%configure2_5x, %%makeinstall_std macros
- s/Copyright/License/
- Provides: pospell (rpmlint)
- Requires: common-licenses
- add %%docs
- BuildRequires: gcc

* Fri Sep 22 2000 Alexander Skwar <ASkwar@DigitalProjects.com> 0.7-2mdk
- Rebuild to have man pages in %%{_mandir}
- Quietted setup

* Fri Jul 07 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.7-1mdk
- updated and changed the package name

* Fri Apr 14 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.4-1mdk
- updated to 0.4 that corrects some bugs

* Tue Apr 11 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.3-1mdk
- updated to 0.3
- made %%files section work with non compressed man pages

* Sun Apr 09 2000 Troels Liebe Bentsen <tlb@iname.com> 0.1-1mdk
- First spec file for Mandrake distribution.

# end of file
