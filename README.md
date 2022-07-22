# Pi-GPIORadio
A python script for triggering the transmission of music and microphone input via FM radio using the GPIO pins on the Raspberry Pi

![IMG02353_adjusted-small](https://user-images.githubusercontent.com/31896499/180519314-4597c4e5-b7a1-4426-a86b-2e21af184e12.jpg)

## How it works

The script checks for input on three different GPIO pins and executes the according command if one of them is connected to ground.
The command is issued inside a screen session so that the transmission can be stopped conveniently.
If you connect the so called "terminatior" pin to ground, the screen session will be killed and the transmission will stop.
The pin assignment and the overall procedure is of course customizable.
It supports:

- Transmission of audio files (in this case .mp3s)
- Transmission of microphone input (USB microphone)
- Control via GPIO pins



## Default GPIO pin assignment

![gpio_default](https://user-images.githubusercontent.com/31896499/180562076-a1ccdac4-e822-4c91-8bf3-493cfec72d38.jpg)

GPIO.21 - Music transmission

GPIO.20 - Microphone input transmission

GPIO.26 - Terminator (Stop transmission)




## Prerequisites/Dependencies

In order for this script to work you'll want to have Python, ffmpeg, screen & git installed on your system.
Python is included in Raspberry Pi OS so you'll only have to install the ffmpeg, screen & git packages.
Do so by issuing the following command in a terminal on your Pi:
```
sudo apt update && sudo apt install ffmpeg screen git
```
Confirm by typing "y" and pressing enter if asked for confirmation.

You will also have to download the "pifm" package by "omattos" which is described in the Instructions section down below.

For better transmission range you can connect/solder a wire to Pin 8 (GPIO4) on the Pi.
If you happen to have a broken radio lying around, you could salvage the antenna and mount it onto your Pi like I did with my Zero W.

> Note: ffmpeg is needed for transmission of .mp3 files because pifm only supports .wav files by default.


## Instructions

1. Clone this repository
```
git clone https://github.com/nohouse-felix/pi-gpioradio.git
```

2. Change directory to the "pi-gpioradio" folder
```
$ cd pi-gpioradio
```

3. Download the "pifm" package
```
wget https://omattos.com/pifm.tar.gz
```

4. Extract the package
```
tar -xzvf pifm.tar.gz
```

5. Verify the new files by typing
```
ls -la
```


6. Modify the "pi-gpioradio" script if you wish to change the GPIO pins or something else
```
nano script.py
```
***IMPORTANT:*** The script assumes that you are using the default "pi" user.

Be sure to modify the directory paths in the script if you use a different user account!

Simply change the numbers of the GPIO pins to different ones if you wish to use different pins.
You can also alter the directory in which the script looks for .mp3 files.

7. Connect a wire or an antenna to Pin 8 (GPIO4) on your Raspberry Pi for better transmission range.

8. Populate the "pi-gpioradio" folder with .mp3 files

Make sure to copy your songs and recordings over to the "pi-gpioradio" folder.
You can also specify a different path in the script and use that for storing your music.

9. Make the "pi-gpioradio" script execute at boot
```
sudo nano /etc/rclocal
```
One line above the "exit 0" string, insert the following:
```
python /home/pi/pi-gpioradio/script.py
```
*Note:* Be sure to change this if you don't use the default "pi" user!

10. Reboot

11. Done!
Grab a wire or something else suitable to connect the pins and give it a test.
Be sure to terminate the transmission before you switch from music to microphone transmission or the other way around!
Make sure to tune your receiving device to the correct frequency.
If you didn't change it, it's 99.8
