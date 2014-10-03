# -*- coding:utf-8-unix -*-
#
# Copyright (c) 2005-2011 InfiniTalk, inc.
# This file and all modifications and/or additions are under
# the same license as package itself.

#マクロ
%define distribution    centos-6
%define enable_osp    %([ -f %{_includedir}/osp/osp.h ] && echo 1 || echo 0)
%define enable_sqlite %([ -f %{_includedir}/sqlite.h ] && echo 1 || echo 0)
%define enable_tds    %([ -f %{_includedir}/tds.h ] && echo 1 || echo 0)
%define enable_h323   %{?_with_h323:1}%{!?_with_h323:0}
%define enable_mp3    0
%define enable_rpt    0
%define enable_vpb    %([ -f %{_includedir}/vpbapi.h ] && echo 1 || echo 0)
%define enable_misdn	0
%define enable_valetparking 0
%define enable_fax    0
%define enable_meetme 0%{?_with_meetme:1}
%define _unpackaged_files_terminate_build 0
%define malloc_debug  %{?_with_malloc_debug:1}%{!?_with_malloc_debug:0}
%define deadlock_debug  %{?_with_deadlock_debug:1}%{!?_with_deadlock_debug:0}
%define show_malloc   %{?_with_show_malloc:1}%{!?_with_show_malloc:0}
%define fnets %{?_fnets:1}%{!?_fnets:0}
%define x86_64 %{?_x86_64:1}%{!?_x86_64:0}

%define nam asterisk
%define ver 1.8.13.0
%define rel f0.20
%define dst %{?dist}
Epoch: 2014080401

#基本情報
Summary: Asterisk PBX
Summary(ja_JP.utf8): アスタリスク PBX
Name: %{nam}
Version: %{ver}
Release: %{rel}%{dst}
License: GPL2
Group: Utilities/System
BuildRoot: %{_tmppath}/%{name}-%{version}
URL: http://www.asterisk.org/

# パッケージの作成時に必要となる情報
#Source0: http://ftp.digium.com/pub/telephony/asterisk/%{name}-%{version}.tar.gz
Source0: asterisk-1.8.13.0.tar.gz
#NoSource: 0
# http://5sn.net/asterisk/rawplayer/native/
### Source1: asterisk-1.2.5-musiconhold.tar.bz2
#Source2: http://www.pbxfreeware.com/app_valetparking.c
#Source3: app_fax.c.1.6.0.21
#Source4: astobj2.c.1.2.35
#Source5: astobj2.h.1.2.35
#Source6: menuselect.makeopts.1.8.13
### Source7: sounds.ja.tar.gz
### Source8: collectSoFiles.sh.tar.gz
#Patch0: asterisk-1.8.13-realtime.patch
#Patch1: asterisk-1.8.13-japanese.patch
#Patch2: asterisk-1.8.13-saxa_nakayo.patch
#Patch3: asterisk-1.8.13-ntt_hikari.patch
#Patch4: asterisk-1.8.13-bugfix.patch
#Patch5: asterisk-1.8.13-bugfix20130614.patch
#Patch6: infinitalk_config.patch
#Patch7: infinitalk_config20130705.patch
#Patch8: astsbindir.patch
#Patch9: asterisk-1.8.13-tenant_moh.patch
#Patch10: support_eclipse_debugger.patch
#Patch11: asterisk-1.8.13-bugfix20130925.patch
#Patch12: cpu100per.patch
#Patch13: park.patch

# 依存情報
BuildRequires:  libpri-devel >= 1.2.0
#BuildRequires:  libtermcap-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  openssl-devel
#BuildRequires:  gtk+-devel
BuildRequires:  newt-devel
BuildRequires:  ncurses-devel
BuildRequires:  unixODBC-devel
BuildRequires:  speex-devel
BuildRequires:  postgresql-devel
BuildRequires:  zlib-devel
BuildRequires:  bison
BuildRequires:  curl-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  sox
%if %{enable_fax}
#BuildRequires:  spandsp-devel
%endif
%if %enable_h323
BuildRequires: openh323-devel
%endif
%if %enable_sqlite
BuildRequires: sqlite-devel
%endif

%description
Asterisk is an Open Source PBX and telephony development platform that
can both replace a conventional PBX and act as a platform for developing
custom telephony applications for delivering dynamic content over a
telephone similarly to how one can deliver dynamic content through a
web browser using CGI and a web server.

Asterisk talks to a variety of telephony hardware including BRI, PRI, 
POTS, and IP telephony clients using the Inter-Asterisk eXchange
protocol (e.g. gnophone or miniphone).  For more information and a
current list of supported hardware, see www.asteriskpbx.com.

%description -l ja_JP.utf8
Asterisk はオープンソースな構内交換機 (PBX) および電話開発用の
プラットホームで、通常の PBX の置き換えとして、また CGI や
ウェブサーバを使ったウェブブラウザ経由と似た方法で電話経由で
動的なコンテントを配信するためのカスタム電話アプリケーション
開発用プラットホームとして使用できます。

Asterisk は BRI, PRI, POTS、および Inter-Asterisk eXchage
プロトコルを使用する 各種通信機器およびIP電話クライアント
(gnophone や miniphone など) と通信することができます。

%package        devel
Summary:        Header files for building Asterisk modules
Summary(ja_JP.utf8): Asterisk 開発用パッケージ
Group:          Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains the development  header files that are needed
to compile 3rd party modules.

%description devel -l ja_JP.utf8
Asterisk 用のモジュールを開発する際に必要なヘッダファイルです。

%package	adsi
Summary:	Analog Display Services Interface
Summary(ja_JP.utf8): アナログディスプレイサービスインターフェース
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	adsi
Analog Display Services Interface for asterisk

%description	adsi -l ja_JP.utf8
asterisk 用のアナログディスプレイサービスインターフェースです。

%package	agent
Summary:	Agent channel
Summary(ja_JP.utf8): エージェントチャンネル
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	agent
Agent proxy channel

