import subprocess
import json
import os.path
iconsNumeral = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪ ", "⑫","⑬", "⑭","⑮ ","⑯", "⑰ ","⑱", "⑲"  ,"⑳" ]
icons=""
prefixStart="𓉘"
prefixEnd=" 𓉝"
prefixActiveStart="﹃"
prefixActiveEnd=" ﹄"
usrdir=os.path.expanduser( '~' )


# Run hyprctl command and get output as JSON
result = subprocess.run(["hyprctl", "-j", "workspaces"], stdout=subprocess.PIPE)
monitors = subprocess.check_output(["hyprctl", "-j", "monitors"])
monitor = json.loads(monitors)
activeWorspaceID = monitor[0]["activeWorkspace"]["id"]
json_data = json.loads(result.stdout)
json_data = sorted(json_data, key=lambda x: x['id'])

with open(usrdir+'/.config/waybar/scripts/linkedIcons.json', 'r') as f:
    linkedIcons = json.load(f)

for workspace in json_data:
    # Extract the id and lastwindowtitle fields from the object
    workspace_id = workspace["id"]
    title = workspace["lastwindowtitle"]
    notDone=True
    for item in linkedIcons:
        if item['appName']in title:
            if activeWorspaceID!=workspace_id:
                icons=icons+prefixStart+item['icon']+prefixEnd
                notDone =False
            else:
                icons=icons+prefixActiveStart+item['icon']+prefixActiveEnd

                notDone=False
    
    if notDone==True:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+iconsNumeral[workspace_id-1]+prefixEnd
        else:
            icons=icons+prefixActiveStart+iconsNumeral[workspace_id-1]+prefixActiveEnd
      


print(icons)