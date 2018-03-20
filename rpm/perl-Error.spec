Name:       perl-Error

Summary:    Error/exception handling in an OO-ish way
Version:    0
Release:    1
Group:      Development/Libraries
License:    GPL+ or Artistic
BuildArch:  noarch
URL:        http://search.cpan.org/dist/Error/
Source0:    %{name}-%{version}.tar.gz
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
The Error package provides two interfaces. Firstly Error provides a
procedural interface to exception handling. Secondly Error is a base class
for errors/exceptions that can either be thrown, for subsequent catch, or
can simply be recorded.


%prep
%setup -q -n %{name}-%{version}/module

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?jobs:-j%jobs}
else
%{__perl} Build.PL  --installdirs vendor
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs vendor
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%defattr(-,root,root,-)
%doc ChangeLog README examples/
%{perl_vendorlib}/*
%doc %{_mandir}/man3/*
