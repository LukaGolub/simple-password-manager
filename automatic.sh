echo "1.) Instalacija biblioteka"
sudo apt install python3-pycryptodome -y
echo "Instalacija završena."

echo -e "2.) Demonstracija rada"
python3 <<EOF
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import sys
import os

EOF


echo "Pokretanje testnog scenarija..."

python3 lab1.py <<EOF
put lab1mp google.com 123 
get lab1mp google.com
put lab1mp google.com 12345
get lab1mp google.com
put lab1mp instagram.com sifra
get lab1mp instagram.com sifra
put labospas instagram.com provjera
get labospas google.com
uzmi labmp1 google.com
get lab1mp facebook.com
exit
EOF

echo -e "\nDemonstracija završena"