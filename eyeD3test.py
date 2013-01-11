import os #imports os functions
import eyed3 #imports eyed3 functions
import errno
import shutil

os.curdir

root_folder = os.path.realpath(os.curdir)

print root_folder

files = os.listdir(root_folder) #lists all files in specified directory


for file_name in files:
    if file_name.endswith('.mp3'): #if file ends with ".mp3" it continues onto the next line
        
        abs_location = '%s/%s' % (root_folder, file_name)
        
        try:
            song_info = eyed3.load(abs_location) #loads each file into eyed3 and assignes the return value to song_info
        except IOError:
            pass
        if song_info.tag is None:
            print 'Skipping %s' % abs_location
            continue
        if song_info is None:
            print 'Skipping %s' % abs_location
            continue
            print 'Skipping %s' % abs_location
            continue
        try:
            artist_folder = os.path.join(root_folder, '%s' % song_info.tag.artist)
            os.mkdir(artist_folder)
        except OSError as e:
            if e.errno!= errno.EEXIST:
                raise
        except UnicodeDecodeError:
            pass
        try:
            album_folder = os.path.join(artist_folder, '%s' %song_info.tag.album)
            os.mkdir(album_folder)
        except OSError as e:
            if e.errno!= errno.EEXIST:
                raise
        except OSError:
                continue
        print song_info
        print song_info.tag.artist
        try :
            shutil.move('%s' % file_name, '%s/%s' % (song_info.tag.artist, song_info.tag.album))
        except UnicodeDecodeError:
            pass
        except shutil.Error:
            try:
                os.renames('%s' % file_name, '%s_%s' % (file_name, song_info.tag.artist))
            except OSError:
                pass
    else:
        pass

#improvements
    #have this work on other computers