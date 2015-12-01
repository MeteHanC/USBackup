# Script Name	: USBackup_main.py
# Author		: Metehan Cetinkaya
# Created              : 25.11.2015
# Version		: 1.0
# Description	: Simple Removable Drive Backup program with python
import win32file
import os
import time
import shutil                                             
import threading
import win32com.client                                                                        
import USBackup_
files_to_be_coppied=[]
def backup_(drive_name):
          target_drive=r'C:\ '                                        
          target_drive=target_drive[0:3]                          
          target_dir="USBackup"                                    
          temporary_="USBackup"
          changeit=False
          name_number=0
          try:
           for dirs in os.listdir(target_drive): # getting directory names in target_drive. 
                  if name_number>=10: # Ord of the 10 is smaller than ord of the 1. so i had to do something other.
                       changeit=True
                  if changeit:
                       target_dir=backup_2(target_drive,temporary_)#10 and above will be named with different way
                  if dirs==target_dir: # If the directory exists it will add 1 to name_number then will convert name_number to str and add it to target_dir. So if USBackup exists it will create a new directory Usbackup-1
                      name_number=name_number+1
                      target_dir=temporary_+"-"+str(name_number)
          
                      
           target_path=target_drive+ target_dir  +"\ "
           target_path_2=target_drive+ target_dir
           for i in os.listdir(drive_name): # getting the directories in plugged drive.
                 try:
                      shutil.copytree(r'%s\%s' %(drive_name,i),  target_path+i, ignore=None) #try copying the whole directory
                 except PermissionError : 
                      print("")
                 except FileExistsError:
                      print("")
                 except NotADirectoryError: # If its not a directory there will be an error. So we will add it to files_to_be_coppied list we will copy them when backup_ function is over
                                   files_to_be_coppied.append(i)
                                   
          except:
               pass
          backup_files(drive_name,target_path_2) # start copying the files 
def backup_2(hedef_disk_sabit,gecici):
     sayma=10
     hedef_klasor_isim="USBackup"+"-"+str(sayma)
     for i_klasor in os.listdir(hedef_disk_sabit):
          if i_klasor==hedef_klasor_isim:
                      sayma+=1
                      hedef_klasor_isim=gecici+"-"+str(sayma)
     return hedef_klasor_isim
def backup_files(drive_name,target_path_2): 
      for kek in files_to_be_coppied: 
       try:
            shutil.copy(r'%s\%s'%(drive_name,kek),target_path_2) # try copying the files from files_to_be_coppied list.
       except:
             pass

          

USBackup_.USBackup_Startup()# Creating shortcut at Startup folder. So py will be executed at start.I mean there will be an import error but if you convert it to exe it will be ok.
while True:
     drive_name=USBackup_.USBackup_GetLogicalDrives() 

     if drive_name !=None:
          backup_(drive_name)
          time.sleep(1)



