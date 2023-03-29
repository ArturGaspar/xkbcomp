Name:       xkbcomp
Version:    1.4.7
Release:    1%{?dist}
Summary:    XKB keyboard description compiler
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/app/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  byacc
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
The X Keyboard Extension essentially replaces the core protocol definition of
keyboard. The extension makes possible to clearly and explicitly specify most
aspects of keyboard behaviour on per-key basis and to more closely track the
logical and physical state of the keyboard. It also includes a number of
keyboard controls designed to make keyboards more accessible to people with
physical impairments.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}

%files devel
%license COPYING
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%{_mandir}/man1/%{name}.1*
