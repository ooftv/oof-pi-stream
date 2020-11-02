import xbmc
import logging
import datetime

# this script can be used to autolaunch actions on boot for some versions of kodi, for example openelec and osmc.
# to use this script, make sure it's has the executable permission and place it:
# ~/.kodi/userdata
# if the script has errors, you'll see them in .kodi/temp/logs

today = datetime.date.today()
print(today)

logging.basicConfig(filename='/tmp/autoexec.log',level=logging.DEBUG)
logging.debug(today)
logging.info('So should this')
logging.warning('And this, too')

xbmc.executebuiltin("PlayerControl(RandomOn)")
xbmc.executebuiltin("XBMC.PlayMedia(/home/osmc/ooftv/playlists/today.m3u)")
xbmc.executebuiltin("XBMC.PlayerControl(RepeatAll)")

#xbmc.executebuiltin("RunScript('/home/osmc/scripts/mainplaylist.py')")
