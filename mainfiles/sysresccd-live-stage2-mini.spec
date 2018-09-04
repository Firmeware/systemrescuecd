subarch: i686
version_stamp: mini
target: livecd-stage2
rel_type: default
profile: default/linux/x86/17.0
snapshot: 20180901
source_subpath: default/livecd-stage1-i686-mini
portage_confdir: /worksrc/sysresccd-src/portage-etc-x86
portage_overlay: /worksrc/sysresccd-src/portage-overlay

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.72-cdtar.tar.bz2
livecd/iso: /worksrc/isofiles/systemrescuecd-x86-current.iso
livecd/fsscript: /worksrc/sysresccd-src/mainfiles/fsscript-livecd.sh
livecd/splash_type:
livecd/splash_theme:
livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts="-j5"
livecd/type: generic-livecd
livecd/readme:
livecd/motd:
livecd/modblacklist:
livecd/root_overlay: /worksrc/sysresccd-src/overlay-squashfs-x86 /worksrc/sysresccd-bin/overlay-squashfs-x86
livecd/users:
livecd/volid: sysresccd

boot/kernel: rescuecd

boot/kernel/rescuecd/sources: sys-kernel/std-sources
boot/kernel/rescuecd/config: /worksrc/sysresccd-src/kernelcfg/config-fake-i686.cfg
boot/kernel/rescuecd/use: pcmcia usb -X png truetype 
boot/kernel/rescuecd/extraversion: i686
boot/kernel/rescuecd/packages:
	sys-apps/sysresccd-scripts
	sys-kernel/linux-firmware
	sys-block/open-iscsi
	sys-fs/nilfs-utils
	sys-fs/aufs3

livecd/unmerge:
	app-admin/eselect-opengl
	app-admin/perl-cleaner
	sys-devel/bison
	sys-devel/flex
	sys-power/iasl
	sys-kernel/gentoo-sources
	sys-kernel/alt-sources
	sys-kernel/std-sources
	dev-lang/nasm
	dev-lang/yasm
	dev-util/yacc
	dev-util/gtk-doc
	dev-util/scons
	dev-util/ccache
	dev-util/ctags
	dev-util/intltool
	sys-apps/help2man
	sys-apps/miscfiles
	sys-apps/busybox
	sys-apps/texinfo
	sys-fs/progsreiserfs
	dev-python/pycrypto
	dev-python/python-fchksum
	media-fonts/font-util
	x11-apps/xclock
	x11-apps/bdftopcf
	x11-terms/xterm
	x11-misc/imake
	x11-misc/util-macros
	sys-devel/gettext
	sys-devel/llvm
	www-client/links
	x11-proto/compositeproto
	x11-proto/damageproto
	x11-proto/fixesproto
	x11-proto/fontcacheproto
	x11-proto/fontsproto
	x11-proto/printproto
	x11-proto/randrproto
	x11-proto/recordproto
	x11-proto/resourceproto
	x11-proto/scrnsaverproto
	x11-proto/trapproto
	x11-proto/videoproto
	x11-proto/xcmiscproto
	x11-proto/xf86bigfontproto
	x11-proto/xf86dgaproto
	x11-proto/xf86driproto
	x11-proto/xf86miscproto
	x11-proto/xf86rushproto
	x11-proto/xf86vidmodeproto
	x11-proto/xineramaproto
	dev-lang/swig
	sys-kernel/genkernel
	sys-libs/cracklib
	app-text/build-docbook-catalog
	app-text/sgml-common
	app-text/docbook-xsl-stylesheets
	app-text/docbook-xml-dtd
	app-text/gnome-doc-utils
	app-admin/eselect-xvmc
	dev-util/unifdef
	net-mail/mailbase
	mail-mta/ssmtp
	dev-util/cmake
	dev-util/scons
	dev-libs/pkcs11-helper
	app-admin/sudo
	media-fonts/dejavu
	games-misc/fortune-mod
	media-fonts/font-adobe-100dpi
	app-text/recode
	media-libs/glew
	media-sound/alsa-headers
	dev-util/gtk-doc-am
	app-text/scrollkeeper-dtd
	app-text/scrollkeeper
	app-text/rarian
	perl-core/Encode
	dev-perl/Archive-Tar
	dev-perl/Compress-Raw-Zlib
	dev-perl/Compress-Zlib
	dev-perl/DateManip
	dev-perl/ExtUtils-CBuilder
	dev-perl/IO-Compress-Base
	dev-perl/IO-Compress-Zlib
	dev-perl/IO-String
	dev-perl/IO-Zlib
	dev-perl/XML-Parser
	dev-perl/extutils-parsexs
	dev-perl/module-build
	dev-perl/Compress-Raw-Bzip2
	dev-perl/IO-Compress-Bzip2
	dev-perl/yaml
	dev-perl/XML-NamespaceSupport
	dev-perl/XML-LibXML-Common
	dev-perl/XML-SAX
	dev-perl/YAML-Tiny
	dev-perl/XML-LibXML
	dev-perl/XML-Simple
	media-gfx/imagemagick
	gnome-base/libgtop
	x11-libs/libgksu
	x11-libs/gksu
	gnome-base/gnome-common
	xfce-extra/xfce4-notifyd
	sys-devel/autoconf
	sys-devel/autogen
	sys-devel/automake
	dev-scheme/guile
	dev-python/paramiko
	dev-vcs/bzr
	dev-vcs/git
	dev-lang/vala
	dev-libs/libcroco
	dev-util/gperf
	gnome-base/librsvg
	media-fonts/unifont
	dev-libs/gobject-introspection
	sys-fs/aufs-headers
	media-video/ffmpeg

