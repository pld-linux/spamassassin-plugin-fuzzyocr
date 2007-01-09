Summary:	FuzzyOcr SpamAssassin plugin
Name:		spamassassin-plugin-fuzzyocr
Version:	2.3b
Release:	1
License:	Apache 2.0
Group:		Applications
Source0:	http://users.own-hero.net/~decoder/fuzzyocr/fuzzyocr-%{version}.tar.gz
# Source0-md5:	51edf3fa63a4438ce26b2fc15f28ff00
Patch0:		fuzzyocr-config.patch
URL:		http://fuzzyocr.own-hero.net/
Requires:	ImageMagick
Requires:	giflib-progs >= 4.1.4-4
Requires:	gifsicle
Requires:	gocr >= 0.43
Requires:	netpbm
Requires:	ocrad >= 0.14
Requires:	perl(Time::HiRes)
Requires:	perl-Digest-MD5
Requires:	perl-Mail-SpamAssassin >= 3.1.4
Requires:	perl-String-Approx
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

%prep
%setup -q -n FuzzyOcr-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_sysconfdir}}
cp -a FuzzyOcr.cf $RPM_BUILD_ROOT%{_sysconfdir}
cp -a FuzzyOcr.words.sample $RPM_BUILD_ROOT%{_sysconfdir}/FuzzyOcr.words
cp -a FuzzyOcr.pm $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ INSTALL samples
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.cf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/FuzzyOcr.words
%{perl_vendorlib}/FuzzyOcr.pm
