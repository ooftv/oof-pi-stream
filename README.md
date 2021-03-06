# oof-pi-stream

# Getting Started:

You'll need to know your raspberry pi model. We will use OSMC as the base OS. I'm using a Raspberry Pi 3 b+ for this. Run the installer from osmc.tv. I have not always been successful with their installer, but that's outside the scope of this document. I recommend downloading the image directly from the website instead of relying on the installer to download it. The installer still failed for me, check the log which is in your user directory (~/osmc_installer_log.txt). It's probably related to new filesystem security in macOS Mojave and later.

I downloaded the image here:
https://osmc.tv/download/

I got the following command from the osmc_installer_log.txt and ran it. This will byte for byte copy the source (if) over the output source (of). So be careful with the command, and be sure to know that whatever is on the destination disk will be destroyed. This is intended to be written to a microSD card that can be totally overwritten.  

sudo dd if=/path/to/img_file of=/dev/destinationdisk bs=1m conv && sync  
ex:  
sudo dd if=/Users/myusername/Downloads/OSMC_TGT_rbp2_20201019.img of=/dev/rdisk2 bs=1m conv=sync && sync  
 
# Basic Configuration of OSMC:
You'll need a keyboard for initial setup. Make sure to enable ssh and note the IP address. Login will be osmc / osmc (now that you know the defaults, change it first thing with the passwd command). Also make sure to turn off autoupdates.  

Next install some useful command line programs:  
sudo apt install git vim rsync

Now change to the ooftv folder and sync with git.  
mkdir -p /usr/local/bin/ooftv && sudo chown -R osmc /usr/local/bin/ooftv && cd /usr/local/bin/ooftv && git init && git remote add origin https://github.com/ooftv/oof-pi-stream && git pull origin main  

# Copying video files to play
make a folder for the videos (this step will be done automatically by plmaker, but usually you'd probably copy media over before running plmaker and you'll need a place to put it). 

mkdir -p ~/ooftv/videos  

note: you need to have a video in promos for plmaker to work (script should check if folder is empty but doesn't currently)

copy videos with rsync (example:)  
rsync -av sourcefolder/ osmc@[serveraddress]:/destinationfolder/  
rsync -av videos/ osmc@[192.168.0.202]:/home/osmc/ooftv/videos/  

if everything worked, then automate. 

# Automate scripts

I used cron. I know there are preferred ways, but this is easy and it works. Make sure you have cron installed:

sudo apt install cron

Add these lines:

@reboot /usr/local/bin/ooftv/startstream # runs the stream after a reboot  
5 4 * * * /usr/local/bin/ooftv/plmaker # runs plmaker at 4:05 am, refreshes the playlist rdaily  
25 4 * * * /usr/local/bin/ooftv/startstream # restarts the stream with the new playlist  
