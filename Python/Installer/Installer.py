import os
def main():
    tools = ['OneX', 'VsCode', 'Obs', 'HTop', 'Tool-X', 'Neofetch', 'Minecraft']

    os.system('clear')
    print("tools")
    for index, tool in enumerate(tools, start=1):
        print (index, tool)
    print ('x Exit')

main()
inputMain = input("Choose Tool: \n")


if inputMain == "x" or inputMain == "X":
    os.system('clear')
    exit()


if int(inputMain) == 1:
    #OneX Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else: pass
    os.system('sudo apt install git')
    os.system('git clone https://github.com/rajkumardusad/onex.git')
    os.system('chmod +x onex/install')
    inputOpen = input ("attempt to open OneX? \n")
    if inputOpen == "yes" or inputOpen == "Yes":
        os.system('./onex/install')
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 2:
    #VsCode Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install snapd')
    os.system('sudo snap install code --classic')
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 3:
    #Obs Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install obs-studio')
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else: os.system('python3 Installer.py')


if int(inputMain) == 4:
    #Htop Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install htop')
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else:
        os.system('python3 Installer.py')


if int(inputMain) == 5:
    #tool-x installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install git')
    os.system('git clone https://github.com/rajkumardusad/Tool-X.git')
    os.system('cd Tool-X')
    os.system('chmod +x install')
    askOpen = input("start Tool-X installer? \n")
    if askOpen == "yes" or askOpen == "Yes":
        os.system('./install')
    else:
        pass
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else:
        os.system('python3 Installer.py')

if int(inputMain) == 6:
    #neofetch Installer
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install neofetch')
    askOpen = input("start neofetch?\n")
    if askOpen == "yes" or askOpen == "Yes":
        os.system('neofetch')
    else:
        pass
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else:
        os.system('python3 Installer.py')


if int(inputMain) == 7:
    InputUpdate = input("update system? \n")
    if InputUpdate == "yes" or InputUpdate == "Yes":
        os.system('sudo apt update && sudo apt upgrade')
    else:
        pass
    os.system('sudo apt install wget')
    os.system('wget  ~/Minecraft.deb https://launcher.mojang.com/download/Minecraft.deb')
    os.system('sudo apt install gdebi-core')
    os.system('sudo gdebi Minecraft.deb')
    AskClose = input("close installer? \n")
    if AskClose == "yes" or AskClose == "Yes":
        os.system('clear')
        exit()
    else:
        os.system('python3 Installer.py')