%description	agent -l ja_JP.utf8
エージェントチャンネルを使用するのに必要なパッケージです。

%package	alarmreceiver
Summary:	Central Station Alarm receiver
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	alarmreceiver
Central Station Alarm receiver for Ademco Contact ID

%package	alsa
Summary:	ALSA Console Channel Driver
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	alsa
ALSA Console Channel Driver for asterisk

%package	festival
Summary:	Festival Interface
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	festival
Simple Festival Interface

%package	h323
Summary:	OpenH323 channel driver for asterisk.
Summary(ja_JP.utf8): OpenH323 チャンネルドライバー
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	h323
OpenH323 channel driver for asterisk.

%description	h323 -l ja_JP.utf8
OpenH323 を使用するのに必要なパッケージです。

%package	skinny
Summary:	Skinny channel driver for asterisk.
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	skinny
Skinny channel driver for asterisk.

%package	cdr
Summary:	CDR recorder for asterisk.
Summary(ja_JP.utf8): CDR レコーダー
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	cdr
Call Detail Records for asterisk.

%description    cdr -l ja_JP.utf8
発着信履歴を記録するのに必要なパッケージです。

%package	cdr-custom
Summary:	Custom Comma Separated Value CDR recorder
Summary(ja_JP.utf8): カスタマイズ可能な CSV 形式用 CDR レコーダー
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:  	%{name}-cdr = %{epoch}:%{version}-%{release}

%description	cdr-custom
Customizable Comma Separated Values CDR Backend.

%description	cdr-custom -l ja_JP.utf8
発着信履歴をカスタマイズ可能な CSV 形式で記録するのに必要なパッケージです。

%package	cdr-odbc
Summary:	ODBC CDR logger
Summary(ja_JP.utf8): ODBC 用 CDR レコーダー
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:  	%{name}-cdr = %{epoch}:%{version}-%{release}

%description	cdr-odbc
ODBC CDR logger.

%description	cdr-odbc -l ja_JP.utf8
発着信履歴を ODBC 経由で記録するのに必要なパッケージです。

%package	cdr-pgsql
Summary:	PostgreSQL CDR logger
Summary(ja_JP.utf8): PostgreSQL 用 CDR レコーダー
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:  	%{name}-cdr = %{epoch}:%{version}-%{release}

%description	cdr-pgsql
PostgreSQL CDR logger.

%description    cdr-pgsql -l ja_JP.utf8
発着信履歴を PostgreSQL へ記録するのに必要なパッケージです。

%if %enable_sqlite
%package	cdr-sqlite
Summary:	SQLite CDR logger
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:  	%{name}-cdr = %{epoch}:%{version}-%{release}

%description	cdr-sqlite
SQLite CDR logger.
%endif

%if %enable_tds
%package	cdr-tds
Summary:	FreeTDS CDR logger
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:  	%{name}-cdr = %{epoch}:%{version}-%{release}

%description	cdr-tds
FreeTDS CDR logger.
%endif

%package	chanspy
Summary:	Listen in on any channel
Summary(ja_JP.utf8): チャンネルのモニタリング
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	chanspy
Tap into any type of asterisk channel and listen to aud
io

%description    chanspy -l ja_JP.utf8
他のチャンネルに接続し、音声をモニタするのに必要なパッケージです。

%package        disa
Summary:        Direct Inward System Access
Group:          System Environment/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    disa
DISA (Direct Inward System Access) Allows someone from outside
the telephone switch (PBX) to obtain an "internal" system dialtone
and to place calls from it as if they were placing a call from
within the switch.

%package	dundi
Summary:	Distributed Universal Number Discovery
Summary(ja_JP.utf8): DUNDi - P2P ルーティングプロトコル
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	dundi
Distributed Universal Number Discovery (DUNDi)

%description    dundi -l ja_JP.utf8
DUNDi (P2P ルーティングプロトコル) を使用するのに必要なパッケージです。

%if %{enable_fax}
%package	fax
Summary:	Simple FAX Application
Summary(ja_JP.utf8): シンプルな FAX アプリケーション
Group:		System Environment/Libraries
Requires:	%{name} = %{version}-%{release}

%description	fax
Simple FAX Application

%description	fax -l ja_JP.utf8
FAX を使用するのに必要なパッケージです。
%endif

%package	ices
Summary:	Stream to an icecast server via ICES
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	ices
Encode and stream using ices.

%package	meetme
Summary:	Meet me conference bridge
Summary(ja_JP.utf8): 電話会議
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-zap = %{epoch}:%{version}-%{release}

%description	meetme
Telephone conference module for asterisk.

%description    meetme -l ja_JP.utf8
電話会議を行うのに必要なパッケージです。

%package	mgcp
Summary:	Implementation of Media Gateway Control Protocol for asterisk
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	mgcp
Implementation of Media Gateway Control Protocol

%if %{enable_misdn}
%package	misdn
Summary:	Channel driver for mISDN
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	misdn
Channel driver for mISDN Support (Bri/Pri)

%endif

%package	modem
Summary:	Voice Modem Drivers
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	modem
Voice Modem Drivers.

%package	monitor
Summary:	Monitor a channel
Summary(ja_JP.utf8): 通話録音
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	monitor
Monitor a channel

%description    monitor -l ja_JP.utf8
通話録音を行うのに必要なパッケージです。

%if %enable_mp3
%package	mp3
Summary:	Play an MP3 file
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mpg123

%description	mp3
Silly application to play an MP3 file -- uses mpg123
%endif

%package	nbscat
Summary:	Play an NBS local stream
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	nbscat
Play an NBS local stream

%if %enable_osp
%package	osp
Summary:	Open Settlement Protocol Support
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	osp
Provide Open Settlement Protocol capability
%endif

%package	page
Summary:	Pages phones
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-meetme = %{epoch}:%{version}-%{release}

%description	page
Page Multiple Phones

