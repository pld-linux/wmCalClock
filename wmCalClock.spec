Summary:	wmCalClock - a simple Calendar Clock
Summary(pl):	wmCalClock - prosty zegar z kalendarzem
Name:		wmCalClock
Version:	1.22 
Release:	1
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Copyright:      GPL
Source:		ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.bz2
BuildRoot: 	/tmp/%{name}-%{version}-root

%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep dock. 

%description -l pl
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa. 

%prep
%setup -q

%build
make -C wmCalClock 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install  wmCalClock/wmCalClock $RPM_BUILD_ROOT/usr/X11R6/bin
install  wmCalClock/wmCalClock.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

gzip -9nf BUGS CHANGES HINTS README TODO
gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/wmCalClock.1

%files
%defattr(644,root,root,755)
%doc BUGS.gz CHANGES.gz HINTS.gz README.gz TODO.gz
%attr(755,root,root) /usr/X11R6/bin/wmCalClock
/usr/X11R6/man/man1/wmCalClock.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 18 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.22-1]
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
