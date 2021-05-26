#!/usr/bin/env python3

# 2021/05 BuRnCycL
# Script detects if sound crosses certain decibal threshold. Uses Root-Mean-Squared and some normalization to make determination.
# Threshold is set using self.ambient_db variable.
# External Dependencies # apt install vlc portaudio19-dev pulseaudio libatlas-base-dev
# Dependencies # pip3 install python-vlc numpy pyaudio

import pyaudio as pa
import numpy as np
import datetime, vlc
from threading import Thread
from time import sleep

class DetectDogBark:
    def __init__(self):
        # PyAudio Variables.
        self.device = None
        self.paud = pa.PyAudio()
        self.format = pa.paInt16
        self.channels = 1 # This may need to be lowered depending on the device used.
        self.rate = 48000 # This may need to be tuned to 48000Hz
        self.chunk = 1024 # This may need to be tuned to 512, 2048, or 4096.
        self.loop = None # Pulse from both ends of the strip. Default None, self.main() sets this.
        self.sensitivity = 1.3 # Sensitivity to sound.
        self.sample_rate = 1024

        # Declare variables, not war.  
        self.ambient_db = 10200 # Define the ambient db threshold.

        # VLC
        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()

        # Lock
        self.lock = False # Default Lock to False.
        self.count = 0

        # Get Audio Stream
        self.audio_stream = self.input_device() # Init microphone as input source/stream.
        self.audio = self.analyze_audio(self.audio_stream, num_samples=self.sample_rate) # Read the audio stream.

    def input_device(self): # i.e. Microphone
        if self.device is not None: # Use non-default device.
            audio_stream = self.paud.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                frames_per_buffer=self.chunk,
                input= True,
                input_device_index=self.device,
                )
        else: # Otherwise, use the default.
            audio_stream = self.paud.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                frames_per_buffer=self.chunk,
                input= True,
                )
        return(audio_stream)

    def analyze_audio(self, audio_stream, num_samples):                
        while True:
            samples = audio_stream.read(num_samples, exception_on_overflow=False)
            samps = np.frombuffer(samples, dtype=np.int16)
            volume = np.sqrt(np.mean(samps.astype(np.dtype(np.int64)) ** 2 )) # Calculate and normalize RMS
            #print('{:2f}'.format(volume)) # Format the volume output so it only # displays at most six numbers behind 0. # Debugging
            current_time = datetime.datetime.now()
            if self.count <= 1:
                if volume >= self.ambient_db:
                    self.count += 1
                    print(f'{current_time} - Audio Crossed Threshold.')
                    if self.lock == True:
                        print(f'{current_time} - Sound already playing.')
                    elif self.lock == False:
                        Thread(target=self.play_sound).start()
                elif volume < self.ambient_db:
                    #print(f'{current_time} - Normal Ambient Sound.')
                    continue
            elif self.count >= 1:
                wait_time = 10
                print(f'{current_time} - Waiting {wait_time} seconds.')
                sleep(wait_time)

    def play_sound(self):
        self.lock = True
        sounds = ['Dog-whistle-sound-16.000-Hz.wav', 'Dog-whistle-sound-20.000-Hz.wav']
        #sounds = ['Dog-whistle-sound-11.200-Hz.wav', 'Dog-whistle-sound-12.200-Hz.wav', 'Dog-whistle-sound-16.000-Hz.wav', 'Dog-whistle-sound-20.000-Hz.wav']
        #sounds = ['./notify1.wav', './notify2.wav'] # Used for Testing.
        for sound in sounds:
            media = self.vlc_instance.media_new(sound)
            self.player.set_media(media)
            self.player.play()
            sleep(0.5) # Breathe before playing next sound.
        self.count = 0
        self.lock = False

DetectDogBark()
