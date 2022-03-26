import os
def main():


    os.system('clear')
    print("tools")
    print("1. OneX (hacking tools)")
    print("2. VsCode")
    print("3. Obs")
    print("4. HTop")
    print("5. Tool-X (hacking tools)")
    print("6. Neofetch")
    print("X. Exit")


main()
inputMain = input("Choose Tool: \n")


if inputMain == "x":
    os.system('clear')
    exit()


if int(inputMain) == 1:
    #OneX Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes":
        os.system('sudo apt update && sudo apt upgrade')
    else: pass
    os.system('sudo apt install git')
    os.system('git clone https://github.com/rajkumardusad/onex.git')
    os.system('chmod +x onex/install')
    inputOpen = input ("attempt to open OneX? \n")
    if inputOpen == "yes":
        os.system('./onex/install')
    AskClose = input("close installer? \n")
    if AskClose == "yes":
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 2:
    #VsCode Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install com.visualstudio.code')
    AskClose = input("close installer? \n")
    if AskClose == "yes":
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 3:
    #Obs Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install obs-studio')
    AskClose = input("close installer? \n")
    if AskClose == "yes":
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 4:
    #Htop Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install htop')
    AskClose = input("close installer? \n")
    if AskClose == "yes":
        exit()
    else:
        os.system('python3 Installer.py')


    if int(inputMain) == 5:
        #tool-x installer
        InputUpdate = input("update system? \n")
        if InputUpdate == "yes":
            os.system('sudo apt update && sudo apt upgrade')
        else:
            pass
        os.system('sudo apt install git')
        os.system('git clone https://github.com/rajkumardusad/Tool-X.git')
        os.system('cd Tool-X')
        os.system('chmod +x install')
        askOpen = input("start Tool-X installer? \n")
        if askOpen == "yes":
            os.system('./install')
        else:
            pass
        AskClose = input("close installer? \n")
        if AskClose == "yes":
            exit()
        else:
            os.system('python3 Installer.py')

if int(inputMain) == 6:
    #neofetch Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install neofetch')
    askOpen = input("start neofetch?\n")
    if askOpen == "yes":
        os.system('neofetch')
    else:
        pass
    AskClose = input("close installer? \n")
    if AskClose == "yes":
        exit()
    else:
        os.system('python3 Installer.py')