%package	queue
Summary:	call queues
Summary(ja_JP.utf8): コールキューイング
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-monitor = %{epoch}:%{version}-%{release}

%description	queue
Call queues

%description	queue -l ja_JP.utf8
コールキューイングを使用するのに必要なパッケージです。

%if %enable_rpt
%package	rpt
Summary:	Radio Repeater/Remote Base
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	rpt
Radio Repeater/Remote Base Control System
%endif

%package	sms
Summary:	SMS handler
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	sms
ETSI ES 201 912 protocol 1 implimentation

%package	valetparking
Summary:	call valetparking
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	valetparking
Call parking module for asterisk

%package	voicemail
Summary:	Voicemail System
Summary(ja_JP.utf8): ボイスメール
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:       %{nam}-adsi = %{epoch}:%{version}-%{release}

%description	voicemail
Voicemail System for asterisk

%description	voicemail -l ja_JP.utf8
ボイスメールを使用するのに必要なパッケージです。

%if %enable_vpb
%package	vpb
Summary:	VoiceTronix Interface driver
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description	vpb
VoiceTronix Interface driver
%endif

%package	zap
Summary:	ZAP trunk
Summary(ja_JP.utf8): ZAP チャンネル
Group:		System Environment/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	zaptel >= 1.2.13

%description	zap
ZAP trunk

%description	zap -l ja_JP.utf8
ZAP チャンネルを使用するのに必要なパッケージです。

%{?_build_debug:%{debug_package}}

%prep
%setup -q
### %setup -q -a1
%if %{enable_valetparking}
#%__cp %{SOURCE2} apps/app_valetparking.c
%endif
%if %{enable_fax}
%__cp %{SOURCE3} apps/app_fax.c
%endif
%if %{enable_meetme}
%__cp %{SOURCE4} astobj2.c
%__cp %{SOURCE5} include/asterisk/astobj2.h
%endif
#%__cp %{SOURCE6} menuselect.makeopts
#%__cp %{SOURCE6} menuselect.makeopts.default

# Source7
### %setup -q -T -D -a7

# Source8
### %setup -q -T -D -a8

#%patch0 -p1 -b .realtime
#%patch1 -p1 -b .japanese
#%patch2 -p1 -b .saxa_nakayo
#%patch3 -p1 -b .ntt_hikari
#%patch4 -p1 -b .bugfix
#%patch5 -p1 -b .bugfix20130614
#%patch6 -p1 -b .infinitalk_config
#%patch7 -p1 -b .infinitalk_config20130705
#%patch8 -p1 -b .astsbindir
#%patch9 -p1 -b .tenant_moh
#%patch10 -p1 -b .support_eclipse_debugger
#%patch11 -p1 -b .bugfix20130925
#%patch12 -p1 -b .cpu100per
#%patch13 -p1 -b .park

%build
%if %malloc_debug
sed -i -e 's/^\(MALLOC_DEBUG.*\)#\(.*\)$/\1\2/g;' Makefile
%endif
%if %deadlock_debug
sed -i -e 's/^\(DEBUG_THREADS = \)\(#.*\)$/\1-DDEBUG_THREADS -DDETECT_DEADLOCKS \2/g;' Makefile
%endif

%if %enable_h323
cd channels/h323
make opt OPENH323DIR=%{_datadir}/openh323 \
    OH323_INCDIR=%{_includedir}/openh323 OH323_LIBDIR=%{_libdir}
cd ../..
%endif
%if %x86_64
#./configure --disable-xmldoc
./configure CFLAGS="$CFLAGS -mtune=native" --with-postgres=/usr/pgsql-9.1
#%patch4 -p1 -b .bugfix0
#%__cp %{SOURCE6} menuselect.makeopts.default

#%__make ASTLIBDIR=%{_libdir}/%{name} PROC=x86_64 USER_MAKEOPTS="menuselect.makeopts.defaults"
%__make ASTLIBDIR=%{_libdir}/%{name} PROC=x86_64
%else
#./configure --disable-xmldoc
./configure CFLAGS="$CFLAGS -mtune=native -Wall -O4 -fexpensive-optimizations -funroll-loops -fPIC" --with-postgres=/usr/pgsql-9.1
%__make ASTLIBDIR=/usr/lib/%{name} PROC=i686
%endif

%install
rm -rf $RPM_BUILD_ROOT

%__make ASTLIBDIR=%{_libdir}/%{name} DESTDIR=%{buildroot} install
%__make ASTLIBDIR=%{_libdir}/%{name} DESTDIR=%{buildroot} samples
# you have doxygen installed on your local system
%__make progdocs

%__mkdir_p %{buildroot}/%{_initrddir}
#%__cp contrib/init.d/rc.redhat.asterisk %{buildroot}/%{_initrddir}/asterisk
%__cp contrib/init.d/rc.redhat.infinitalk.asterisk %{buildroot}/%{_initrddir}/asterisk
# Collect support information
%__rm -f %{buildroot}/%{_sbindir}/autosupport
# logrotate configuration file
%__mkdir_p %{buildroot}/%{_sysconfdir}/logrotate.d
cat > %{buildroot}/%{_sysconfdir}/logrotate.d/%{name} <<END
/var/log/asterisk/event_log /var/log/asterisk/messages /var/log/asterisk/queue_log /var/log/asterisk/cdr-csv/Master.csv {
    missingok
    notifempty
    sharedscripts
    postrotate
        [ -e /var/lock/subsys/asterisk ] && /usr/sbin/asterisk -r -x 'logger rotate' || :
    endscript
}
END

%__mkdir_p %{buildroot}/var/spool/asterisk/dictate
%__mkdir_p %{buildroot}/var/spool/asterisk/outgoing
%__mkdir_p %{buildroot}/var/spool/asterisk/monitor
%__mkdir_p %{buildroot}/var/log/asterisk/cdr-csv
touch %{buildroot}/var/log/asterisk/cdr-csv/Master.csv
%__mkdir_p %{buildroot}/var/log/asterisk/cdr-custom
touch %{buildroot}/var/log/asterisk/cdr-custom/Master.csv

