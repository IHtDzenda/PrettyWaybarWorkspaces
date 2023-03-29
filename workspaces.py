import subprocess
import json
import os.path
import argparse
iconsNumeral = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪ ", "⑫","⑬", "⑭","⑮ ","⑯", "⑰ ","⑱", "⑲"  ,"⑳" ]
icons=""
usrdir=os.path.expanduser( '~' )

#Monitors and script arguments
parser = argparse.ArgumentParser()
parser.add_argument('--m', type=str, default='0', help="monitors are numbers try running the script with 0 to get monitors u ")
args = parser.parse_args()
display=args.m

# Hyprctl
hyprctldata = subprocess.check_output(["hyprctl", "-j", "clients"])
clients= json.loads(hyprctldata)
clients = [item for item in clients if item["monitor"] >= 0]
clients.sort(key=lambda x: x["workspace"]["id"])
monitors = subprocess.check_output(["hyprctl", "-j", "monitors"])
monitor = json.loads(monitors)
activeWorspaceID = monitor[int(display)]["activeWorkspace"]["id"]

#loading config files
with open(usrdir + '/.config/waybar/scripts/looks.json', 'r') as f:
    looksconfig = json.load(f)[0]  
prefixStart = looksconfig["prefixStart"]
prefixEnd = looksconfig["prefixEnd"]
prefixActiveStart = looksconfig["prefixActiveStart"]
prefixActiveEnd = looksconfig["prefixActiveEnd"]
number_workspaces = looksconfig["number_workspaces"]
icon_numerals= looksconfig["icon_numerals"]
empty_icon=looksconfig["emptyicon"]
with open(usrdir+'/.config/waybar/scripts/linkedIcons.json', 'r') as f:
    linkedIcons = json.load(f)
lastid=0
once =True

for item in clients:
    name = item["class"]
    if name=="":
        continue
    id = item["workspace"].get("id")
    currentmonitor = item["monitor"]

    if currentmonitor == int(display):
        notDone = True
        for icon in linkedIcons:
            if icon['appName'] in name:
                if activeWorspaceID != id:
                    if number_workspaces:
                        icon_str = icon['icon']
                        if looksconfig:
                            icon_str = f"{id}{prefixStart}{icon_str}{prefixEnd}"
                        else:
                            icon_str = f"{prefixStart}{icon_str}{prefixEnd}"
                        icons += icon_str
                        notDone = False
                    else:
                        icons += icon['icon']
                        notDone = False                        
                else:
                    if number_workspaces:
                        icon_str = icon['icon']
                        if looksconfig:
                            icon_str = f"{id}{prefixActiveStart}{icon_str}{prefixActiveEnd}"
                        else:
                            icon_str = f"{prefixActiveStart}{icon_str}{prefixActiveEnd}"
                        icons += icon_str
                        notDone = False
                    else:
                        icons += icon['icon']
                        notDone = False        

        if notDone and icon_numerals:
            icon_str = iconsNumeral[id - 1]
            if activeWorspaceID != id:
                if looksconfig:
                    icon_str = f"{id}{prefixStart}{icon_str}{prefixEnd}"
                else:
                    icon_str = f"{prefixStart}{icon_str}{prefixEnd}"
            else:
                if looksconfig:
                    icon_str = f"{id}{prefixActiveStart}{icon_str}{prefixActiveEnd}"
                else:
                    icon_str = f"{prefixActiveStart}{icon_str}{prefixActiveEnd}"
            icons += icon_str
        elif notDone and not icon_numerals:
            icon_str = empty_icon
            if activeWorspaceID != id:
                if looksconfig:
                    icon_str = f"{id}{prefixStart}{icon_str}{prefixEnd}"
                else:
                    icon_str = f"{prefixStart}{icon_str}{prefixEnd}"
            else:
                if looksconfig:
                    icon_str = f"{id}{prefixActiveStart}{icon_str}{prefixActiveEnd}"
                else:
                    icon_str = f"{prefixActiveStart}{icon_str}{prefixActiveEnd}"
            icons += icon_str

print(icons)