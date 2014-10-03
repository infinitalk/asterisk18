#!/bin/sh
SODIR=sofiles
rm -rf $SODIR
mkdir $SODIR
for x in `find . -name '*.so'` ; do
	/bin/cp -pf $x $SODIR/. ;
done
