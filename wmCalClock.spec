Summary:	wmCalClock - a simple Calendar Clock
Summary(pl):	wmCalClock - prosty zegar z kalendarzem
Name:		wmCalClock
Version:	1.25
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep
dock.

%description -l pl
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa.

%prep
%setup -q

%build
%{__make} -C Src \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
#%%{_applnkdir}/DockApplets/wmCalClock.desktop
