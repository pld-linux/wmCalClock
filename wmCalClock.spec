Summary:	wmCalClock - a simple Calendar Clock
Summary(pl.UTF-8):   wmCalClock - prosty zegar z kalendarzem
Name:		wmCalClock
Version:	1.25
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	a401ded0e1fee4bcc4623076159bca41
Source1:	%{name}.desktop
Patch0:		%{name}-locale.patch.gz
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmCalClock is a simple Calendar Clock for the WindowMaker/AfterStep
dock.

%description -l pl.UTF-8
wmCalClock jest prostym, dokowalnym zegarem z kalendarzem dla
WindowMakera/AfterStepa.

%prep
%setup -q

%patch0 -p0

%build
%{__make} -C Src \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmCalClock.desktop
