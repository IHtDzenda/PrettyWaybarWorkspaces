import subprocess
import json
iconsNumeral = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪ ", "⑫","⑬", "⑭","⑮ ","⑯", "⑰ ","⑱", "⑲"  ,"⑳" ]
icons=""
prefixStart="𓉘"
prefixEnd=" 𓉝"
prefixActiveStart="﹃"
prefixActiveEnd=" ﹄"

# Run hyprctl command and get output as JSON
result = subprocess.run(["hyprctl", "-j", "workspaces"], stdout=subprocess.PIPE)
monitors = subprocess.check_output(["hyprctl", "-j", "monitors"])
monitor = json.loads(monitors)
activeWorspaceID = monitor[0]["activeWorkspace"]["id"]
json_data = json.loads(result.stdout)
json_data = sorted(json_data, key=lambda x: x['id'])


for workspace in json_data:
    # Extract the id and lastwindowtitle fields from the object
    workspace_id = workspace["id"]
    title = workspace["lastwindowtitle"]
    if "Brave" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
    elif "Firefox" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
    elif "Discord" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
        
    elif "VSCodium" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
    elif "~" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
    elif "Spotify" in title:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+""+prefixEnd
        else:
            icons=icons+prefixActiveStart+""+prefixActiveEnd
    else:
        if activeWorspaceID!=workspace_id:
            icons=icons+prefixStart+iconsNumeral[workspace_id-1]+prefixEnd
        else:
            icons=icons+prefixActiveStart+iconsNumeral[workspace_id-1]+prefixActiveEnd


print(icons)