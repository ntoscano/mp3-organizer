import os #imports os functions
import eyed3 #imports eyed3 functions
import errno
import shutil

root_folder = '/Users/ntoscano/Desktop/mp3-organizer'

files = os.listdir(root_folder) #lists all files in specified directory


for file_name in files:
    if file_name.endswith('.mp3'): #if file ends with ".mp3" it continues onto the next line
        
        abs_location = '%s/%s' % (root_folder, file_name)
        
        song_info = eyed3.load(abs_location) #loads each file into eyed3 and assignes the return value to song_info
        if song_info is None:
            print 'Skippig %s' % abs_location
            continue
        try:
            os.mkdir(os.path.expanduser('~/Desktop/mp3-organizer/%s' % song_info.tag.artist))
        except OSError as e:
            if e.errno!= errno.EEXIST:
                raise
        print song_info
        print song_info.tag.artist
        shutil.move('%s' % file_name, '%s' % song_info.tag.artist)
    else:
        pass
