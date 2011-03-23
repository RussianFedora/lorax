Name:           lorax
Version:        0.3.2
Release:        1%{?dist}.3.R
Summary:        Tool for creating the anaconda install images

Group:          Applications/System
License:        GPLv2+
URL:            http://git.fedorahosted.org/git/?p=lorax.git
Source0:        https://fedorahosted.org/releases/l/o/%{name}/%{name}-%{version}.tar.bz2
Patch0:		lorax-0.3.2-rfremix-install-tree.patch
BuildArch:      noarch

BuildRequires:  python-setuptools
Requires:       python2-devel
Requires:       python-mako
Requires:       gawk
Requires:       glibc-common
Requires:       cpio
Requires:       module-init-tools
Requires:       device-mapper
Requires:       findutils
Requires:       GConf2
Requires:       isomd5sum
Requires:       syslinux
Requires:       glibc
Requires:       util-linux-ng
Requires:       dosfstools
Requires:       genisoimage
Requires:       parted

%description
Lorax is a tool for creating the anaconda install images.

%prep
%setup -q
%patch0 -p1 -b .rfremix-install-tree

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{python_sitelib}/pylorax
%{python_sitelib}/*.egg-info
%{_sbindir}/lorax
%dir %{_sysconfdir}/lorax
%config(noreplace) %{_sysconfdir}/lorax/lorax.conf
%dir %{_datadir}/lorax
%{_datadir}/lorax/*


%changelog
* Wed Mar 23 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.3.2-1.3.R
- added NM vpn plugins into image
- fix function name

* Wed Mar 23 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.3.2-1.2.R
- fix release

* Wed Mar 23 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.3.2-1.R2
- fix import in rfrinstalltree.py

* Wed Mar 23 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.3.2-1.1
- create kickstarts
- create proper repo file

* Mon Mar 21 2011 Martin Gracik <mgracik@redhat.com> 0.3.2-1
- gconf/metacity: have only one workspace. (#683548)
- Do not remove libassuan. (#684742)
- Add yum-langpacks yum plugin to anaconda environment (notting) (#687866)

* Tue Mar 15 2011 Martin Gracik <mgracik@redhat.com> 0.3.1-1
- Add the images-xen section to treeinfo on x86_64
- Add /sbin to $PATH (for the tty2 terminal)
- Create /var/run/dbus directory in installtree
- Add mkdir support to template
- gpart is present only on i386 arch (#672611)
- util-linux-ng changed to util-linux

* Mon Jan 24 2011 Martin Gracik <mgracik@redhat.com> 0.3-1
- Don't remove libmount package
- Don't create mtab symlink, already exists
- Exit with error if we have no lang-table
- Fix file logging
- Overwrite the /etc/shadow file
- Use [images-xen] section for PAE and xen kernels

* Fri Jan 14 2011 Martin Gracik <mgracik@redhat.com> 0.2-2
- Fix the gnome themes
- Add biosdevname package
- Edit .bash_history file
- Add the initrd and kernel lines to .treeinfo
- Don't remove the gamin package from installtree

* Wed Dec 01 2010 Martin Gracik <mgracik@redhat.com> 0.1-1
- First packaging of the new lorax tool.
