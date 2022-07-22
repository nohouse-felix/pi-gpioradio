from gpiozero import Button
import time
import os

## Here we define which button is linked to which GPIO Pin
## We also give them a friendlier name
## You can adjust this to your liking & needs
music_but	= Button(21)
mic_but		= Button(20)
term_but	= Button(26)


while True:
	
    ## If this button is pressed, the music transmission will begin
    if music_but.is_pressed:
        ## button needs to be pressed for one second to trigger the rest of the script
        time.sleep(1)
        
		if music_but.is_pressed:
            
            ## create a detached screen session with the name "radio"
            ## if you change the session name you'll have to change all further lines in this script as well
			os.system("screen -dmS radio")
			time.sleep(1)
            
            ## changes the directory inside the screen session to "/home/pi/pi-gpioradio"
			os.system("screen -S radio -X stuff 'cd /home/pi/pi-gpioradio^M'")
			time.sleep(1)
            
            ## triggers the transmission of the .mp3 files inside the pi-radio folder
            ## REMINDER: the frequency which is defined here can be changed to your liking (~80-100)
			os.system("screen -S radio -X stuff 'ffmpeg -i *.mp3 -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - 99.8^M'")
			time.sleep(5)



    ## If this button is pressed, the microphone input will be transmitted in real time.
	## Be sure to alter the "plughw:" parameter if you have connected multiple audio devices.
    ## Usually this doesn't need to be changed but it could be neccesary.
    ## Check your audio devices by typing "alsamixer" in a terminal.
    
    elif mic_but.is_pressed:
		time.sleep(1)
		if mic_but.is_pressed:
			os.system("screen -dmS radio")
			time.sleep(1)
			os.system("screen -S radio -X stuff 'cd /home/pi/pi-gpioradio^M'")
			time.sleep(1)
			os.system("screen -S radio -X stuff 'arecord -fS16_LE -r 22050 -Dplughw:1,0 - | sudo ./pifm - 99.8 22050^M'")
			time.sleep(5)



    ## If this button is pressed, all ongoing screen sessions and therefore transmissions will be killed/stopped.
    ## This only applies for one session named according to the definition here.
    ## If you didn't change the name of the screen session, don't worry!
    
	elif term_but.is_pressed:
		time.sleep(1)
		if term_but.is_pressed:
        
               # Sends a "kill" command to the "radio" screen session
			os.system("screen -S radio -X kill")
			time.sleep(1)

