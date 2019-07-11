import paramiko
import os
import sys
import shutil
import time

pathRoot = os.getcwd()
source = os.path.join( pathRoot, 'upload' )
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

    try:
        sftp.chdir( dest )
    except IOError:
        sftp.mkdir( dest )
        sftp.chdir( dest )

    for root, dirs, files in os.walk( source ):
        for fname in files:
            full_fname = os.path.join( root, fname )
            sftp.put( full_fname, os.path.join( dest, fname ) )

    sftp.put( source, os.path.join( dest, 'files.zip' ) )
    #stdin, stdout, stderr = client.exec_command('ls -a')
    
    #print(stdout.read())
    print("-----------------connected-----------------")
finally:
    client.close()
    sftp.close()
    print("-----------------Close-----------------")
    time.sleep(3)
    shutil.rmtree( source )
    print("-----------------Remove Folder Upload-----------------")
