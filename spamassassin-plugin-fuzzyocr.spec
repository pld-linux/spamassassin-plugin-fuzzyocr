#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	FuzzyOcr SpamAssassin plugin
Summary(pl.UTF-8):	Wtyczka FuzzyOcr dla SpamAssassina
Name:		spamassassin-plugin-fuzzyocr
Version:	3.5.1
%define		_snap	svn132
Release:	1.%{_snap}.1
License:	Apache Software License v2
Group:		Applications/Mail
#Source0:	http://users.own-hero.net/~decoder/fuzzyocr/fuzzyocr-%{version}-devel.tar.gz
Source0:	http://www.blues.gda.pl/SOURCES/fuzzyocr-%{version}-%{_snap}-devel.tar.bz2
# Source0-md5:	6b8c70ed9b72312f8c6cd522a3ebd0ab
Patch0:		fuzzyocr-config.patch
URL:		http://fuzzyocr.own-hero.net/
BuildRequires:	sed >= 4.0
%if %{with autodeps}
BuildRequires:	perl-DBI
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MLDBM
BuildRequires:	perl-MLDBM-Sync
BuildRequires:	perl-Mail-SpamAssassin >= 3.1.4
BuildRequires:	perl-String-Approx
BuildRequires:	perl-Time-HiRes
%endif
Requires:	ImageMagick
Requires:	giflib-progs >= 4.1.4-4
Requires:	gifsicle
Requires:	gocr >= 0.43
Requires:	netpbm-progs >= 10.34-4
Requires:	netpbm-progs-pstopnm >= 10.34-4
Requires:	ocrad >= 0.14
Requires:	perl-Compress-Zlib
Requires:	perl-DBD-mysql
Requires:	perl-Digest-MD5
Requires:	perl-MLDBM-Sync
Requires:	perl-Mail-SpamAssassin >= 3.1.4
Requires:	perl-String-Approx
Requires:	perl-Tie-Cache
Requires:	perl-Time-HiRes
# It's optional, disabled by default:
Suggests:	tesseract
# For pdf-processing:
Suggests:	poppler-progs
# Has problems with some pdfs:
Conflicts:	xpdf-tools
# Requred anyway, but maybe it should be suggests only?
#Suggests:	netpbm-progs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/mail/spamassassin

%description
FuzzyOcr is a plugin for SpamAssassin which is aimed at unsolicited
bulk mail (also known as "Spam") containing images as the main content
carrier. Using different methods, it analyzes the content and
properties of images to distinguish between normal mails (Ham) and
spam mails.

The methods mainly are:
- Optical Character Recognition using different engines and settings
- Fuzzy word matching algorithm applied to OCR results
- Image hashing system to learn unique properties of known spam images
- Dimension, size and integrity checking of images
- Content-Type verification for the containing email

%description -l pl.UTF-8
FuzzyOcr to wtyczka SpamAssassina mająca wykrywać niezamówioną pocztę
masową (znaną także jako "spam") zawierającą obrazki jako główny
nośnik treści. Przy użyciu różnych metod analizuje zawartość i
właściwości obrazków w celu rozróżnienia między zwykłą pocztą ("ham")
a spamem.

Główne metody to:
- optyczne rozpoznawanie znaków (OCR) przy użyciu różnych silników i
  ustawień
- algorytm przybliżonego dopasowywania słów stosowany na wynikach OCR
- system haszowania obrazków w celu uczenia się unikalnych właściwości
  znanych obrazków ze spamem
- sprawdzanie wymiarów, rozmiaru i integralności obrazków
- weryfikacja Content-Type dla wiadomości z obrazkami

%prep
%setup -q -n FuzzyOCR-%{version}
%patch0 -p1
%{__sed} -i -e '1s,#!.*perl,#!%{__perl},' Utils/fuzzy-*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_sysconfdir},%{_bindir}}
cp -a FuzzyOcr.words FuzzyOcr.cf FuzzyOcr.scansets FuzzyOcr.preps $RPM_BUILD_ROOT%{_sysconfdir}
cp -a FuzzyOcr FuzzyOcr.pm $RPM_BUILD_ROOT%{perl_vendorlib}
install Utils/fuzzy-* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FuzzyOcr.mysql samples
%attr(755,root,root) %{_bindir}/fuzzy-cleantmp
%attr(755,root,root) %{_bindir}/fuzzy-find
%attr(755,root,root) %{_bindir}/fuzzy-stats
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.cf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.preps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.scansets
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.words
%{perl_vendorlib}/FuzzyOcr.pm
%{perl_vendorlib}/FuzzyOcr
