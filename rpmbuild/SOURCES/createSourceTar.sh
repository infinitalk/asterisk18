#!/bin/sh
SVN_TARGET=http://yc2.infinitalk.co.jp/svn/asterisk18-fork/trunk/asterisk
SOURCE_ASTERISK_DIR=asterisk-1.8.13.0
rm -rf $SOURCE_ASTERISK_DIR > /dev/null 2>&1
rm -rf $SOURCE_ASTERISK_DIR.tar.gz > /dev/null 2>&1
svn co $SVN_TARGET $SOURCE_ASTERISK_DIR
find  $SOURCE_ASTERISK_DIR -name .svn -exec rm -fr {} \;
chmod 755 -R $SOURCE_ASTERISK_DIR
echo "1" > $SOURCE_ASTERISK_DIR/.cleancount
tar cvfz $SOURCE_ASTERISK_DIR.tar.gz $SOURCE_ASTERISK_DIR
rm -rf $SOURCE_ASTERISK_DIR > /dev/null 2>&1
