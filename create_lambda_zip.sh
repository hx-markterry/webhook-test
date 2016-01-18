#!/bin/bash
set -e

SYSTEM=`uname -m -s`

if [ "${SYSTEM}" != "Linux x86_64" ]; then
  echo "Must be run on 64 bit linux"
  exit 1
fi

rm -f lambda_bundle.zip
rm -rf build
mkdir build

pip install -t build --requirement=requirements.txt

cp -av src/*.py build/

cd build
zip -qr ../lambda_bundle.zip *
unzip -l ../lambda_bundle.zip