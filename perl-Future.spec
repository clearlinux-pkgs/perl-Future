#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Future
Version  : 0.40
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-0.40.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-0.40.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-async-perl/libio-async-perl_0.72-1.debian.tar.xz
Summary  : Perl module to deal with operation awaiting completion
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Future-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Refcount)

%description
NAME
Future - represent an operation awaiting completion
SYNOPSIS
my $future = Future->new;

perform_some_operation(
on_complete => sub {
$future->done( @_ );
}
);

$future->on_ready( sub {
say "The operation is complete";
} );

%package dev
Summary: dev components for the perl-Future package.
Group: Development
Provides: perl-Future-devel = %{version}-%{release}
Requires: perl-Future = %{version}-%{release}

%description dev
dev components for the perl-Future package.


%package license
Summary: license components for the perl-Future package.
Group: Default

%description license
license components for the perl-Future package.


%prep
%setup -q -n Future-0.40
cd ..
%setup -q -T -D -n Future-0.40 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Future-0.40/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Future
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Future/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Future.pm
/usr/lib/perl5/vendor_perl/5.28.2/Future/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.2/Future/Mutex.pm
/usr/lib/perl5/vendor_perl/5.28.2/Future/Phrasebook.pod
/usr/lib/perl5/vendor_perl/5.28.2/Future/Utils.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/Future.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/Future/Deferred.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Future.3
/usr/share/man/man3/Future::Exception.3
/usr/share/man/man3/Future::Mutex.3
/usr/share/man/man3/Future::Phrasebook.3
/usr/share/man/man3/Future::Utils.3
/usr/share/man/man3/Test::Future.3
/usr/share/man/man3/Test::Future::Deferred.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Future/deblicense_copyright
