#!/bin/bash
sudo apt-get update

sudo apt-get install -y python3 python3-pip

pip3 install gmpy2 pycryptodome pwntools

chmod +x copyCRYPTOLIB.sh

chmod +x copyPWNLIB.sh

chmod +x copyWEBLIB.sh