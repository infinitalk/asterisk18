#!/bin/sh

AST_VER=1.8.13.0
AST_SPECFILE=asterisk.spec

SELF_DIR=`pwd`
AST_SRC=$SELF_DIR/asterisk
AST_RPMBUILD_ROOT=$SELF_DIR/rpmbuild
AST_RPMBUILD_SOURCE=$AST_RPMBUILD_ROOT/SOURCES
AST_RPMBUILD_SPECS=$AST_RPMBUILD_ROOT/SPECS
AST_RPMBUILD_ASTSRC=$AST_RPMBUILD_SOURCE/asterisk-$AST_VER

AST_SPECFILE=$AST_RPMBUILD_SPECS/asterisk.spec


#初期化
rm -rf $AST_RPMBUILD_ROOT/BUILD
rm -rf $AST_RPMBUILD_ROOT/BUILDROOT
rm -rf $AST_RPMBUILD_ROOT/RPMS
rm -rf $AST_RPMBUILD_ROOT/SRPMS
rm -rf $AST_RPMBUILD_SOURCE*/ > /dev/null 2>&1
rm -rf $AST_RPMBUILD_SOURCE/asterisk*.tar.gz > /dev/null 2>&1

#ソースコードのコピー
mkdir -p $AST_RPMBUILD_ASTSRC
cp -arp $AST_SRC/* $AST_RPMBUILD_ASTSRC

#不要SVN管理ファイルの削除
find $AST_RPMBUILD_ASTSRC -name .svn -exec rm -fr {} \;

#圧縮ファイル作成
chmod 755 -R $AST_RPMBUILD_ASTSRC
echo "1" > $AST_RPMBUILD_ASTSRC/.cleancount
cd $AST_RPMBUILD_SOURCE
tar cvfz ./asterisk-$AST_VER.tar.gz ./asterisk-$AST_VER
rm -rf $AST_RPMBUILD_ASTSRC > /dev/null 2>&1

#rpm作成環境作成
mkdir -p $AST_RPMBUILD_ROOT/BUILD
mkdir -p $AST_RPMBUILD_ROOT/BUILDROOT
mkdir -p $AST_RPMBUILD_ROOT/RPMS
mkdir -p $AST_RPMBUILD_ROOT/SRPMS

#rpm作成
cd $AST_RPMBUILD_SPECS
rpmbuild --define "_topdir ${AST_RPMBUILD_ROOT}" -ba $AST_SPECFILE
