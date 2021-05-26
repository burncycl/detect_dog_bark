### 2021/05 BuRnCycL

Script use Root-Mean-Squared and some normalization to detect sound "loudness". This triggers VLC method to play sounds. These sounds can be Dog Whistles at different frequencies. 

Use self.ambient_db to set the threshold for playing dog whistle. 

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

### Normaliztion  
Reference: https://stackoverflow.com/questions/40963659/root-mean-square-of-a-function-in-python

"Warning: in numpy, if the number are too big in comparison of their type (dtype in python), the power function may return negative values. To avoid this, it is sometimes useful to cast the values. Example: >>np.sqrt(np.mean(y.astype(np.dtype(np.int64)) ** 2 )). Not very nice in the code, but it will do the work!"

### Known Issues
If you get the following error
```
vlcpulse audio output error: PulseAudio server connection failure: Connection refused
```
Try killing and restarting Pulse Audio with the following script.
```
./bounce_pulseaudio.sh
```
