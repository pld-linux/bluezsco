%define		mainpkg_snap 2003-09-15
Summary:	Bluetooth headset controlling program
Summary(pl):	Program do kontroli zestawu sluchawkowego Bluetooth
Name:		bluezsco
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.dcs.gla.ac.uk/~jp/snd-bluez-sco/snd-bluez-sco-%{mainpkg_snap}.tar.gz
#Source0-MD5:	c7ef302f3fcae934eb3935267cf557c8
URL:		http://www.dcs.gla.ac.uk/~jp/snd-bluez-sco/
BuildRequires:	alsa-driver-devel
Requires:	kernel-sound-alsa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
empty


%prep
%setup -q -n snd-bluez-sco-%{mainpkg_snap}

%build
cd %{name}-%{version}

%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}
cp %{name}-%{version}/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
