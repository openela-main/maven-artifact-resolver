Name:           maven-artifact-resolver
Version:        1.0
Release:        18%{?dist}
# Epoch is added because the original package's version in maven-shared is 1.1-SNAPSHOT
Epoch:          1
Summary:        Maven Artifact Resolution API
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
BuildArch:      noarch

Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Replaced plexus-maven-plugin with plexus-component-metadata
Patch0:         %{name}-plexus.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.easymock:easymock)

%description
Provides a component for plugins to easily resolve project dependencies.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%pom_xpath_inject pom:project/pom:dependencies "
<dependency>
  <groupId>org.apache.maven</groupId>
  <artifactId>maven-compat</artifactId>
  <version>1.0</version>
</dependency>" pom.xml

# Incompatible method invocation
rm src/test/java/org/apache/maven/shared/artifact/resolver/DefaultProjectDependenciesResolverIT.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0-15
- Add missing build-requires
- Remove old obsoletes/provides

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0-12
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.0-10
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Michal Srb <msrb@redhat.com> - 1:1.0-9
- Adapt to current guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.0-7
- Add maven-shared to BR/R
- Add few other missing BRs

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Sep 14 2012 Tomas Radej <tradej@redhat.com> - 1:1.0-4
- Installing folders separately with -m 755
- Installing NOTICE in javadoc subpackage
- Fixed changelog

* Wed Sep 12 2012 Tomas Radej <tradej@redhat.com> - 1:1.0-3
- Really fixed Provides/Obsoletes by introducing epoch

* Thu Sep 06 2012 Tomas Radej <tradej@redhat.com> - 1.0-2
- Fixed Provides/Obsoletes

* Tue Jul 31 2012 Tomas Radej <tradej@redhat.com> - 1.0-1
- Initial version
