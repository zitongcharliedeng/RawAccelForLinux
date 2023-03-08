# RawAccelForLinux

## Problems

- Only tested in Linux Minecraft so far...
  - Getting problems like this https://www.reddit.com/r/linux_gaming/comments/3nxnzg/mouse_stuck_in_topleft_corner_please_help/  
- At least I can browse linux with a cursor motion I like... which is what I wanted mainly (I game on windows)... Getting games to take this new modified input properly is gonna be hard...  
- Unplugging and replugging in mouse resets the settings
- Accel speed also resets to the option used in linux settings
  ![Screenshot from 2023-02-11 19-52-53](https://user-images.githubusercontent.com/108423881/218279032-43443366-ae0e-43dd-babc-c92ca9633c32.png)


## Features

- Works fine in cursor mode (in games are another story)
- Mouse sensor rotation (decimal in degrees)  
- Mouse sensitivity multiplier (decimal)  

### TODO SOON

- Custom function accel curves  
- GUI with speed graph thing, profiles, etc

## Prequisites

- python3
  - e.g. ```sudo apt-get install python3```
## Usage

### Finding your mouseId

- Open your terminal  
- Type ```xinput list``` and enter  
- You will find the id number next to mouse name (e.g. Finalmouse Starlight ... id=9)  
![image](https://user-images.githubusercontent.com/108423881/218272916-08bff256-bafb-4b68-aac0-b90dbe394bc9.png)  

- If you don't see your mouse (i.e. wayland recievers) try booting your linux into XORG (e.g. https://itsfoss.com/switch-xorg-wayland/), this would likely also fix some mouse stutter issues as it did for me  

### Edit your config

- Edit "ApplyMouseConfig.py" config to your liking
- For mouseId I recommend using your xinput mouse name (in quotations "") rather than integer id number since the id can change after replugging the mouse
  ![image](https://user-images.githubusercontent.com/108423881/218272945-7e72fa74-10cd-43bd-b0e9-e7c915cdcca0.png)  

### Apply config

- Run "ApplyMouseConfig.py" (e.g. ```~/etc/RawAccelForLinux$ python3 ApplyMouseConfig.py```)  
- Changes should be applied immediately but restarting the OS will reset the settings  
- So I recommend running "ApplyOnStartup.sh" on startup  
  - e.g. with the startup manager:  
 ![image](https://user-images.githubusercontent.com/108423881/218856959-abb16a1f-ff45-4c49-b2a4-7397b0bc903d.png)



