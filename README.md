# PrettyWaybarWorkspaces
Yet another waybar script for controlling HYPRLAND work-spaces but this time nice with icons
### Looks:
(The first bar is the defual the second bar is the one you will have if you use my config)

 ![image](https://user-images.githubusercontent.com/111608778/225114272-d07d615a-3975-467b-bd80-5608889fb4c6.png)
## Setup:
```
git clone https://github.com/IHtDzenda/PrettyWaybarWorkspaces.git
cd PrettyWaybarWorkspaces
python setup.py
```
#### Installing fonts:
```
Arch:
  yay -S ttf-jetbrains-mono-git	
Other:
  https://github.com/JetBrains/JetBrainsMono
```
Add this to the waybar config file(this creates the bar object) 
```
"custom/betterbar":{
    "format": "{}",
    "interval": 1,        
    "on-scroll-up": "hyprctl dispatch workspace e+1",     
    "on-scroll-down": "hyprctl dispatch workspace e-1",
    "exec": "python3 ~/.config/waybar/scripts/workspaces.py -m HDMI-A-1", // replace the "HDMI-A-1" with your monitor get monitors by running yprctl -j monitors
},
```
Add dont forget to add it to the bar to!!!
```
"modules-left": ["custom/betterbar"],
```
### ⚠️ For multiple monitors 
I recommend making two waybar config files and adding "output": "HDMI-A-1" to each file and replacing the monitor name in the scrtipt argument 


## Features :
* ✅ Work
* ✅  Easy setup
* ✅  Support for multi monitors
* ✅ Importing config / configfile
* ✅ Adding a config script