# meetme recording files
%__mkdir_p %{buildroot}/var/spool/asterisk/meetme

# Music On Hold
%__mkdir %{buildroot}/var/lib/asterisk/moh-files
%__install -m 644 moh-files/* %{buildroot}/var/lib/asterisk/moh-files/

# documentation
#%__mkdir %{buildroot}/var/lib/asterisk/documentation
#%__install -m 644 doc/* %{buildroot}/var/lib/asterisk/documentation/

# Start up script directory
%__mkdir %{buildroot}%{_sysconfdir}/asterisk/startup.d

%__mkdir_p %{buildroot}/var/asterisk/webapp/lib
touch %{buildroot}/var/asterisk/webapp/lib/version
echo "Infini-Asterisk"%{ver}-%{rel} > %{buildroot}/var/asterisk/webapp/lib/version

# infinitalk ja sounds
%__mkdir_p %{buildroot}/var/lib/asterisk/sounds
cp -r ja %{buildroot}/var/lib/asterisk/sounds

# infinitalk tenant moh
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_a
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_b
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_c
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_d
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_e
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_f
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_g
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_h
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_i
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_j
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_k
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_l
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_m
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_n
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_o
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_p
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_q
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_r
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_s
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_t
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_u
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_v
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_w
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_x
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_y
cp -rf %{buildroot}/var/lib/asterisk/moh %{buildroot}/var/lib/asterisk/moh_z

# channele license over sounds
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/en/outgoing-too-many-calls-line.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/en/outgoing-too-many-calls.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/en/incoming-too-many-calls-line.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/en/incoming-too-many-calls.gsm

cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/ja/outgoing-too-many-calls-line.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/ja/outgoing-too-many-calls.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/ja/incoming-too-many-calls-line.gsm
cp %{buildroot}/var/lib/asterisk/sounds/en/beep.gsm %{buildroot}/var/lib/asterisk/sounds/ja/incoming-too-many-calls.gsm

%clean
rm -rf %{buildroot}

%pre
%{_sbindir}/groupadd -g 58 asterisk > /dev/null 2>&1 || :
%{_sbindir}/useradd -r -d /var/lib/asterisk -u 58 -g 58 asterisk > /dev/null  2>&1 || :

%post
/sbin/chkconfig --add %{name}

if [ "$1" = "2" ]
then
  [ -f /var/lib/%{name}/astdb ] && %__chown asterisk.asterisk /var/lib/%{name}/astdb
  %__chown -R asterisk.asterisk /var/log/asterisk/
  %__chown -R asterisk.asterisk /var/spool/asterisk/
fi

%preun
if [ "$1" = "0" ]; then
    /sbin/chkconfig --del %{name} || :
    /sbin/service asterisk stop || :
    %{_sbindir}/userdel asterisk
    %{_sbindir}/groupdel asterisk
    /bin/true
fi

%postun
if [ "$1" = 1 ]; then
%_initrddir/asterisk condrestart > /dev/null 2>&1 || :
fi

%files
%defattr(0644,root,root,0755)
#%doc COPYING BUGS CHANGES CREDITS ChangeLog HARDWARE
%doc COPYING BUGS CHANGES CREDITS ChangeLog
#%doc LICENSE README README.fpm SECURITY UPGRADE.txt
%doc LICENSE README UPGRADE.txt
%doc doc

%attr(0755,asterisk,asterisk)
%dir    %{_sysconfdir}/asterisk

%attr(0750,asterisk,asterisk)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/asterisk.adsi
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/telcordia-1.adsi
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/adsi.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/agents.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/ais.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/alarmreceiver.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/alsa.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/amd.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/app_mysql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/calendar.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/ccss.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_adaptive_odbc.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_custom.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_manager.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_mysql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_odbc.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_sqlite3_custom.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_syslog.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_tds.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel_custom.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel_odbc.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel_pgsql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel_sqlite3_custom.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cel_tds.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/chan_dahdi.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/chan_mobile.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/chan_ooh323.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cli.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cli_aliases.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cli_permissions.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/codecs.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/console.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/dbsep.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/dnsmgr.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/dsp.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/dundi.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/enum.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/extconfig.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/extensions.ael
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/extensions.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/extensions.lua
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/extensions_minivm.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/features.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/festival.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/followme.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/func_odbc.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/gtalk.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/h323.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/http.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/iax.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/iaxprov.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/indications.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/jabber.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/jingle.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/logger.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/manager.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/meetme.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/mgcp.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/minivm.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/misdn.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/modules.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/musiconhold.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/muted.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/osp.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/oss.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/phone.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/phoneprov.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/queuerules.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/queues.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_config_mysql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_config_sqlite.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_curl.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_fax.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_ldap.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_odbc.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_pgsql.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_pktccops.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_snmp.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/res_stun_monitor.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/rtp.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/say.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/sip.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/sip_notify.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/skinny.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/sla.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/smdi.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/udptl.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/unistim.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/users.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/voicemail.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/vpb.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/asterisk.conf

%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/*.ael
%config(noreplace) %attr(0644,root,asterisk) %{_sysconfdir}/logrotate.d/%{name}
%attr(0750,asterisk,asterisk) %dir    %{_sysconfdir}/asterisk/startup.d
%attr(0755,root,root)       %{_initrddir}/asterisk

%defattr(0644,asterisk,asterisk,0755)
%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules

############################################################
%{_libdir}/asterisk/modules/app_authenticate.so
%{_libdir}/asterisk/modules/app_chanisavail.so
%{_libdir}/asterisk/modules/app_controlplayback.so
#%{_libdir}/asterisk/modules/app_curl.so
#%{_libdir}/asterisk/modules/app_cut.so
%{_libdir}/asterisk/modules/app_db.so
%{_libdir}/asterisk/modules/app_dial.so
%{_libdir}/asterisk/modules/app_dictate.so
%{_libdir}/asterisk/modules/app_directed_pickup.so
%{_libdir}/asterisk/modules/app_dumpchan.so
%{_libdir}/asterisk/modules/app_echo.so
#%{_libdir}/asterisk/modules/app_enumlookup.so
#%{_libdir}/asterisk/modules/app_eval.so
%{_libdir}/asterisk/modules/app_exec.so
%{_libdir}/asterisk/modules/app_externalivr.so
#%{_libdir}/asterisk/modules/app_groupcount.so
%{_libdir}/asterisk/modules/app_image.so
#%{_libdir}/asterisk/modules/app_lookupblacklist.so
#%{_libdir}/asterisk/modules/app_lookupcidname.so
%{_libdir}/asterisk/modules/app_macro.so
#%{_libdir}/asterisk/modules/app_math.so
#%{_libdir}/asterisk/modules/app_md5.so
%{_libdir}/asterisk/modules/app_milliwatt.so
%{_libdir}/asterisk/modules/app_parkandannounce.so
%{_libdir}/asterisk/modules/app_playback.so
%{_libdir}/asterisk/modules/app_privacy.so
#%{_libdir}/asterisk/modules/app_random.so
%{_libdir}/asterisk/modules/app_read.so
%{_libdir}/asterisk/modules/app_readfile.so
#%{_libdir}/asterisk/modules/app_realtime.so
%{_libdir}/asterisk/modules/app_record.so
%{_libdir}/asterisk/modules/app_sayunixtime.so
%{_libdir}/asterisk/modules/app_senddtmf.so
%{_libdir}/asterisk/modules/app_sendtext.so
%{_libdir}/asterisk/modules/app_setcallerid.so
#%{_libdir}/asterisk/modules/app_setcidname.so
#%{_libdir}/asterisk/modules/app_setcidnum.so
#%{_libdir}/asterisk/modules/app_setrdnis.so
#%{_libdir}/asterisk/modules/app_settransfercapability.so
%{_libdir}/asterisk/modules/app_softhangup.so
%{_libdir}/asterisk/modules/app_stack.so
%{_libdir}/asterisk/modules/app_system.so
%{_libdir}/asterisk/modules/app_talkdetect.so
%{_libdir}/asterisk/modules/app_test.so
%{_libdir}/asterisk/modules/app_transfer.so
#%{_libdir}/asterisk/modules/app_txtcidname.so
%{_libdir}/asterisk/modules/app_url.so
%{_libdir}/asterisk/modules/app_userevent.so
%{_libdir}/asterisk/modules/app_verbose.so
%{_libdir}/asterisk/modules/app_waitforring.so
%{_libdir}/asterisk/modules/app_waitforsilence.so
%{_libdir}/asterisk/modules/app_while.so
#%{_libdir}/asterisk/modules/chan_features.so
%{_libdir}/asterisk/modules/chan_iax2.so
%{_libdir}/asterisk/modules/chan_local.so
%{_libdir}/asterisk/modules/chan_phone.so
%{_libdir}/asterisk/modules/chan_sip.so
%{_libdir}/asterisk/modules/codec_a_mu.so
%{_libdir}/asterisk/modules/codec_adpcm.so
%{_libdir}/asterisk/modules/codec_alaw.so
%{_libdir}/asterisk/modules/codec_g726.so
%{_libdir}/asterisk/modules/codec_gsm.so
%{_libdir}/asterisk/modules/codec_ilbc.so
%{_libdir}/asterisk/modules/codec_lpc10.so
%{_libdir}/asterisk/modules/codec_speex.so
%{_libdir}/asterisk/modules/codec_ulaw.so
#%{_libdir}/asterisk/modules/format_au.so
%{_libdir}/asterisk/modules/format_g723.so
%{_libdir}/asterisk/modules/format_g726.so
%{_libdir}/asterisk/modules/format_g729.so
%{_libdir}/asterisk/modules/format_gsm.so
%{_libdir}/asterisk/modules/format_h263.so
%{_libdir}/asterisk/modules/format_ilbc.so
%{_libdir}/asterisk/modules/format_jpeg.so
%{_libdir}/asterisk/modules/format_ogg_vorbis.so
%{_libdir}/asterisk/modules/format_pcm.so
#%{_libdir}/asterisk/modules/format_pcm_alaw.so
%{_libdir}/asterisk/modules/format_sln.so
%{_libdir}/asterisk/modules/format_vox.so
%{_libdir}/asterisk/modules/format_wav.so
%{_libdir}/asterisk/modules/format_wav_gsm.so
%{_libdir}/asterisk/modules/func_callerid.so
%{_libdir}/asterisk/modules/func_enum.so
%{_libdir}/asterisk/modules/func_uri.so
%{_libdir}/asterisk/modules/pbx_ael.so
%{_libdir}/asterisk/modules/pbx_config.so
#%{_libdir}/asterisk/modules/pbx_functions.so
%{_libdir}/asterisk/modules/pbx_loopback.so
%{_libdir}/asterisk/modules/pbx_realtime.so
%{_libdir}/asterisk/modules/pbx_spool.so
%{_libdir}/asterisk/modules/res_agi.so
#%{_libdir}/asterisk/modules/res_config_odbc.so
%{_libdir}/asterisk/modules/res_crypto.so
#%{_libdir}/asterisk/modules/res_features.so
#%{_libdir}/asterisk/modules/res_indications.so
%{_libdir}/asterisk/modules/res_musiconhold.so
#%{_libdir}/asterisk/modules/res_odbc.so
%{_libdir}/asterisk/modules/app_amd.so
%{_libdir}/asterisk/modules/app_celgenuserevent.so
%{_libdir}/asterisk/modules/app_channelredirect.so
%{_libdir}/asterisk/modules/app_confbridge.so
%{_libdir}/asterisk/modules/app_dahdibarge.so
%{_libdir}/asterisk/modules/app_dahdiras.so
%{_libdir}/asterisk/modules/app_followme.so
%{_libdir}/asterisk/modules/app_minivm.so
%{_libdir}/asterisk/modules/app_morsecode.so
%{_libdir}/asterisk/modules/app_originate.so
%{_libdir}/asterisk/modules/app_playtones.so
%{_libdir}/asterisk/modules/app_readexten.so
%{_libdir}/asterisk/modules/app_speech_utils.so
%{_libdir}/asterisk/modules/app_waituntil.so
%{_libdir}/asterisk/modules/bridge_builtin_features.so
%{_libdir}/asterisk/modules/bridge_multiplexed.so
%{_libdir}/asterisk/modules/bridge_simple.so
%{_libdir}/asterisk/modules/bridge_softmix.so
%{_libdir}/asterisk/modules/cdr_csv.so
%{_libdir}/asterisk/modules/cdr_syslog.so
%{_libdir}/asterisk/modules/cel_custom.so
%{_libdir}/asterisk/modules/cel_manager.so
%{_libdir}/asterisk/modules/chan_bridge.so
%{_libdir}/asterisk/modules/chan_dahdi.so
%{_libdir}/asterisk/modules/chan_multicast_rtp.so
%{_libdir}/asterisk/modules/chan_unistim.so
%{_libdir}/asterisk/modules/codec_dahdi.so
%{_libdir}/asterisk/modules/codec_g722.so
%{_libdir}/asterisk/modules/format_g719.so
%{_libdir}/asterisk/modules/format_h264.so
%{_libdir}/asterisk/modules/format_siren14.so
%{_libdir}/asterisk/modules/format_siren7.so
%{_libdir}/asterisk/modules/format_sln16.so
%{_libdir}/asterisk/modules/func_aes.so
%{_libdir}/asterisk/modules/func_audiohookinherit.so
%{_libdir}/asterisk/modules/func_base64.so
%{_libdir}/asterisk/modules/func_blacklist.so
%{_libdir}/asterisk/modules/func_callcompletion.so
%{_libdir}/asterisk/modules/func_cdr.so
%{_libdir}/asterisk/modules/func_channel.so
%{_libdir}/asterisk/modules/func_config.so
%{_libdir}/asterisk/modules/func_cut.so
%{_libdir}/asterisk/modules/func_db.so
%{_libdir}/asterisk/modules/func_devstate.so
%{_libdir}/asterisk/modules/func_dialgroup.so
%{_libdir}/asterisk/modules/func_dialplan.so
%{_libdir}/asterisk/modules/func_env.so
%{_libdir}/asterisk/modules/func_extstate.so
%{_libdir}/asterisk/modules/func_frame_trace.so
%{_libdir}/asterisk/modules/func_global.so
%{_libdir}/asterisk/modules/func_groupcount.so
%{_libdir}/asterisk/modules/func_iconv.so
%{_libdir}/asterisk/modules/func_lock.so
%{_libdir}/asterisk/modules/func_logic.so
%{_libdir}/asterisk/modules/func_math.so
%{_libdir}/asterisk/modules/func_md5.so
%{_libdir}/asterisk/modules/func_module.so
%{_libdir}/asterisk/modules/func_pitchshift.so
%{_libdir}/asterisk/modules/func_rand.so
%{_libdir}/asterisk/modules/func_realtime.so
%{_libdir}/asterisk/modules/func_sha1.so
%{_libdir}/asterisk/modules/func_shell.so
%{_libdir}/asterisk/modules/func_sprintf.so
%{_libdir}/asterisk/modules/func_srv.so
%{_libdir}/asterisk/modules/func_strings.so
%{_libdir}/asterisk/modules/func_sysinfo.so
%{_libdir}/asterisk/modules/func_timeout.so
%{_libdir}/asterisk/modules/func_version.so
%{_libdir}/asterisk/modules/func_vmcount.so
%{_libdir}/asterisk/modules/func_volume.so
%{_libdir}/asterisk/modules/res_ael_share.so
%{_libdir}/asterisk/modules/res_calendar.so
%{_libdir}/asterisk/modules/res_clialiases.so
%{_libdir}/asterisk/modules/res_clioriginate.so
%{_libdir}/asterisk/modules/res_convert.so
%{_libdir}/asterisk/modules/res_limit.so
%{_libdir}/asterisk/modules/res_mutestream.so
%{_libdir}/asterisk/modules/res_phoneprov.so
%{_libdir}/asterisk/modules/res_realtime.so
%{_libdir}/asterisk/modules/res_rtp_asterisk.so
%{_libdir}/asterisk/modules/res_rtp_multicast.so
%{_libdir}/asterisk/modules/res_security_log.so
%{_libdir}/asterisk/modules/res_smdi.so
%{_libdir}/asterisk/modules/res_speech.so
%{_libdir}/asterisk/modules/res_stun_monitor.so
%{_libdir}/asterisk/modules/res_timing_dahdi.so
%{_libdir}/asterisk/modules/res_timing_pthread.so
%{_libdir}/asterisk/modules/res_timing_timerfd.so
%{_libdir}/asterisk/modules/app_sms.so
%{_libdir}/asterisk/modules/chan_oss.so
%{_libdir}/asterisk/modules/func_curl.so
%{_libdir}/asterisk/modules/func_speex.so
%{_libdir}/asterisk/modules/res_config_curl.so
%{_libdir}/asterisk/modules/res_config_pgsql.so
%{_libdir}/asterisk/modules/res_curl.so
%{_libdir}/asterisk/modules/res_srtp.so
############################################################

%attr(0755,root,root) %{_sbindir}/asterisk
%attr(0755,root,root) %{_sbindir}/safe_asterisk
%attr(0755,root,root) %{_sbindir}/astgenkey
#%attr(0755,root,root) %{_sbindir}/astman
#%attr(0755,root,root) %{_sbindir}/streamplayer
#%attr(0755,root,root) %{_sbindir}/stereorize
%attr(0755,root,root) %{_sbindir}/astcanary
%attr(0755,root,root) %{_sbindir}/rasterisk
%attr(0644,root,root) /var/asterisk/webapp/lib/version

# Sound files
%dir /var/lib/asterisk
%dir /var/lib/asterisk/sounds/en
/var/lib/asterisk/sounds/en/*.gsm
%dir /var/lib/asterisk/sounds/en/dictate
/var/lib/asterisk/sounds/en/dictate/*.gsm
%dir /var/lib/asterisk/sounds/en/digits
/var/lib/asterisk/sounds/en/digits/*.gsm
#%dir /var/lib/asterisk/sounds/en/enletters
#/var/lib/asterisk/sounds/en/letters/*.gsm
%dir /var/lib/asterisk/sounds/en/phonetic
/var/lib/asterisk/sounds/en/phonetic/*.gsm
%dir /var/lib/asterisk/sounds/en/silence
/var/lib/asterisk/sounds/en/silence/*.gsm
%dir /var/lib/asterisk/images
/var/lib/asterisk/images/*
#%dir /var/lib/asterisk/keys
#/var/lib/asterisk/keys/*
#%dir /var/lib/asterisk/agi-bin
#%attr(0755,asterisk,asterisk) /var/lib/asterisk/agi-bin/*
%dir /var/lib/asterisk/sounds/en/letters
/var/lib/asterisk/sounds/en/letters/*.gsm
%dir /var/lib/asterisk/sounds/en/followme
/var/lib/asterisk/sounds/en/followme/*.gsm

%dir /var/lib/asterisk/sounds/ja
%dir /var/lib/asterisk/sounds/ja/*
%dir /var/lib/asterisk/sounds/ja/dictate
%dir /var/lib/asterisk/sounds/ja/dictate/*
%dir /var/lib/asterisk/sounds/ja/digits
%dir /var/lib/asterisk/sounds/ja/digits/*

####################################################
#%dir /var/lib/asterisk
#%dir /var/lib/asterisk/sounds
#/var/lib/asterisk/sounds/*.gsm
#%dir /var/lib/asterisk/sounds/dictate
#/var/lib/asterisk/sounds/dictate/*.gsm
#%dir /var/lib/asterisk/sounds/digits
#/var/lib/asterisk/sounds/digits/*.gsm
#%dir /var/lib/asterisk/sounds/letters
#/var/lib/asterisk/sounds/letters/*.gsm
#%dir /var/lib/asterisk/sounds/phonetic
#/var/lib/asterisk/sounds/phonetic/*.gsm
#%dir /var/lib/asterisk/sounds/silence
#/var/lib/asterisk/sounds/silence/*.gsm
#%dir /var/lib/asterisk/images
#/var/lib/asterisk/images/*
#%dir /var/lib/asterisk/keys
#/var/lib/asterisk/keys/*
#%dir /var/lib/asterisk/agi-bin
#%attr(0755,asterisk,asterisk) /var/lib/asterisk/agi-bin/*
####################################################


# Firmware
%dir /var/lib/asterisk/firmware
%dir /var/lib/asterisk/firmware/iax
#%attr(0755,root,root)      /var/lib/asterisk/firmware/iax/*.bin

# Music On Hold
%dir /var/lib/asterisk/moh-files
%attr(0755,apache,asterisk) /var/lib/asterisk/moh-files/*
%dir /var/lib/asterisk/moh
%attr(0755,apache,asterisk) /var/lib/asterisk/moh/*

%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_a
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_a/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_b
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_b/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_c
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_c/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_d
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_d/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_e
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_e/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_f
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_f/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_g
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_g/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_h
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_h/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_i
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_i/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_j
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_j/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_k
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_k/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_l
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_l/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_m
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_m/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_n
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_n/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_o
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_o/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_p
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_p/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_q
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_q/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_r
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_r/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_s
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_s/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_t
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_t/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_u
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_u/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_v
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_v/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_w
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_w/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_x
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_x/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_y
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_y/*
%attr(0755,apache,asterisk) %dir /var/lib/asterisk/moh_z
%attr(0755,apache,asterisk) /var/lib/asterisk/moh_z/*

# documentation
%dir /var/lib/asterisk/documentation
/var/lib/asterisk/documentation/*

#%dir /var/lib/asterisk/mohmp3
#/var/lib/asterisk/mohmp3/*

#
# Log
#
%attr(0750,asterisk,asterisk) %dir /var/log/asterisk

# spool
%attr(0755,asterisk,asterisk) %dir /var/spool/asterisk
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/outgoing
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/dictate
%attr(0750,asterisk,asterisk) %dir /var/spool/asterisk/voicemail

# socket file and pid file
%attr(0750,asterisk,asterisk) %dir /var/run/asterisk

# Man page
%attr(0644,root,root) %{_mandir}/man8/*.gz

%files devel
%defattr(0644,root,root,0755)
#
# Include files
#
%dir %{_includedir}/asterisk
%{_includedir}/asterisk/*.h
%{_includedir}/asterisk.h

%files adsi
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/adsi.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/*.adsi
%{_libdir}/asterisk/modules/app_adsiprog.so
%{_libdir}/asterisk/modules/app_getcpeid.so
%{_libdir}/asterisk/modules/res_adsi.so

%files alarmreceiver
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/alarmreceiver.conf
%{_libdir}/asterisk/modules/app_alarmreceiver.so

%files alsa
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/alsa.conf
%{_libdir}/asterisk/modules/chan_alsa.so

#%if %{enable_fax}
#%files fax
#%defattr(0644,asterisk,asterisk,0755)
#%{_libdir}/asterisk/modules/app_fax.so
#%endif

%files festival
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/festival.conf
%{_libdir}/asterisk/modules/app_festival.so

%if %enable_h323
%files h323
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/chan_h323.so
%endif

%files skinny
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/skinny.conf
%{_libdir}/asterisk/modules/chan_skinny.so

%files cdr
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_manager.conf
%{_libdir}/asterisk/modules/app_cdr.so
%{_libdir}/asterisk/modules/app_forkcdr.so
#%{_libdir}/asterisk/modules/app_setcdruserfield.so
%{_libdir}/asterisk/modules/cdr_manager.so
%{_libdir}/asterisk/modules/cdr_csv.so
%dir /var/log/asterisk/cdr-csv
/var/log/asterisk/cdr-csv/Master.csv

%files cdr-custom
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/cdr_custom.so
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_custom.conf
%dir /var/log/asterisk/cdr-custom
/var/log/asterisk/cdr-custom/Master.csv

#%files cdr-odbc
#%defattr(0644,asterisk,asterisk,0755)
#%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_odbc.conf
#%{_libdir}/asterisk/modules/cdr_odbc.so

%files cdr-pgsql
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_pgsql.conf
%{_libdir}/asterisk/modules/cdr_pgsql.so
%{_libdir}/asterisk/modules/cel_pgsql.so

%if %enable_sqlite
%files cdr-sqlite
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/cdr_sqlite.so
%endif

%if %enable_tds
%files cdr-tds
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/cdr_tds.conf
%{_libdir}/asterisk/modules/cdr_tds.so
%else
%exclude %{_sysconfdir}/asterisk/cdr_tds.conf
%endif

%files chanspy
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_chanspy.so

%files disa
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_disa.so

%files dundi
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/dundi.conf
%{_libdir}/asterisk/modules/pbx_dundi.so

%files ices
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_ices.so

%files meetme
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/meetme.conf
%{_libdir}/asterisk/modules/app_meetme.so
%dir /var/spool/asterisk/meetme

%files mgcp
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/mgcp.conf
%{_libdir}/asterisk/modules/chan_mgcp.so

%if %{enable_misdn}
%files misdn
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/misdn.conf
%{_libdir}/asterisk/modules/chan_misdn.so
%else
%exclude %{_sysconfdir}/asterisk/misdn.conf
%endif

%files modem
%defattr(0644,asterisk,asterisk,0755)
#%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/modem.conf
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/oss.conf
#%{_libdir}/asterisk/modules/chan_modem.so
#%{_libdir}/asterisk/modules/chan_modem_aopen.so
#%{_libdir}/asterisk/modules/chan_modem_bestdata.so
#%{_libdir}/asterisk/modules/chan_modem_i4l.so
#%{_libdir}/asterisk/modules/chan_oss.so

%files monitor
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/res_monitor.so
%{_libdir}/asterisk/modules/app_mixmonitor.so
%attr(0755,asterisk,asterisk) %dir /var/spool/asterisk/monitor

%if %enable_mp3
%files mp3
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_mp3.so
%else
%exclude %{_libdir}/asterisk/modules/app_mp3.so
%endif

%files nbscat
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_nbscat.so

%if %enable_osp
%files osp
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/osp.conf
%{_libdir}/asterisk/modules/app_osplookup.so
%{_libdir}/asterisk/modules/res_osp.so
%else
%exclude %{_sysconfdir}/asterisk/osp.conf
%endif

%files page
%defattr(0644,asterisk,asterisk,0755)
%{_libdir}/asterisk/modules/app_page.so

%files queue
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/queues.conf
%{_libdir}/asterisk/modules/app_queue.so

%files agent
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/agents.conf
%{_libdir}/asterisk/modules/chan_agent.so

#%if %enable_rpt
#%files rpt
#%defattr(0644,asterisk,asterisk,0755)
#%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/rpt.conf
#%{_libdir}/asterisk/modules/app_rpt.so
#%else
#%exclude %{_sysconfdir}/asterisk/rpt.conf
#%endif

#%files sms
#%defattr(0644,asterisk,asterisk,0755)
#%{_libdir}/asterisk/modules/app_sms.so
#%attr(0755,root,root) %{_sbindir}/smsq

#%files valetparking
#%defattr(0644,asterisk,asterisk,0755)
#%{_libdir}/asterisk/modules/app_valetparking.so

%files voicemail
%defattr(0644,asterisk,asterisk,0755)
%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/voicemail.conf
%{_libdir}/asterisk/modules/app_voicemail.so
#%{_libdir}/asterisk/modules/app_hasnewvoicemail.so
%{_libdir}/asterisk/modules/app_directory.so
%dir /var/spool/asterisk/voicemail
%dir /var/spool/asterisk/voicemail/default
%dir /var/spool/asterisk/voicemail/default/1234/en
/var/spool/asterisk/voicemail/default/1234/en/*.gsm

#%if %enable_vpb
#%files vpb
#%defattr(0644,asterisk,asterisk,0755)
#%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/vpb.conf
#%{_libdir}/asterisk/modules/chan_vpb.so
#%else
#%exclude %{_sysconfdir}/asterisk/vpb.conf
#%endif

%files zap
%defattr(0644,asterisk,asterisk,0755)
#%config(noreplace) %attr(0750,root,asterisk) %{_sysconfdir}/asterisk/zapata.conf
%{_libdir}/asterisk/modules/app_flash.so
%{_libdir}/asterisk/modules/app_zapateller.so
#%{_libdir}/asterisk/modules/app_zapbarge.so
#%{_libdir}/asterisk/modules/app_zapras.so
#%{_libdir}/asterisk/modules/app_zapscan.so
#%{_libdir}/asterisk/modules/chan_zap.so
#%{_libdir}/asterisk/modules/codec_zap.so

%changelog
* Mon Aug 04 2014 K.Kobayashi <kkobayashi@infinitalk.co.jp> - 1.8.13.0-f0.18
- Added moh directories 

* Wed Jun 11 2013 K.Kobayashi <kkobayashi@infinitalk.co.jp> - 1.8.13.0-r0.1
- Added version file 

