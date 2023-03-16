import subprocess
import json
import os.path
import distro
usrdir=os.path.expanduser( '~' )

def appearance():
    json_data = open(usrdir+'/.config/waybar/scripts/looks.json')
    data = json.load(json_data)
    print("--------------------------")
    print("Do you wish to change the border appearance edit icons or exit? \n==> [A]ppearance [I]cons [E]xit ")
    select=input()
    if select =="A" or select =="a":
        editAppearance()
        print("The config was saved sucesfully Here you can check if everythingis ok ")
    if select =="I" or select =="i":
        icons()
    if select =="E" or select =="e":
        exit
    else: 
        appearance()

def icons():
    with open(usrdir+'/.config/waybar/scripts/linkedIcons.json', 'r') as f:
        data = json.load(f)
    editIcons(data)

def editIcons(data):
    
    data=data
    lenght = listIcons(data)
    print("Input the number to edit the icon [E]dit [A]dd new entry [L]eave and save:")
    result=input()
    if result=="E" or result=="e":
        editingIconsAndNames(data)
    if result=="A" or result=="a":
        addIcons(data)  
    if result=="L" or result=="l":
        return
    else:
        editIcons(data)

def addIcons(data):
    data=data
    app_name = input("Enter the app name: ")
    icon = input("Enter the icon: ")

    # Add the new entry to the JSON data
    data.append({"appName": app_name, "icon": icon})

    # Write the updated JSON data to the file
    with open('file.json', 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"\nNew entry added: {app_name}: {icon}")
    print("Updated contents of file.json:\n", json.dumps(data, indent=2))


def editingIconsAndNames(data):
    data=data
    index = int(input("Enter the index of the entry you want to edit (starting from 0): "))

    if index < 0 or index >= len(data):
        print("Invalid index!")
        exit()

    app_name = input("Enter the new app name (leave blank to keep the same): ")
    icon = input("Enter the new icon (leave blank to keep the same): ")

    if app_name != "":
        data[index]["appName"] = app_name
    if icon != "":
        data[index]["icon"] = icon

    with open('file.json', 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"\nEntry {index} updated:")
    print("Updated contents of file.json:\n", json.dumps(data, indent=2))


def listIcons(data):
    data=data
    print("--------------------------")
    index=0
    for item in data:

        print(index,")\""+item['appName']+"\""+" is linked to "+"\""+ item['icon']+"\"")
        index=index+1
    return index
    

def installWaybar():
    distroname = distro.id()
    if distroname == 'arch':
        subprocess.run(["yay", "-S", "waybar-hyprland-git"])
        
    if distroname =='debian' or distroname =='ubuntu' :
        subprocess.run(["sudo", "apt-get update", "&& sudo ","apt-get","install","waybar"])
     

def copyConfig():
    print("Moving the worspace spripts to ~/.config/waybar/scripts/workspaces.py   ")
    subprocess.run(["cp ./workspaces.py ~/.config/waybar/scripts && cp ./looks.json ~/.config/waybar/scripts && ./linkedIcons.json ~/.config/waybar/scripts && cd ~/.config/waybar/"])
    print("Done")

def printAppearance():
    json_data = open(usrdir+'/.config/waybar/scripts/looks.json')
    data = json.load(json_data)
    print("-----------------------")
    print("Current border config :")
    print("1)"+data[0]["prefixStart"]+"    <the start of the bar> ")
    print("2)"+data[0]["prefixEnd"]+"     <the end of the bar not>")
    print("Example : "+ data[0]["prefixStart"] +"①"+data[0]["prefixEnd"] +data[0]["prefixStart"]+ "②"+data[0]["prefixEnd"])
    print("3)"+data[0]["prefixActiveStart"]+"    <this only effects the active window start> ")
    print("4)"+data[0]["prefixActiveEnd"]+"     <this only effects the active window end>")
    print("Example : "+ data[0]["prefixStart"] +"①"+data[0]["prefixEnd"] +data[0]["prefixStart"]+ "②"+data[0]["prefixEnd"]+data[0]["prefixActiveStart"]+"③"+data[0]["prefixActiveEnd"]+"     in this case the current workspaces is ③ ")

def editAppearance():
    json_data = open(usrdir+'/.config/waybar/scripts/looks.json')
    data = json.load(json_data)
    printAppearance()
    print("Edit the config by typing the relvant number: [1], [2], [3], [4], [e]xit and save")
    asnwer = input()
    if asnwer=="1":
        edit = input()
        data[0]['prefixStart'] = edit
        editAppearance()
    elif asnwer=="2":
        data[0]['prefixStart'] = edit
        editAppearance()
    if asnwer=="3":
        edit = input()
        data[0]['prefixStart'] = edit
        editAppearance()
    elif asnwer=="4":
        data[0]['prefixStart'] = edit
        editAppearance()
    elif asnwer=="e":
        json_object = json.dumps(data, indent=4)
        with open(usrdir+'/.config/waybar/scripts/looks.json', "w") as outfile:
            outfile.write(json_object)
        
    else:
        editAppearance()


def setUp():
    if  os.path.exists(usrdir+"/.config/waybar/")==False:
        print("Error NO waybar config folder found check if waybar is installed and the config folder is setuped")
        print("Do you want to install waybar [Y/n] ?")
        select = input()
        if select in "Y" or "y" or "":

            installWaybar()
        else:
            print("Config not foud exiting")
            exit()
    if  os.path.exists(usrdir+"/.config/waybar/scripts/")==False:
        print("Creating scripts folder in ~/.config/waybar/scripts/")
        subprocess.run(["mkdir", usrdir+"/.config/waybar/scripts/"])
        copyConfig()
    if  os.path.exists(usrdir+"/.config/waybar/scripts/workspaces.py")==False:
        copyConfig()
    else:
        print("Config found!!  \n going to config setup ")
        appearance()
        icons()

setUp()
