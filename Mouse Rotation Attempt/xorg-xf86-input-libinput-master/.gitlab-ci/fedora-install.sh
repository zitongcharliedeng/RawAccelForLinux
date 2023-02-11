#!/bin/bash

# we require at least inputproto >= 2.3.99.1 which has been released in xorgproto 2021.5
git clone https://gitlab.freedesktop.org/xorg/proto/xorgproto.git --depth 1 --branch=xorgproto-2021.5
pushd xorgproto
./autogen.sh
make -j${FDO_CI_CONCURRENT:-4} install
popd
rm -rf xorgproto
