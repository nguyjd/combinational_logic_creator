import simpleaudio
import pathlib
import random
import glob

def PlayMusic():

    # Location of the Music player file
    file_loc = str(pathlib.Path(__file__).parent.resolve())
    while True:
        music_list = glob.glob(f'{file_loc}/audio/*.wav')
        
        if len(music_list) != 0:

            # Select a random beat
            music_index = random.randrange(len(music_list))
            music = simpleaudio.WaveObject.from_wave_file(music_list[music_index])

            # Play and wait until its over.
            player = music.play()
            player.wait_done()