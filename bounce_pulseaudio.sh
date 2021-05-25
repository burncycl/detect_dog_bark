#!/bin/bash

echo "Stopping Pulseaudio..."
pkill pulseaudio
sleep 1
echo "Loading Pulseaudio..."
pulseaudio --start --verbose
ps -ef|grep pulseaudio
