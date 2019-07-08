#$pip install paramiko os
import paramiko
import os
import sys

pathRoot = os.getcwd()

HOSTNAME = 'ssh.ec2-52-55-113-15.compute-1.amazonaws.com'
USERNAME = 'ubuntu'
KEY_FILE = os.path.join( pathRoot, 'key-semparar-server-dsa.ppk' )


system(cd /var/www/html/)
scp -i <key_path> -r * root@<my_local_machine_public_ip:~/var/www/html/
