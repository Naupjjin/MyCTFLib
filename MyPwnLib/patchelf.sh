#!/bin/bash

read -p "Your libc and ld version： " VERSION

chmod +x libc-${VERSION}.so
chmod +x ld-${VERSION}.so

echo "**success chmod**"
ls

read -p "Your binary name： " BINARY

patchelf --set-interpreter ./ld-${VERSION}.so ${BINARY}
patchelf --replace-needed libc.so.6 ./libc-${VERSION}.so ${BINARY}