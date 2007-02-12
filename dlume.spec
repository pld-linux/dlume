Summary:	Handy and easy to use addressbook
Summary(pl.UTF-8):   Poręczna i łatwa w użyciu książka adresowa
Name:		dlume
Version:	0.2.4
Release:	1.1
License:	GPL
Group:		X11/Applications
Source0:	http://clay.ll.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	6b2a3ef0eff622a412395187d1c5d178
Source1:	%{name}.desktop
URL:		http://clay.ll.pl/dlume.html
#BuildRequires:	ImageMagick
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dlume is nice, gtk2-based addressbook. You can easily add, edit and
delete records to/from database (but Dlume doesn't rely on an outside
database - It stores your contacts in XML format). The Quick-search
feature allows you find required entry in comfortable way. Export to
CSV and HTML formats is also available.

%description -l pl.UTF-8
Dlume to ładna książka adresowa oparta o gtk2. W łatwy sposób można
dodawać, modyfikować i usuwać rekordy z bazy (Dlume nie korzysta z
zewnętrznej bazy - przechowuje kontakty w formacie XML). Szybkie
wyszukiwanie umożliwia w łatwy sposób znalezienie pożądanej pozycji.
Możliwy jest eksport do CSV i HTML.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1}  $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
