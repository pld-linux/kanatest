Summary:	Kanatest - a simple hiragana and katakana drill tool
Summary(pl):	Kanatest - proste narzêdzie do æwiczenia hiragany i katakany
Name:		kanatest
Version:	0.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://clay.ll.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	0727789e69c227551c64ddde4570b495
URL:		http://clay.ll.pl/projects.html
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kanatest is a simple hiragana and katakana drill tool.

%description -l pl
Kanatest to proste narzêdzie do æwiczenia hiragany i katakany.

%prep
%setup -q

%build
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--datadir=/usr/share/games/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}/%{name}}

find data/ -name 'Makefile*' -exec rm {} \;
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/%{name}
install src/kanatest $RPM_BUILD_ROOT%{_bindir} 

#fix me
#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/kanatest
%{_datadir}/games/%{name}
