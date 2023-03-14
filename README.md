# PrettyWaybarWorkspaces
Yet another waybar script for controlling HYPRLAND work-spaces but this time nice with icons
### Looks:
(The first bar is the defual the second bar is the one you will have if you use my config)

 ![image](https://user-images.githubusercontent.com/111608778/225114272-d07d615a-3975-467b-bd80-5608889fb4c6.png)
## Setup:
```
git clone https://github.com/IHtDzenda/PrettyWaybarWorkspaces.git
mkdir ~/.config/waybar/scripts 
cp ./PrettyWaybarWorkspaces/workspaces.py ~/.config/waybar/scripts && cp ./PrettyWaybarWorkspaces/looks.json ~/.config/waybar/scripts && ./PrettyWaybarWorkspaces/linkedIcons.json
~/.config/waybar/scripts && cd ~/.config/waybar/
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
    "exec": "python3 ~/.config/waybar/scripts/workspaces.py",

},
```
Add dont forget to add it to the bar to!!!
```
"modules-left": ["custom/betterbar"],
```

## Features :
* ✅ Work
* ❌ Easy setup
* ❌ Importing config / configfile
* ❌ Adding a config script
