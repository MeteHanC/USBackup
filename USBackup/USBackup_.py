# Script Name	: USBackup_.py
# Author		: Metehan Cetinkaya
# Created              : 25.11.2015
# Version		: 1.0
# Description	: Simple Removable Drive Backup program with python


import os
import platform
import win32com.client
import getpass
import threading
import time
import win32file
allready_plugged=[]
def USBackup_Startup(): # This will be  useful when we convert our program to exe.
     win_version=platform.win32_ver() #Getting windows info.(7,sp1,6.1.7601 build etc)
     win_version=win_version[0] # Getting the version
     a=os.getcwd() #getting the path  our program is currently running
     slash=r'\ ' 
     slash=slash[0]#raw string slash
     script_name="USBackup_main.py" 
     a=a+slash+script_name #with os.getcwd() u are only getting the folder not the script  so with this way we are getting the exact path. 
     shortcut_=getpass.getuser()+slash # Getting the current user's name 
     if win_version=="7" or win_version=="10" or  win_version=="8" or win_version=="8.1":  #if its 7,8,8.1 or 10 create the shorcut to this path. If its xp or vista create the shorcut to below path.
      try:
          path_1=r'C:\Users'+slash
          path_2=r'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
          path=path_1+shortcut_+path_2+slash+"USBackup_main.lnk"
          if "USBackup_main.lnk" not in os.walk(path_1+path_2):
               shell = win32com.client.Dispatch("wscript.shell")
               s_cut= shell.CreateShortcut(path)
               s_cut.TargetPath = a
               s_cut.Save()
      except:
           pass
     else:
          path_1=r'C:\Documents and Settings'+bol
          path_2=r'Start Menu\Programs\Startup\USBackup_main.lnk'
          path=path_1+shortcut_+path_2
          shell = win32com.client.Dispatch("wscript.shell")
          s_cut= shell.CreateShortcut(path)
          s_cut.TargetPath = a
          s_cut.Save()



def USBackup_GetLogicalDrives():
            drv_bits=win32file.GetLogicalDrives() #Getting available logical drives
            for d in range(0,26): #There will be maximum 26 logical drives (A-Z). 
                  control=1 << d #    1*2^d 
                  drive_name='%s:\\' % chr(ord('A')+d) # Getting the drive's name 
                  try:
                       if drv_bits & control==False : #  BitWISE AND. if the drive isnt available try to delete it from the allready_plugged list. So with this way we will be blocking unlimited copying.
                            allready_plugged.remove(drive_name)
                            
                  except:
                       pass
                  if drv_bits & control: #Again bitwise and. if the drive is available 
                      drive_name='%s:\\' % chr(ord('A')+d)#get the drive's name
                      if drive_name not in allready_plugged: #  if the drive's name isnt in the allready_plugged list it will start copying. 
                          allready_plugged.append(drive_name) #We are adding the drive's name to allready_plugged list so if we dont it unplug and replug it it wont copy it again. 
                          t=win32file.GetDriveType(drive_name) # Getting the drive type for example if the drive type is removable drive it will return "2" 
                          if t == win32file.DRIVE_REMOVABLE: #Basically if its "2"
                              return drive_name #Start Backup progress.
     



     
