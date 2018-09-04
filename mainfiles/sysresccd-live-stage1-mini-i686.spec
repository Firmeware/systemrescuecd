subarch: i686
version_stamp: mini
target: livecd-stage1
rel_type: default
profile: default/linux/x86/17.0
snapshot: 20180901
source_subpath: default/stage4-i686-baseos
portage_confdir: /worksrc/sysresccd-src/portage-etc-x86
portage_overlay: /worksrc/sysresccd-src/portage-overlay

livecd/use: python sysrcdfull X consolekit icu gtk gtk2 -svg -opengl -glx -berkdb -gdbm -minimal -introspection dri fbcon ipv6 livecd ncurses pam readline ssl unicode zlib nptl nptlonly multilib multislot jfs ntfs reiserfs xfs fat reiser4 samba png jpeg xorg usb pdf acl nologin atm bash-completion slang -kdrive vram loop-aes crypt device-mapper 7zip xattr bzip2 server lzo lz4 xz zstd xcb xkb xpm bash-completion -fam -doc -hardened -spoof-source -static -tcpd -mailwrapper -milter -nls -selinux -ermt -pic -dar32 -dar64 -openct -pcsc-lite -smartcard -caps -qt3 -qt4 -aqua -cscope -gnome -gpm -motif -netbeans -nextaw -perl -ruby -xterm -emacs -justify -spell -vim-pager -vim-with-x -sqlite -afs -bashlogger -plugins -vanilla -examples -maildir pcre pcre16 pcre32 -accessibility -ithreads -perlsuid -php -pike -tcl -tk -nocxx -no-net2 -kerberos -sse2 -aio -cups -ldap -quotas -swat -syslog -winbind -socks5 -guile -X509 dbus -gnutls -gsm -cracklib -nousuid -skey -old-linux -pxeserial -multitarget -test -clvm -cman -gulm -gd -glibc-compat20 -glibc-omitfp -bidi -xinerama -qt3support -alsa nfsv4 -gallium -fortran

