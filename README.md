# MyPwnLib
> Author: 堇姬Naup

## 描述
CTF模板，包含Pwn跟Crypto

## 下載
```
git clone https://github.com/Naupjjin/MyCTFLib.git
cd MyCTFLib
chmod +x init.sh
./init.sh
```

## use PwnLib
```
cd MyCTFLib
./copyPWNLIB.sh
cd ../
```

## use CryptoLib
```
cd MyCTFLib
./copyCRYPTOLIB.sh
cd ../
```

## use WebLib
```
cd MyCTFLib
./copyWEBLIB.sh
cd ../
```

## lib intro
```
MyCTFLib
├── copyCRYPTOLIB.sh
├── copyPWNLIB.sh
├── copyWEBLIB.sh
├── init.sh
├── MyCryptoLib
│   ├── Block_cipher_lib.py
│   ├── exploit.py
│   ├── MATH_lib.py
│   ├── MT19937_lib.py
│   ├── RSA_lib.py
│   └── wiener.py
├── MyPwnLib
│   ├── exploit.py
│   ├── NAUP_pwn_lib.py
│   └── NAUP_shellcode_lib.py
├── MyWebLib
│   ├── exploit.py
│   └── php_filter_chain.py
└── README.md
```