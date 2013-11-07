%define debug_package %{nil}

Name:           lorax
Version:        19.5
Release:        1.2%{?dist}
Summary:        Tool for creating the anaconda install images

Group:          Applications/System
License:        GPLv2+
URL:            http://git.fedorahosted.org/git/?p=lorax.git
Source0:        https://fedorahosted.org/releases/l/o/%{name}/%{name}-%{version}.tar.gz
Patch0:		lorax-19.5-install-releases-packages.patch
Patch2:		lorax-18.29-read-from-rfremix-release.patch

BuildRequires:  python2-devel

Requires:       GConf2
Requires:       cpio
Requires:       device-mapper
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       findutils
Requires:       gawk
Requires:       genisoimage
Requires:       glib2
Requires:       glibc
Requires:       glibc-common
Requires:       gzip
Requires:       isomd5sum
Requires:       libselinux-python
Requires:       module-init-tools
Requires:       parted
Requires:       python-mako
Requires:       squashfs-tools >= 4.2
Requires:       util-linux
Requires:       xz
Requires:       yum
Requires:       pykickstart

%if 0%{?fedora}
# Fedora specific deps
Requires:       fedup-dracut
Requires:       fedup-dracut-plymouth
%endif

%ifarch %{ix86} x86_64
Requires:       syslinux >= 4.02-5
%endif

%ifarch ppc ppc64
Requires:       kernel-bootwrapper
%endif

%ifarch s390 s390x
Requires:       openssh
%endif

%description
Lorax is a tool for creating the anaconda install images.

It also includes livemedia-creator which is used to create bootable livemedia,
including live isos and disk images. It can use libvirtd for the install, or
Anaconda's image install feature.

%prep
%setup -q
%patch0 -p1 -b .rfremix-repos
%patch1 -p1 -b .vpn
%patch2 -p1 -b .read-from-rfremix-release

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README.livemedia-creator
%{python_sitelib}/pylorax
%{python_sitelib}/*.egg-info
%{_sbindir}/lorax
%{_sbindir}/mkefiboot
%{_sbindir}/livemedia-creator
%dir %{_sysconfdir}/lorax
%config(noreplace) %{_sysconfdir}/lorax/lorax.conf
%dir %{_datadir}/lorax
%{_datadir}/lorax/*


%changelog
* Thu Nov  7 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.5-1.2.R
- drop vpn patch as it this functionality does not work in F19
  In F20 this looks like good
- hardcode 19 as release for repo-files

* Tue Nov  5 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.5-1.1.R
- install proper vpn packages

* Thu Jun 27 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.5-1.R
- update to 19.5

* Fri May 24 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.4-1.R
- update to 19.4

* Wed May 15 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.3-1.R
- update to 19.3

* Wed Apr 17 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.2-1.R
- update to 19.2

* Tue Apr  9 2013 Arkady L. Shane <ashejn@russianfedora.ru> 19.1-1.R
- update to 19.1

* Fri Jan 11 2013 Arkady L. Shane <ashejn@russianfedora.ru> 18.29-1.2.R
- read branding from rfremix-release

* Thu Jan  3 2013 Arkady L. Shane <ashejn@russianfedora.ru> 18.29-1.1.R
- added NetworkManager-l2tp

* Sun Dec 23 2012 Arkady L. Shane <ashejn@russianfedora.ru> 18.29-1.R
- update to 18.29

* Thu Dec 20 2012 Arkady L. Shane <ashejn@russianfedora.ru> 18.28-1.R
- update to 18.28
- drop shim patch
