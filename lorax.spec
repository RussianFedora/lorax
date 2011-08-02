%define debug_package %{nil}

Name:           lorax
Version:        0.4.6
Release:        2%{?dist}.R
Summary:        Tool for creating the anaconda install images

Group:          Applications/System
License:        GPLv2+
URL:            http://git.fedorahosted.org/git/?p=lorax.git
Source0:        https://fedorahosted.org/releases/l/o/%{name}/%{name}-%{version}.tar.bz2
Patch0:         lorax-0.3.2-rfremix-install-tree.patch
Patch1:         lorax-0.4.6-install-vpn-and-sysvinit-tools.patch

BuildRequires:  python2-devel
Requires:       python-mako
Requires:       gawk
Requires:       glibc-common
Requires:       cpio
Requires:       module-init-tools
Requires:       device-mapper
Requires:       findutils
Requires:       GConf2
Requires:       isomd5sum
Requires:       glibc
Requires:       util-linux-ng
Requires:       dosfstools
Requires:       genisoimage
Requires:       parted
Requires:       pyliblzma

%ifarch %{ix86} x86_64
Requires:       syslinux
%endif

%ifarch %{sparc}
Requires:       silo
%endif

%description
Lorax is a tool for creating the anaconda install images.

%prep
%setup -q
%patch0 -p1 -b .rfremix-install-tree
%patch1 -p1 -b .install-vpn-and-sysvinit-tools

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
* Tue Aug  2 2011 Arkady L. Shane <ashejn@russianfedora.ru> 0.4.6-2.R
- also install sysvinit-tools
- drop lorax-0.4.6-do-not-remove-some-NM-files.patch

* Mon Aug  1 2011 Arkady L. Shane <ashejn@russianfedora.ru> 0.4.6-1.4.R
- do not remove some ModemManager files too

* Mon Aug  1 2011 Arkady L. Shane <ashejn@russianfedora.ru> 0.4.6-1.3.R
- do not remove some NetworkManager files

* Thu May 19 2011 Arkady L. Shane <ashejn@russianfedora.ru> 0.4.6-1.2.R
- fix group in lxde kickstart

* Thu May 12 2011 Arkady L. Shane <ashejn@russianfedora.ru> 0.4.6-1.1.R
- added NM-vpn packages to anaconda image
- added kickstart files to anaconda image

* Tue May 10 2011 Martin Gracik <mgracik@redhat.com> 0.4.6-1
- Do not remove libmodman (#701622)
- Add firmware for Intel Wireless WiFi Link 6030 Adapters (#703291)

* Tue May 03 2011 Martin Gracik <mgracik@redhat.com> 0.4.5-1
- Disable debuginfo package
- Do not remove libproxy (#701622)

* Mon May 02 2011 Martin Gracik <mgracik@redhat.com> 0.4.4-1
- Disable rsyslogd rate limiting on imuxsock.
- Add the udf module to the image.

* Tue Apr 19 2011 Martin Gracik <mgracik@redhat.com> 0.4.3-1
- bits is an integer and replace needs arguments to be strings (#697542)
- Use arch macros in the lorax.spec
- use reqs not regs for files to backup (dgilmore)
- Reflect changes made in ntfs-3g and ntfsprogs packages (#696706)
- getkeymaps resides in /usr/libexec/anaconda
- workdir is a local variable, not a class attribute
- Add sparcv9 to arch map
- Change the location of *.b files on sparc

* Wed Apr 13 2011 Martin Gracik <mgracik@redhat.com> 0.4.2-1
- Do not remove shutdown from sbin
- Change BuildRequires to python2-devel
- Remove pungi patch
- Remove pseudo code

* Wed Apr 13 2011 Martin Gracik <mgracik@redhat.com> 0.4.1-1
- Provide shutdown on s390x (#694518)
- Fix arch specific requires in spec file
- Add s390 modules and do some cleanup of the template
- Generate ssh keys on s390
- Don't remove tr, needed for s390
- Do not check if we have all commands
- Change location of addrsize and mk-s390-cdboot
- Shutdown is in another location
- Do not skip broken packages
- Don't install network-manager-netbook
- Wait for subprocess to finish
- Have to call os.makedirs
- images dir already exists, we just need to set it
- The biarch is a function not an attribute
- Create images directory in outputtree
- Create efibootdir if doing efi images
- Get rid of create_gconf().
- Replace variables in yaboot.conf
- Add sparc specific packages
- Skip keymap creation on s390
- Copy shutdown and linuxrc.s390 on s390
- Add packages for s390
- Add support for sparc
- Use factory to get the image classes
- treeinfo has to be addressed as self.treeinfo
- Add support for s390
- Add the xen section to treeinfo on x86_64
- Fix magic and mapping paths
- Fix passing of prepboot and macboot arguments
- Small ppc fixes
- Check if the file we want to remove exists
- Install x86 specific packages only on x86
- Change the location of zImage.lds
- Added ppc specific packages
- memtest and efika.forth are in /boot
- Add support for ppc
- Minor sparc pseudo code changes
- Added sparc pseudo code (dgilmore)
- Added s390 and x86 pseudo code
- Added ppc pseudo code
- Print a message when no arguments given (#684463)
- Mako template returns unicode strings (#681003)
- The check option in options causes ValueError
- Disable all ctrl-alt-arrow metacity shortcuts.
- Use xz when compressing the initrd

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
