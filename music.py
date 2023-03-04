import os

def music(dir):
    songs = os.listdir(dir)
    print(songs)    
    os.startfile(os.path.join(dir, songs[0]))