Summary:	Latin2 encoding support for xpdf
Summary(pl):	Wsparcie kodowania Latin2 dla xpdf
Name:		xpdf-latin2
Version:	1.0
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
# Source0-md5:	ac19ef990cd63afd2837c10dc7e1c3ab
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Latin2 PDF files.

%description -l pl
Pakiety wspieraj±ce jêzyki Xpdf zawieraj± pliki CMap, kodowania oraz
ró¿ne inne informacje konfiguracyjne niezbêdne b±d¼ przydatne przy
okre¶lonych zestawach znaków. (Nie zawieraj± ¿adnych fontów).
Ten pakiet zawiera pliki potrzebne do u¿ywania narzêdzi Xpdf z plikami
PDF o kodowaniu Latin2.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	Latin2	/usr/share/xpdf/Latin2.unicodeMap' >> /etc/xpdfrc
else
 if ! grep -q 'Latin2\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	Latin2	/usr/share/xpdf/Latin2.unicodeMap' >> /etc/xpdfrc
 fi
fi

%preun
umask 022
grep -v 'Latin2\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
mv -f /etc/xpdfrc.new /etc/xpdfrc

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
