Summary:	wmCalClock - a simple Calendar Clock
Summary(pl):	wmCalClock - prosty zegar z kalendarzem
Name:		wmCalClock
Version:	1.22 
Release:	3
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:      GPL
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.bz2
Source1:	wmCalClock.wmconfig
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define	_prefix		/usr/X11R6

%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep dock. 

%description -l pl
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa. 

%prep
%setup -q

%build
make -C %{name} \
	CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1


install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

gzip -9nf BUGS CHANGES HINTS README TODO \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
/etc/X11/wmconfig/%{name}

%changelog
* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.22-3]
- added using more rpm macros.

* Wed May 12 1999 Piotr Czerwiñski <pius@pld.org.pl>
- added "BuildPrereq: xpm-devel",
- package is now FHS 2.0 compliant.

* Thu Apr 22 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.22-2]
- fixed installing wmconfig file,
- removed %config from /etc/X11/wmconfig/wmCalClock.

* Tue Apr 20 1999 Piotr Czerwiñski <pius@pld.org.pl>
- added BuildPrereq: XFree86-devel,
- recompiled on rpm 3,
- cosmetics.

* Fri Mar 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.22-1]
- simplifications in %install,
- added using $RPM_OPT_FLAGS during compile,
- changed Group to X11/Window Managers/Tools.

* Tue Mar 18 1999 Piotr Czerwiñski <pius@pld.org.pl>
- upgraded to 1.22,
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- added pl translation,
- added -q %setup parameter,
- added gzipping documentation and man pages,
- removed INSTALL and COPYING from %doc,
- rewritten %build and %install sections,
- added %attr macro and fixed %defattr description in %files,
- cosmetic changes.

* Tue Feb  9 1999 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
