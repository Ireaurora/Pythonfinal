#This program allows you to
#Read a file
#Write to a file
#Append to a file
#Delete a file
#List the contents in a folder

import shutil
import os
import time
import subprocess
# the os and subprocess module deal with the operating system you are using

def Read():
    path = input("Enter the file path you want to read")
    file = open(path, "r") #the "r" indicates that the file has to be opened and read
    print(file.read())
    input("Please press enter")
    file.close()

def Write():
    path = input("Enter the file path you want to create or write")
    if os.path.isfile(path):
        print("On the way to rebuild the existing file")
    else:
        print("Creating the file")
    text = input("Enter name of file")
    file = open(path, "w")
    file.write(text)

def Add():
    path = input("Enter the file path, please")
    text = input("Enter the text to add")
    file = open(path, "a")
    file.write('\n'+ text)

def Delete():
    path = input("Enter the file path to delete")
    if os.path.exists(path):
        print("File found")
        os.remove(path)
        print("File deleted")
    else:
        print("File doesn't exist")

def Dirlist():
    path = input("Enter the directory path to display")
    sortlist = sorted(os.listdir(path))
    i=0
    while (i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+= 1

def Check():
    fp = int(input("Check existence of \n1.File \n2.Directory"))
    if fp==1:
        path = input("Enter the file path:")
        os.path.isfile(path)
        if os.path.isfile(path) == True:
            print("File found")
        else:
            print("File not found")
    if fp == 2:
        path = input("Enter the directory path:")
        os.path.isfile(path)
        if os.path.isdir(path) == False:
            print("File not found")
        else:
            print("Directory not found")

def Move():
    path1 = input("Please enter the source path of file to move")
    mr = int(input("1.Rename \n2.MOve\n"))
    if mr == 1:
        path2 = input("Enter the destination path and file name")
        shutil.move(path1, path2) #renames
        print("File renamed")
    if mr ==2:
        path2 = input("Enter the path to move")
        shutil.move(path1, path2) #moves the file from path 1 to path 2
        print("File moved")


def Copy():
    path1 = input("Please enter the path of the file to copy or rename")
    path2 = input("Enter the path to copy to")
    shutil.copy(path1, path2)
    print("File copied")

def Create_dir():
    path = input("Enter the directory name with path to make \neg. C:\\New_Folders is new directory")
    os.makedirs(path)
    print("Directory Created")

def Opening_files():
    path = input("Enter the path of the program")
    try :
        os.open(path)
    except:
        print("File not found")

run = 1
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
while (run==1):
    try:
        os.system("clear")
    except OSError:
        os.system("cls")
    print('>>>>>>>>Python 3 File Management<<<<<<<< \n')
    print("Current time and date is", time_string)
    print("Choose an option by inserting its number")
    options = int(input("\n1.Read a file,\n2.Write to a file,\n3.Append text to a file,\n4.Delete a file,\n5.List files in a directory, \n6.Check file existance,\n7.Move a file,\n8.Copy a file,\n9.Create an directory,\n10.Open a program,\n11.Exit "))
    if options ==1 :
        Read()
    if options ==2 :
        Write()
    if options ==3 :
        Add()
    if options ==4 :
        Delete()
    if options ==5 :
        Dirlist()
    if options ==6 :
        Check()
    if options ==7 :
        Move()
    if options ==8 :
        Copy()
    if options ==9 :
        Create_dir()
    if options ==10 :
        Opening_files()
    if options ==11 :
        run = int(input("1.Return to menu\n2.Exit \n"))
    if run ==2:
        exit()
