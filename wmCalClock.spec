Summary:	wmCalClock - a simple Calendar Clock
Summary(pl):	wmCalClock - prosty zegar z kalendarzem
Name:		wmCalClock
Version:	1.24
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:      GPL
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmCalClock.wmconfig
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep dock. 

%description -l pl
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa. 

%prep
%setup -q

%build
make -C Src \
	CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

install -s Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
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
* Mon May 24 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.24-1]
- updated to 1.24.

* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.22-3]
- package is FHS 2.0 compliant,
- based on spec file written by Ian Macdonald <ianmacd@xs4all.nl>,
  rewritten for PLD use by me and Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>.
