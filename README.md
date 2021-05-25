### 2021/05 BuRnCycL

Script use Root-Mean-Squared and some normalization to detect sound "loudness". This triggers VLC method to play sounds. These sounds can be Dog Whistles at different frequencies. 


Assumes you're running Ubuntu 18.04+ or Raspberry Pi Buster

### Installation
Install package manager maintained dependencies 
```
sudo ./install.sh
```

### Run Python Virtual Environment
```
source ./init.sh
```

### Run Script
```
python3 detect_barks.py
```

### Known Issues
If you get the following error
```
vlcpulse audio output error: PulseAudio server connection failure: Connection refused
```
Try killing and restarting Pulse Audio with the following script.
```
./bounce_pulseaudio.sh
```
