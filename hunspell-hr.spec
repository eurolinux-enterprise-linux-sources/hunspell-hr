Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%define upstreamid 20040608
Version: 0.%{upstreamid}
Release: 10%{?dist}
Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
Group: Applications/Text
URL: http://cvs.linux.hr/spell/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPLv2+ or SISSL
BuildArch: noarch

Requires: hunspell

%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Requires: hyphen
Summary: Croatian hyphenation rules
Group: Applications/Text

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hr_HR.txt
%{_datadir}/myspell/*

%files -n hyphen-hr
%doc README_hr_HR.txt
%defattr(-,root,root,-)
%{_datadir}/hyphen/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.20040608-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Caolán McNamara <caolanm@redhat.com> - 1:0.20040608-5
- add licence notice to all subpackages

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 22 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.20040608-2
- package hyphenation rules

* Tue Aug 21 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.20040608-1
- clarify license
- canonical upstream version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20060607-1
- initial version