livecd/packages:
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/mcelog
	app-admin/passook
	app-admin/procinfo-ng
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-admin/sysstat
	app-admin/testdisk
	app-arch/afio
	app-arch/arj
	app-arch/bzip2
	app-arch/cabextract
	app-arch/cfv
	app-arch/cpio
	app-arch/dump
	app-arch/gzip
	app-arch/lbzip2
	app-arch/lrzip
	app-arch/lz4
	app-arch/lzip
	app-arch/lzop
	app-arch/mt-st
	app-arch/ncompress
	app-arch/p7zip
	app-arch/par2cmdline
	app-arch/pbzip2
	app-arch/pigz
	app-arch/pixz
	app-arch/pxz
	app-arch/rzip
	app-arch/sharutils
	app-arch/star
	app-arch/tar
	app-arch/unace
	app-arch/unrar
	app-arch/unshield
	app-arch/unzip
	app-arch/xz-utils
	app-arch/zip
	app-arch/zstd
	app-backup/bacula
	app-backup/borgbackup
	app-backup/dar
	app-backup/fsarchiver
	app-backup/rsnapshot
	app-backup/tob
	app-benchmarks/bonnie++
	app-benchmarks/cpuburn
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/systester
	app-cdr/dvd+rw-tools
	app-crypt/chntpw
	app-crypt/md5deep
	app-editors/hexcurse
	app-editors/hexedit
	app-editors/joe
	app-editors/nano
	app-editors/qemacs
	app-editors/vim
	app-editors/vim-core
	app-editors/zile
	app-emulation/open-vm-tools
	app-forensics/afflib
	app-forensics/chkrootkit
	app-forensics/cmospwd
	app-forensics/foremost
	app-forensics/magicrescue
	app-misc/beep
	app-misc/colordiff
	app-misc/fdupes
	app-misc/livecd-tools
	app-misc/mc
	app-misc/screen
	app-misc/scrub
	app-misc/symlinks
	app-misc/tmux
	app-misc/vlock
	app-misc/wipe
	app-portage/eix
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/portage-utils
	app-shells/bash
	app-shells/ksh
	app-shells/tcsh
	app-shells/zsh
	app-text/dos2unix
	app-text/tree
	app-text/wgetpaste
	app-vim/gentoo-syntax
	dev-lang/perl
	dev-libs/expat
	dev-libs/libconfig
	dev-libs/libdnet
	dev-libs/libisoburn
	dev-libs/libusb
	dev-libs/lzo
	dev-libs/pkcs11-helper
	dev-libs/popt
	dev-scheme/guile
	dev-util/cmake
	dev-util/intltool
	dev-util/ltrace
	dev-util/patchutils
	dev-util/pkgconfig
	dev-util/strace
	net-analyzer/dnstracer
	net-analyzer/httping
	net-analyzer/ifstat
	net-analyzer/iftop
	net-analyzer/iptraf-ng
	net-analyzer/macchanger
	net-analyzer/netcat
	net-analyzer/ngrep
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/vnstat
	net-dialup/mingetty
	net-dialup/minicom
	net-dns/bind-tools
	net-vpn/ipsec-tools
	net-firewall/iptables
	net-fs/curlftpfs
	net-fs/nfs-utils
	net-fs/samba
	net-ftp/ftp
	net-ftp/lftp
	net-ftp/ncftp
	net-ftp/tftp-hpa
	net-misc/autossh
	net-misc/bridge-utils
	net-misc/dhcp
	net-misc/dhcpcd
	net-misc/ethercard-diag
	net-misc/ifenslave
	net-misc/iperf
	net-misc/iputils
	net-misc/netifrc
	net-misc/netkit-rsh
	net-misc/ntp
	net-misc/openssh
	net-vpn/openvpn
	net-misc/pssh
	net-misc/rdate
	net-misc/rsync
	net-misc/telnet-bsd
	net-misc/udpcast
	net-misc/vconfig
	net-vpn/vpnc
	net-misc/wget
	net-misc/whois
	net-misc/wput
	sys-apps/acl
	sys-apps/attr
	sys-apps/cciss_vol_status
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/dmapi
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/ed
	sys-apps/ethtool
	sys-apps/fbset
	sys-apps/file
	sys-apps/findutils
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/hdparm
	sys-apps/hwids
	sys-apps/ipmitool
	sys-apps/iproute2
	sys-apps/kbd
	sys-apps/lm_sensors
	sys-apps/lshw
	sys-apps/man
	sys-apps/man-pages
	sys-apps/memtester
	sys-apps/miscfiles
	sys-apps/mlocate
	sys-apps/netplug
	sys-apps/net-tools
	sys-apps/nvme-cli
	sys-apps/openrc
	sys-apps/pv
	sys-apps/rename
	sys-apps/renameutils
	sys-apps/rescan-scsi-bus
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
	sys-apps/shadow
	sys-apps/smartmontools
	sys-apps/sysresccd-custom
	sys-apps/tcp-wrappers
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/which
	sys-apps/x86info
	sys-auth/pambase
	sys-block/aic94xx-firmware
	sys-block/gpart
	sys-block/mbuffer
	sys-block/mpt-status
	sys-block/ms-sys
	sys-block/mtx
	sys-block/nbd
	sys-block/parted
	sys-block/partimage
	sys-block/scsiadd
	sys-block/whdd
	sys-boot/efibootmgr
	sys-boot/grub
	sys-boot/lilo
	sys-boot/mbr
	sys-boot/os-prober
	sys-boot/syslinux
	sys-cluster/drbd-utils
	sys-devel/autogen
	sys-devel/bc
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dd-rescue
	sys-fs/diskdev_cmds
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/ext3grep
	sys-fs/extundelete
	sys-fs/growpart
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lufis
	sys-fs/lufs
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/mtd-utils
	sys-fs/multipath-tools
	sys-fs/ncdu
	sys-fs/ntfs3g
	sys-fs/ntfsreloc
	sys-fs/reiser4progs
	sys-fs/reiserfsprogs
	sys-fs/safecopy
	sys-fs/scrounge-ntfs
	sys-fs/squashfs-tools
	net-fs/sshfs
	sys-fs/eudev
	sys-fs/udftools
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-fs/zerofree
	sys-kernel/gentoo-sources
	sys-kernel/linux-firmware
	sys-libs/libstdc++-v3
	sys-libs/openipmi
	sys-libs/pam
	sys-libs/pwdb
	sys-libs/readline
	sys-libs/zlib
	sys-power/acpi
	sys-process/atop
	sys-process/cronbase
	sys-process/htop
	sys-process/iotop
	sys-process/lsof
	sys-process/nmon
	sys-process/procps
	sys-process/psmisc
	sys-process/vixie-cron
	www-client/elinks
	www-servers/thttpd

