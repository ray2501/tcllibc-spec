%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:           tcllibc
Summary:        The parts of Tcllib written in C
Group:          Development/Libraries/Tcl
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl
BuildRequires:  tcllib
BuildRequires:  critcl
BuildRequires:  critcl-devel
Requires:       tcl 
Version:        2.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
License:        TCL
Source0:        tcllib-2.0.tar.xz
BuildRoot:      %{buildroot}

%description
Tcl Standard Library (Tcllib) is intended to be a collection
of Tcl packages that provide utility functions useful to a
large collection of Tcl programmers.

It is the parts of Tcllib written in C.

%prep
%setup -q -n tcllib-2.0

%build
autoconf
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make critcl

%install
mkdir -p %{buildroot}/%{tcl_archdir}/%{name}%{version}
cp -r modules/tcllibc/linux* %{buildroot}/%{tcl_archdir}/%{name}%{version}
cp -r modules/tcllibc/*.tcl %{buildroot}/%{tcl_archdir}/%{name}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}/%{name}%{version}