livecd/empty:
	/var/cache/revdep-rebuild
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/logrotate.d
	/etc/runlevels/single
	/etc/skel
	/usr/lib/nfs
	/usr/local
	/usr/src
	/var/cache
	/var/empty
	/var/lock
	/var/log
	/var/run
	/var/spool
	/var/state
	/var/www
	/var/tmp
	/tmp

livecd/rm:
	/boot/System*
	/boot/initr*
	/boot/kernel*
	/root/.ccache
	/root/.viminfo
	/lib/dev-state
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/genkernel.conf
	/etc/make.conf.example
	/etc/splash
	/lib*/*.a
	/lib*/*.la
	/lib*/cpp
	/lib*/security/pam_chroot.so
	/lib*/security/pam_debug.so
	/lib*/security/pam_ftp.so
	/lib*/security/pam_issue.so
	/lib*/security/pam_mkhomedir.so
	/lib*/security/pam_postgresok.so
	/lib*/security/pam_rhosts_auth.so
	/lib*/security/pam_userdb.so
	/root/.bash_history
	/root/.svn
	/root/.zsh/.svn
	/usr/lib/mozilla-firefox/include
	/usr/lib/mozilla-firefox/idl
	/usr/include/webkit*
	/usr/include/mozilla-firefox
	/usr/include/unicode
	/usr/include/wx*
	/usr/include/tsk3
	/usr/lib/wx/include
	/usr/lib/tcl*/include
	/usr/lib/gdkmm*
	/usr/lib/scons*
	/usr/share/doc/scons-*
	/usr/share/man/{man0p,man2,man3,man3p,man4,man6,man7,man9}
	/usr/share/man/{ca*,fr*,gl*,id*,hu*,it*,jp*,pl*,pt*,ru*,sk*,ug*,zh*}
	/usr/share/man/man1/{zshall.1.gz,ssl-*,openssl*,perl*,pod2*}
	/usr/share/man/man5/{groff*,lj4*}
	/usr/sbin/archive-conf
	/usr/sbin/bootsplash*
	/usr/sbin/dispatch-conf
	/usr/sbin/fb*
	/usr/share/misc/*.old
	/usr/share/devhelp
	/usr/share/doc
	/usr/share/info
	/bin/*.old
	/sbin/*.old
	/usr/share/gtk-doc
	/usr/share/gtk-2.0
	/usr/bin/{addr2line,as,bashcomp-config,gfortran*,gmsgfmt,gprof}
	/usr/bin/{idle,ifnames,kernel-config,lex}
	/usr/bin/{pydoc,rc-config,rpm2tar,size,wish}
	/usr/bin/{yacc,gtk-demo,cdda2wav,readcd,htmltopng}
	/usr/bin/{repoman,tbz2tool,xpak}
	/usr/lib/{libltdl.so,libtk*}
	/sbin/{kallsyms,kallsyms.static,ksyms,ksyms.static}
	/usr/lib/nss/*.a
	/usr/lib/nspr/*.a
	/usr/lib/cairo/*.la
	/usr/lib/librpm*.la
	/usr/lib/rpm-plugins/*.la
	/usr/lib/{libbsd.a,libcurses.a,libpng.a}
	/usr/lib/{libipsec.la}
	/usr/*/lib/{libbfd.a,libiberty.a,libopcodes.a}
	/usr/lib/binutils/*/*/libbfd.{a,la}
	/usr/lib/binutils/*/*/libopcodes.{a,la}
	/usr/include/GL
	/var/mail
	/make*
	/bin/.svn
	/var/.svn
	/var/lib/.svn
	/usr/.svn
	/usr/sbin/.svn
	/etc/.svn
	/etc/X11/.svn
	/etc/X11/xinit/.svn
	/etc/udev/.svn
	/etc/udev/rules.d/.svn
	/usr/bin/{s2p,perlcc,xsubpp,splain,h2xs,perlbug,psed,piconv,instmodsh,dprofpp,perldoc}
	/usr/bin/{pl2pm,perlivp,a2p,libnetcfg,find2perl,enc2xs,pstruct,pod2latex,cpan,c2ph}
	/usr/bin/{smbclient,net,smbget,smbtree,nmblookup,smbpasswd,rpcclient,smbcacls,smbcquotas,ntlm_auth}
	/usr/share/doc/{lrzsz*,minicom*,vte*,ckermit*}
	/usr/share/gtk-doc/html/vte*
	/usr/portage/{*-*,virtual,packages,scripts,metadata,licenses,eclass,distfiles,skel*,header.txt}
	/usr/portage/profiles/arch/{alpha,arm,hppa,ia64,m68k,mips,powerpc,ppc,ppc64,s390,sparc,x86-fbsd}
	/usr/portage/profiles/{default/bsd,default-bsd,hardened,obsolete,selinux,uclibc,ChangeLog}
	/usr/portage/profiles/default/linux/{alpha,arm,hppa,ia64,m68k,mips,powerpc,ppc,ppc64,s390,sparc,x86-fbsd}
	/usr/portage/profiles/default-linux/{alpha,arm,hppa,ia64,m68k,mips,powerpc,ppc,ppc64,s390,sparc,x86-fbsd}
	/usr/bin/{code2color,devdump}
	/usr/bin/{html2png,afmtodit,grolj4,oldfind}
	/usr/lib/groff
	/usr/lib/xorg/modules/multimedia
	/usr/lib/gtkmm*
	/usr/sbin/{ntpd,swat}
	/usr/share/zoneinfo
	/usr/share/locale/{a*,b*,c*,d*,e*,f*,g*,h*,i*,j*,k*,lb,lg,li,lt,lv,m*,n*,o*,p*,q*,r*,s*,t*,u*,v*,w*,x*,y*,z*}
	/usr/lib/locale/{a*,b*,c*,g*,h*,i*,j*,k*,l*,m*,n*,o*,p*,q*,r*,s*,t*,u*,v*,w*,x*,y*,z*}
	/usr/lib/locale/{da*,de_AT*,de_BE*,de_CH*,de_LU*,de_DE@euro,dz*}
	/usr/lib/locale/{en_AU*,en_BW*,en_CA*,en_DK*,en_HK*,en_IE*,en_IN*,en_NG*,en_NZ*,en_PH*,en_SG*,en_ZA*,en_ZW*}
	/usr/lib/locale/{es_*,et_*,eu_*,el_*}
	/usr/lib/locale/{fa*,fi*,fo*,fr_BE*,fr_CA*,fr_CH*,fr_LU*,fy*,fur_IT,fr_FR@euro}
	/usr/share/fonts/misc/6x10-ISO8859-{2,3,4,5,6,7,8,9,10,11,12,13,14}.pcf.gz
	/usr/share/fonts/cyrillic
	/usr/share/fonts/encodings/large
	/usr/share/fonts/misc/{*ja*,*ko*,k14*}
	/usr/share/fonts/{75dpi,unifont}
	/usr/share/i18n/charmaps/{GB18030*,EUC-TW*,CP949*,JOHAB*,GBK*,BIG5*,EUC*}
	/usr/share/i18n/charmaps/{SHIFT*,ISO_default46*,GB2312*,WINDOWS-31J*}
	/usr/share/ati/*
	/opt/bin/amdcccle
	/opt/bin/fglrxinfo
	/usr/lib/opengl/nvidia/*
	/usr/lib/opengl/nvidia/*
	/usr/lib/syslinux/com32
	/usr/lib/opengl/xorg-x11/include
	/usr/share/man/{bg,cs,da,de,el,es,fi,hr,ja,ko,nl,pt,ro,sl}
	/usr/bin/dar_static
	/usr/bin/{Xati,Xephyr,Xfake,Xi810,Xmga,Xvia}
	/usr/sbin/th_htpasswd
	/usr/include/{*mm*,poppler,openssl,nouveau,libxml2,geany,drm,irssi,dar,qemacs,selinux,gmpxx.h,reiser4}
	/usr/share/icons/Rodent
	/usr/lib/python*/test
	/usr/share/dict/
	/usr/share/i18n/locales/{a*,b*,c*,g*,h*,j*,k*,l*,m*,n*,o*,p*,q*,r*,s*,u*,v*,w*,x*,y*,z*}
	/usr/share/i18n/locales/{da*,dz*,de_AT*,de-CH*,de_BE*,es_*,et_*,eu_*,el_*,fa*,fi*,fo*,fr_BE*,fr_CH*,fr_LU*,fy*,fu*}
	/usr/share/i18n/locales/{en_AU,en_BW,en_CA,en_DK,en_HK,en_IE*,en_IN,en_NG,en_NZ,en_PH,en_SG,en_ZA,en_ZW}
	/usr/share/i18n/locales/{id_*,is_*,ik_*,ig_*,it_*,iu_*,iw_*}
	/usr/share/i18n/locales/{ta_*,te_*,tg_*,th_*,ti_*,tig*,tk_*,tl_*,tn_*,tr_*,ts_*,tt_*}
	/usr/share/i18n/locales/*
	/usr/share/X11/locale/{fi*,pt_BR*,el_GR*,zh*,ko*,ja*}
	/usr/share/groff/*/font/devlj4
	/usr/share/zsh/*/functions/Completion/{AIX,Debian,Cygwin,Darwin,Mandriva,Redhat}
	/usr/share/swig/*/{csharp,java,gcj,ruby,guile,modula3,php4}
	/usr/share/vim/vim*/{doc,indent,keymap,spell,tutor,print}
	/usr/share/vim/vim*/syntax/{php.vim,baan.vim,pfmain.vim,autoit.vim,xmodmap.vim}
	/usr/share/vim/vim*/syntax/{postscr.vim,doxygen.vim,lisp.vim,foxpro.vim,sqlanywhere.vim}
	/usr/share/vim/vim*/syntax/{maple.vim,ora.vim,ishd.vim,stata.vim,jam.vim,skill.vim}
	/usr/share/vim/vim*/syntax/{rpl.vim,fortran.vim,aml.vim,fvwm.vim,lpc.vim}
	/usr/share/vim/vim*/syntax/{cdrtoc.vim,groovy.vim,vb.vim,progress.vim,vera.vim}
	/usr/share/vim/vim*/syntax/{inform.vim,sudoers.vim,maxima.vim,idl.vim,sicad.vim,scheme.vim}
	/usr/share/vim/vim*/syntax/{splint.vim,mupad.vim,nqc.vim,openroad.vim,hamster.vim}
	/usr/share/vim/vim*/syntax/{sqr.vim,spup.vim,idlang.vim,ncf.vim,mush.vim,ocaml.vim}
	/usr/share/vim/vim*/syntax/{slrnrc.vim,ada.vim,cmusrc.vim,logtalk.vim,sisu.vim}
	/usr/share/vim/vim*/syntax/{lscript.vim,smcl.vim,mma.vim,lua.vim,virata.vim,slpconf.vim}
	/usr/share/vim/vim*/syntax/{framescript.vim,xmath.vim,freebasic.vim,cobol.vim}
	/usr/share/vim/vim*/syntax/{sml.vim,btm.vim,aspvbs.vim,moo.vim,jal.vim,pov.vim,nastran.vim}
	/usr/share/vim/vim*/syntax/{forth.vim,csc.vim,fasm.vim,tsalt.vim,quake.vim,chill.vim}
	/usr/share/vim/vim*/syntax/{mf.vim,rexx.vim,fgl.vim,specman.vim,radiance.vim,rst.vim}
	/usr/share/vim/vim*/syntax/{tf.vim,tads.vim,ibasic.vim,uc.vim,omnimark.vim,a65.vim}
	/usr/share/vim/vim*/syntax/{pike.vim,jess.vim,litestep.vim,lifelines.vim,abap.vim}
	/usr/share/vim/vim*/syntax/{vhdl.vim,dcl.vim,kix.vim,sqlinformix.vim,rhelp.vim,wml.vim}
	/usr/share/vim/vim*/syntax/{verilogams.vim,hercules.vim,cs.vim,b.vim,fdcc.vim}
	/usr/share/vim/vim*/syntax/{smil.vim,jproperties.vim,clipper.vim,stp.vim,mp.vim}
	/usr/share/vim/vim*/syntax/{wsml.vim,plm.vim,aap.vim,conaryrecipe.vim,racc.vim,pilrc.vim}
	/usr/share/vim/vim*/syntax/{tsscl.vim,flexwiki.vim,trasys.vim,eviews.vim,abel.vim}
	/usr/share/vim/vim*/syntax/{iss.vim,slpreg.vim,verilog.vim,pinfo.vim,acedb.vim,lite.vim}
	/usr/share/vim/vim*/syntax/{mmix.vim,diva.vim,aflex.vim,lhaskell.vim,psf.vim,spyce.vim}
	/usr/share/vim/vim*/syntax/{pccts.vim,lout.vim,occam.vim,ptcap.vim,sl.vim,lace.vim}
	/usr/share/vim/vim*/syntax/{opl.vim,mplayerconf.vim,lprolog.vim,gkrellmrc.vim,snobol4.vim}
	/usr/share/vim/vim*/syntax/{ampl.vim,prolog.vim,loginaccess.vim,cl.vim,cupl.vim}
	/usr/share/vim/vim*/syntax/{gretl.vim,sinda.vim,papp.vim,django.vim,logindefs.vim}
	/usr/share/vim/vim*/syntax/{expect.vim,latte.vim,tpp.vim,mgl.vim,modsim3.vim}
	/usr/share/vim/vim*/syntax/{focexec.vim,bdf.vim,sather.vim,objc.vim,dylan.vim,msidl.vim}
	/usr/share/vim/vim*/syntax/{mel.vim,pic.vim,hitest.vim,simula.vim,bib.vim,purifylog.vim}
	/usr/share/vim/vim*/syntax/{gdmo.vim,modula2.vim,r.vim,privoxy.vim,slrnsc.vim,scilab.vim}
	/usr/share/vim/vim*/syntax/{povini.vim,desc.vim,matlab.vim,webmacro.vim,mason.vim}
	/usr/share/vim/vim*/syntax/{hb.vim,bst.vim,form.vim,amiga.vim,tak.vim,cdl.vim,dot.vim}
	/usr/share/vim/vim*/syntax/{yaml.vim,sm.vim,cweb.vim,z8a.vim,elmfilt.vim,pod.vim}
	/usr/share/vim/vim*/syntax/{slice.vim,ppwiz.vim,mib.vim,tssgm.vim,ahdl.vim,eruby.vim}
	/usr/share/vim/vim*/syntax/{netrw.vim,esterel.vim,clean.vim,smarty.vim,dracula.vim}
	/usr/share/vim/vim*/syntax/{st.vim,cynlib.vim,atlas.vim,uil.vim,kwt.vim,ayacc.vim,asn.vim}
	/usr/share/vim/vim*/syntax/{prescribe.vim,gp.vim,lotos.vim,elf.vim}
	/usr/share/vim/vim*/syntax/{pf.vim,snnsnet.vim,gedcom.vim,javacc.vim,spice.vim,esqlc.vim}
	/usr/share/vim/vim*/syntax/{chordpro.vim,asmh8300.vim,texmf.vim,sd.vim,takout.vim}
	/usr/share/vim/vim*/syntax/{rib.vim,modula3.vim,sindaout.vim,mgp.vim,cuplsim.vim,kscript.vim}
	/usr/share/vim/vim*/syntax/{ist.vim,snnspat.vim,ave.vim,rnc.vim,abc.vim,remind.vim}
	/usr/share/vim/vim*/syntax/{dcd.vim,tssop.vim,gsp.vim,snnsres.vim,cheetah.vim,xsd.vim}
	/usr/share/vim/vim*/syntax/{grads.vim,pyrex.vim,tli.vim,rnoweb.vim,takcmp.vim,cynpp.vim}
	/usr/share/vim/vim*/syntax/{sindacmp.vim,bzr.vim,sieve.vim,jgraph.vim,xs.vim,ecd.vim}
	/usr/share/vim/vim*/syntax/{tilde.vim,trustees.vim,dylanintr.vim,abaqus.vim,README.txt}
	/usr/share/vim/vim*/autoload/{README.txt,ada.vim,adacomplete.vim,decada.vim,gnat.vim}
	/usr/share/vim/vim*/autoload/{spellfile.vim,phpcomplete.vim,netrw.vim,javascriptcomplete.vim}
	/usr/share/vim/vim*/lang/menu_{ja*,ru*,vi*,zh*,sr*,sl*,ch*,it*,ca*,es*,pl*,po*,pt*}
	/usr/share/vim/vim*/lang/menu_{cs*,cz*,sr*,hu*,no*,sv*,nl*,ko*,af*,sk*}
	/usr/share/vim/vim*/macro/{hanoi*,life*,maze*,urm*}
	/usr/share/vim/vim*/ftplugin/{ocaml.vim,cobol.vim,ada.vim,Append*,vhdl.vim,eruby.vim}
	/usr/share/vim/vim*/ftplugin/{abaqus.vim,vb.vim,hamster.vim,aspvbs.vim,flexwiki.vim}
	/usr/share/vim/vim*/ftplugin/{verilog.vim,lprolog.vim,ishd.vim,xsd.vim,scheme.vim,occam.vim}
	/usr/share/vim/vim*/ftplugin/{mupad.vim,lua.vim,lisp.vim,aap.vim,pyrex.vim,matlab.vim}
	/usr/share/xfce4/backdrops/{flower.png,xfce-*png}
	/usr/share/xfce4/doc
	/usr/share/alsa
	/usr/share/icons/hicolor/icon-theme.cache
	/usr/share/icons/gnome/scalable
	/usr/share/icons/gnome/256x256
	/usr/include/{alsa,nspr,OpenIPMI,nss,xorg,hunspell,xulrunner*,netlink,xfce4,exo*}
	/usr/lib/portage/pym/cache/{*.pyo,*.pyc}
	/usr/lib/portage/pym/elog_modules/{*.pyo,*.pyc}
	/usr/lib/portage/pym/{*.pyo,*.pyc}
	/usr/lib/python*/pym/{*.pyo,*.pyc}
	/usr/lib/gentoolkit/pym/gentoolkit/{*.pyo,*.pyc}
	/usr/share/dstat/{*.pyo,*.pyc}
	/usr/bin/{Xchips,Xepson,Xmach64,Xnest,Xpm2,Xr128,Xsmi,Xvfb}
	/usr/share/gcc-data/*-pc-linux-gnu/*/{info,locale}
	/usr/share/binutils-data/*-pc-linux-gnu/*/{info,locale}
	/usr/lib/mozilla-firefox/xpidl
	/usr/bin/fgl_glxgears
	/usr/include/{X11,sigc++*}
	/usr/lib/cracklib_dict.*
	/usr/share/dmraid
	/usr/share/doc/git*
	/usr/share/man/*/git*
	/usr/lib/xorg/modules/extensions/libglx.so
	/usr/lib/opengl/xorg-x11/extensions/libglx.so
	/usr/bin/glsl_compiler
	/usr/lib/dri
	/lib/firmware/{dvb*,v4l*,i6050*,i2400*}
