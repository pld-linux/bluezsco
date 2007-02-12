%define		mainpkg_snap 2003-09-15
Summary:	Bluetooth headset controlling program
Summary(pl.UTF-8):	Program do kontroli zestawu słuchawkowego Bluetooth
Name:		bluezsco
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.dcs.gla.ac.uk/~jp/snd-bluez-sco/snd-bluez-sco-%{mainpkg_snap}.tar.gz
#Source0-MD5:	c7ef302f3fcae934eb3935267cf557c8
URL:		http://www.dcs.gla.ac.uk/~jp/snd-bluez-sco/
BuildRequires:	alsa-driver-devel >= 0.9.7a-2
BuildRequires:	alsa-lib-devel >= 0.9.7-2
BuildRequires:	bluez-libs-devel
Requires:	kernel-sound-alsa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bluezsco is a utility to control Bluetooth headset.

%description -l pl.UTF-8
bluezsco to narzędzie do sterowania zestawem słuchawkowym Bluetooth.

%prep
%setup -q -n snd-bluez-sco-%{mainpkg_snap}

%build
cd %{name}-%{version}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}-%{version}/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
