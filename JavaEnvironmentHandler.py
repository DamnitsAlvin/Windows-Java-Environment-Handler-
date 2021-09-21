import winreg 
import ctypes 
import os, sys


def setValues(subkey, new_local, new_java, control_path):
    try:
        winreg.SetValueEx(subkey, "JAVA_HOME", 0, winreg.REG_SZ, new_java)
        print("OK!")
    except:
        print("Error updating JAVA HOME")
        print(new_java)

    try:
        winreg.SetValueEx(subkey, "PATH", 0, winreg.REG_EXPAND_SZ, new_local)
        print("OK!")
    except: 
        print("error updating path value!")
        print(new_local)
        
    HWND_BROADCAST = 0xFFFF         #tochange 
    WM_SETTINGCHANGE = 0x1A 
    SMTO_ABORTIFHUNG = 0x0002       
    result = ctypes.c_long()
    SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
    SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u'%s'%control_path, SMTO_ABORTIFHUNG, 5000, ctypes.byref(result))


def getValues(hkey, subkey, control_path):
    JAVA_VERSIONS = list()
    found_index = list()
    entityNumber = winreg.QueryInfoKey(subkey)[1]
    for i in range(0, entityNumber):
        if winreg.EnumValue(subkey, i)[0] == "JAVA_HOME":
            JAVA_HOME_VALUE = winreg.EnumValue(subkey, i)[1]
        if winreg.EnumValue(subkey, i)[0] == "Path":
            LOCAL_MACHINE_PATH_VALUE = winreg.EnumValue(subkey, i)[1]
    
    Path_value = LOCAL_MACHINE_PATH_VALUE.split(";")
    with open("javaVersions.txt", "r") as f:
        JAVA_VERSIONS = f.readlines()
    if int(sys.argv[2]) > len(JAVA_VERSIONS):
        print("Versions out of bounds ")
        return False 

    for versions in JAVA_VERSIONS:
        for i in range(0, len(Path_value)):
            if Path_value[i].replace("\n", "") == versions.replace("\n", ""):
                found_index.append(i)
    for found in found_index:
        Path_value.pop(found)
                
    new_local_machine_path = "".join([str(path)+";" for path in Path_value[:len(Path_value)-1]])
    new_local_machine_path += JAVA_VERSIONS[int(sys.argv[2])].replace("\n", "") + ";"
    setValues(subkey, new_local_machine_path, JAVA_VERSIONS[int(sys.argv[2])].replace("\\bin", ""), control_path)
    return new_local_machine_path, JAVA_VERSIONS[int(sys.argv[2])].replace("\n", "").replace("\\bin", "")

def ChangeUserJavaPathAndVersion():
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key:
            getValues(hkey, sub_key, "Environment")

def ChangeSystemJavaPathAndVersion():
    with winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE) as hkey:
        with winreg.OpenKey(hkey, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", 0, winreg.KEY_ALL_ACCESS) as subkey:
            getValues(hkey, subkey, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" )

            
def AddJavaVersion(path):
    with open("javaVersions.txt", "+a") as f: 
        f.seek(0)
        for lines in f.readlines():
            if lines.replace("\n", "") == path:
                print("Version was already saved!")
                return False 
        f.writelines(path)
        f.write("\n")
        print("OK! Saved!")
        f.close()       

def readJavaVersions():
    with open("javaVersions.txt", "r") as f:
        for lines in f.readlines(): 
           print(lines)

def main():
    if sys.argv[1] == "-s":
        ChangeSystemJavaPathAndVersion()
    elif sys.argv[1] == "-u":
        ChangeUserJavaPathAndVersion()
    elif sys.argv[1] == "-r":
        readJavaVersions()
    elif sys.argv[1] == "-a":
        AddJavaVersion(sys.argv[2])


if __name__ == "__main__":
    main()