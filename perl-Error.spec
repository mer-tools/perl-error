# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       perl-Error

# >> macros
# << macros

Summary:    Error/exception handling in an OO-ish way
Version:    0.17020
Release:    1
Group:      Development/Libraries
License:    GPL+ or Artistic
BuildArch:  noarch
URL:        http://search.cpan.org/dist/Error/
Source0:    http://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-%{version}.tar.gz
Source100:  perl-Error.yaml
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
%setup -q -n Error-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

if test -f Makefile.PL; then
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?jobs:-j%jobs}
else
%{__perl} Build.PL  --installdirs vendor
./Build
fi

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs vendor
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

# >> install post
# << install post

%check
# >> check
make test
# << check

%files
%defattr(-,root,root,-)
# >> files
%doc ChangeLog README examples/
%{perl_vendorlib}/*
%doc %{_mandir}/man3/*
# << files
