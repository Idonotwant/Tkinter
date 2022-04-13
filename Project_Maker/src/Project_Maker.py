'''
Author: Idonotwant
Description: A small tool to set up project
Brief_Log:
2022/04/13 start
Note:
a rough program to help me make project easier
but I beleive that there is a lot to be improved in fileIO
'''
import os
import time
import json


SETTING_FILE_NAME = f"..{os.sep}data{os.sep}setting.json"
InSTRUCTION_FILE_NAME = f"..{os.sep}data{os.sep}instruction.txt"

def timeCatcher():#return current date
    t = time.localtime()
    return time.strftime("%Y/%m/%d",t)
def settingGetter():#get setting document,return a dict
    try:
        if(os.path.isfile(SETTING_FILE_NAME)):
            with open(SETTING_FILE_NAME,"r") as f:
                data = f.read()
                js = json.loads(data)
                return js
    except:
        print("settingGetter ERROR")

def instructionPrinter():#print instruction from current file
    try:
        if(os.path.isfile(InSTRUCTION_FILE_NAME)):
            with open(InSTRUCTION_FILE_NAME,"r") as f:
                data = f.readlines()
                if(data):
                    for i in range(len(data)):
                        print(data[i],end="")
    except:
        print("instructionPrinter ERROR")

def projectMaker(setting,userinput):
    if(len(list(userinput.keys()))):
        for item in userinput.keys():
            setting[item] = userinput[item]
        if not (len(setting['Description'])):
            setting['Description'] = setting['ProjectName']
        print(setting)
        name = setting['ProjectName']
        try:
            os.mkdir(f"..{os.sep}..{os.sep}{name}")
            os.mkdir(f"..{os.sep}..{os.sep}{name}{os.sep}data")
            os.mkdir(f"..{os.sep}..{os.sep}{name}{os.sep}src")
            os.mkdir(f"..{os.sep}..{os.sep}{name}{os.sep}packages")
        except:
            print("ProjectMakerERROR")
        try:
            with open(f"..{os.sep}..{os.sep}{name}{os.sep}src{os.sep}{name}.py","w") as f:
                f.write("'''\n")
                for item in setting.keys():
                    itemV = setting[item]
                    if item=="Brief_Log_Start":
                        f.write("Brief_Log:\n")
                        time = timeCatcher()
                        f.write(f"{time} {itemV}\n")
                    else:
                        f.write(f"{item}: {itemV}\n")
                    
                f.write("'''\n")
        except:
            print("WriteFileERROR")
if __name__ == "__main__":
    instructionPrinter()
    userinput = {}
    mode = input("mode: ")
    projectName = input("Project name: ")
    userinput["ProjectName"] = projectName
    if(mode==1):#with description
        description = input("description: ")
        userinput["Description"] = description
    else:
        pass
    setting = settingGetter()
    if setting:
        projectMaker(setting,userinput)
    else:
        print("inValid Setting")
