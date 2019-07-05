import os, shutil
from datetime import datetime

pathRoot = os.getcwd()
source = os.path.join( pathRoot, 'files' )
destination = os.path.join( pathRoot, 'upload/files.zip' )

def zipAll( source, destination ):
    base = os.path.basename( destination )
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname( source )
    archive_to = os.path.basename( source.strip( os.sep ) )
    print( source, destination, archive_from, archive_to )
    shutil.make_archive( name, format, archive_from, archive_to )
    shutil.move( '%s.%s'%( name,format ), destination )

zipAll( source, destination )