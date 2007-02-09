#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	FuzzyOcr SpamAssassin plugin
Summary(pl):	Wtyczka FuzzyOcr dla SpamAssassina
Name:		spamassassin-plugin-fuzzyocr
Version:	3.5.1
Release:	0.4
License:	Apache Software License v2
Group:		Applications/Mail
Source0:	http://users.own-hero.net/~decoder/fuzzyocr/fuzzyocr-%{version}-devel.tar.gz
# Source0-md5:	14e04c4768f57a39a4953a837766f772
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
Requires:	netpbm-progs >= 10.34
Requires:	ocrad >= 0.14
Requires:	perl-Compress-Zlib
Requires:	perl-DBD-mysql
Requires:	perl-Digest-MD5
Requires:	perl-MLDBM-Sync
Requires:	perl-Mail-SpamAssassin >= 3.1.4
Requires:	perl-String-Approx
Requires:	perl-Tie-Cache
Requires:	perl-Time-HiRes
Requires:	tesseract
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

%description -l pl
FuzzyOcr to wtyczka SpamAssassina maj±ca wykrywaæ niezamówion± pocztê
masow± (znan± tak¿e jako "spam") zawieraj±c± obrazki jako g³ówny
no¶nik tre¶ci. Przy u¿yciu ró¿nych metod analizuje zawarto¶æ i
w³a¶ciwo¶ci obrazków w celu rozró¿nienia miêdzy zwyk³± poczt± ("ham")
a spamem.

G³ówne metody to:
- optyczne rozpoznawanie znaków (OCR) przy u¿yciu ró¿nych silników i
  ustawieñ
- algorytm przybli¿onego dopasowywania s³ów stosowany na wynikach OCR
- system haszowania obrazków w celu uczenia siê unikalnych w³a¶ciwo¶ci
  znanych obrazków ze spamem
- sprawdzanie wymiarów, rozmiaru i integralno¶ci obrazków
- weryfikacja Content-Type dla wiadomo¶ci z obrazkami

%prep
%setup -q -n FuzzyOcr-%{version}
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
