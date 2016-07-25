%global pkg_name jzlib
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1.1
Release:        6.5%{?dist}
Epoch:          0
Summary:        Re-implementation of zlib in pure Java
License:        BSD
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
Source0:        http://www.jcraft.com/jzlib/jzlib-%{version}.zip

BuildRequires:  %{?scl_prefix}maven-local

%description
The zlib is designed to be a free, general-purpose, legally unencumbered 
-- that is, not covered by any patents -- loss-less data-compression 
library for use on virtually any computer hardware and operating system. 
The zlib was written by Jean-loup Gailly (compression) and Mark Adler 
(decompression). 

%package        javadoc
Summary:        API documentation for %{pkg_name}

%description    javadoc
%{summary}.

%package        demo
Summary:        Examples for %{pkg_name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install

# examples
install -dm 755 %{buildroot}%{_datadir}/%{pkg_name}
cp -pr example/* %{buildroot}%{_datadir}/%{pkg_name}
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%doc %{_datadir}/%{pkg_name}

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-6.5
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-6.4
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-6.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-6.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-6.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.1.1-6
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.1-4
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.1.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jan 7 2013 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.1-1
- Update to latest upstream.

* Tue Oct 23 2012 Mat Booth <fedora@matbooth.co.uk> 0:1.1.0-3
- Add maven pom and depmap rhbz #806572.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.0-1
- Update to upstream 1.1.0 release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.7-8
- Fix merge review comments bug#225956.

* Wed Apr 7 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.7-7.4
- Drop gcj_support.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.7-6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0.7-5.3
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0.7-5jpp.2
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0.7-5jpp.1
- Autorebuild for GCC 4.3

* Tue Aug 08 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-4jpp.1
- Re-sync with latest from JPP.
- Partially adopt new naming convention.

* Sat Jul 22 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-3jpp_2fc
- Rebuild.

* Sat Jul 22 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.0.7-3jpp_1fc
- Merge with latest version from JPP.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.0.5-2jpp_4fc
- Rebuilt

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:1.0.5-2jpp_3fc
- rebuild

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:1.0.5-2jpp_2fc
- stop the scriptlet spew

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Mar 18 2005 Andrew Overholt <overholt@redhat.com> 1.0.5-2jpp_1fc
- Build into Fedora.
- Remove Distribution and Vendor tags.

* Tue Oct 19 2004 David Walluck <david@jpackage.org> 0:1.0.5-2jpp
- rebuild with jdk 1.4.2

* Tue Oct 19 2004 David Walluck <david@jpackage.org> 0:1.0.5-1jpp
- 0.1.5

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0.3-2jpp
- Rebuild with ant-1.6.2

* Wed Jan 14 2004 Ralph Apel <r.apel@r-apel.de> - 0:1.0.3-1jpp
- First build.
