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

## lib intro
```
MyCTFLib/
├── copyPWNLIB.sh
├── init.sh
├── MyCryptoLib
│   ├── exploit.py
│   ├── NAUP_crypto_lib.py
│   └── wiener.py
├── MyPwnLib
│   ├── exploit.py
│   ├── NAUP_pwn_lib.py
│   └── NAUP_shellcode_lib.py
└── README.md
```