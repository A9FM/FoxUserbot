import os
import colorama
from plugins.settings.main_settings import version

from prefix import my_prefix
prefix = my_prefix()

yellow = "\033[1;33m"
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\33[1;36m"
purple = "\33[1;35m"

os.system("cls" if os.name == "nt" else "clear")
print(f"""{red}
    dMMMMMP .aMMMb  dMP dMP dMP dMP .dMMMb  dMMMMMP dMMMMb  dMMMMb  .aMMMb dMMMMMMP 
   dMP     dMP"dMP dMK.dMP dMP dMP dMP" VP dMP     dMP.dMP dMP"dMP dMP"dMP   dMP    
  dMMMP   dMP dMP .dMMMK" dMP dMP  VMMMb  dMMMP   dMMMMK" dMMMMK" dMP dMP   dMP     
 dMP     dMP.aMP dMP"AMF dMP.aMP dP .dMP dMP     dMP"AMF dMP.aMF dMP.aMP   dMP      
dMP      VMMMP" dMP dMP  VMMMP"  VMMMP" dMMMMMP dMP dMP dMMMMP"  VMMMP"   dMP       
{green}
Channel - @foxteam0
Help - @foxteamchat
Version: {version}

Client Started! Type {prefix}ping to check Userbot works
""")