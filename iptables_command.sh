#/bin/bash
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
