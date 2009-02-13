#!/bin/bash
if [[ $1 = "" ]] ; then
echo "Please supply the version as a parameter."
echo "For example:"
echo "\$ sh snowballz-snapshot.sh 1.0-beta1"
exit 1
else
version=$1
fi
echo "Version set to $version..."

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
hg=$(date +%Y%m%d)hg
name=snowballz

cd "$tmp"
hg clone http://freehg.org/u/joey/snowballz/
rm -fr $name/.hg*
# Removing the shipped fonts
# No fonts are allowed in Fedora in non-font packages
rm $name/data/*.ttf
tar jcf "$pwd"/$name-$version.$hg.tar.bz2 $name
echo "Written: $name-$version-$hg.tar.bz2"
cd - >/dev/null
