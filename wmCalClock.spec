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
Patch:		wmCalClock-fhs.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep dock. 

%description -l pl
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa. 

%prep
%setup -q
%patch -p0

%build
make -C wmCalClock \
	CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,share/man/man1}}

make -C wmCalClock install DESTDIR=$RPM_BUILD_ROOT/usr/X11R6

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmCalClock

gzip -9nf BUGS CHANGES HINTS README TODO \
	$RPM_BUILD_ROOT/usr/X11R6/share/man/man1/wmCalClock.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,README,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/wmCalClock
/usr/X11R6/share/man/man1/wmCalClock.1.gz
/etc/X11/wmconfig/wmCalClock

%changelog
* Wed May 12 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.22-3]
- added wmCalClock-fhs.patch,
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
