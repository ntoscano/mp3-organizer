import os #imports os functions
import eyed3 #imports eyed3 functions
import errno
import shutil

def question(root_folder):
    files = os.listdir(root_folder) #lists all files in specified directory
    print '''Organize methods
    1.artist/album
    2.artit'''
    print'''
    
    1 or 2'''
    
    O_method = raw_input('> ')
    if '1' in O_method:
        for file_name in files:
            if file_name.endswith('.mp3'): #if file ends with ".mp3" it continues onto the next line
                
                abs_location = '%s/%s' % (root_folder, file_name)
                
                try:
                    song_info = eyed3.load(abs_location) #loads each file into eyed3 and assignes the return value to song_info
                except IOError:
                    pass
                if song_info.tag is None:
                    print 'Skipping %s' % file_name
                    continue
                if song_info is None:
                    print 'Skipping %s' % file_name
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
                print file_name
                print song_info.tag.artist
                try :
                    source_folder = ('%s' % file_name)
                    dest_folder = ('%s/%s' % (song_info.tag.artist, song_info.tag.album))
                    shutil.move(source_folder, dest_folder)
                except UnicodeDecodeError:
                    pass
                except shutil.Error:
                    try:
                        OG_name = '%s' % file_name
                        new_name = '%s_%s.mp3' % (song_info.tag.title, song_info.tag.artist)
                        os.renames(OG_name, new_name)
                    except OSError:
                        pass
            else:
                pass
    elif '2' in O_method:
        for file_name in files:
            if file_name.endswith('.mp3'): #if file ends with ".mp3" it continues onto the next line
                
                abs_location = '%s/%s' % (root_folder, file_name)
                
                try:
                    song_info = eyed3.load(abs_location) #loads each file into eyed3 and assignes the return value to song_info
                except IOError:
                    pass
                if song_info.tag is None:
                    print 'Skipping %s' % file_name
                    continue
                if song_info is None:
                    print 'Skipping %s' % file_name
                    continue
                try:
                    artist_folder = os.path.join(root_folder, '%s' % song_info.tag.artist)
                    os.mkdir(artist_folder)
                except OSError as e:
                    if e.errno!= errno.EEXIST:
                        raise
                except UnicodeDecodeError:
                    pass
                print file_name
                print song_info.tag.artist
                try :
                    source_folder = ('%s' % file_name)
                    dest_folder = ('%s/' % song_info.tag.artist)
                    shutil.move(source_folder, dest_folder)
                except UnicodeDecodeError:
                    pass
                except shutil.Error:
                    try:
                        OG_name = '%s' % file_name
                        new_name = '%s_%s.mp3' % (song_info.tag.title, song_info.tag.artist)
                        os.renames(OG_name, new_name)
                    except OSError:
                        pass
            else:
                pass
    else:
        return 'question'

if __name__ == "__main__":
    root_folder = os.path.realpath(os.curdir)
    question(root_folder)

