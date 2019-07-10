import paramiko
import os
import sys

pathRoot = os.getcwd()
source = os.path.join( pathRoot, 'upload' )
source = os.path.join( source, 'files.zip' )
dest = '/home/ubuntu/'

keyRSA = os.path.join( pathRoot, 'keyAws.pem' )
hostname = "ec2-52-55-113-15.compute-1.amazonaws.com"
port = '22'
username = "ubuntu"

try:
    keyConnect = paramiko.RSAKey.from_private_key_file( keyRSA )
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect( hostname = hostname, username = username, pkey = keyConnect )

    sftp = client.open_sftp()
    sftp.put(source, dest)

    stdin, stdout, stderr = client.exec_command('pwd')
    print(stdout.read())

finally:
    print("connected")
    client.close()
    sftp.close()

