# RawAccelForLinux

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

- Edit "ApplyMouseConfig.py" config to your liking using the mouseId you just found  
  ![image](https://user-images.githubusercontent.com/108423881/218272945-7e72fa74-10cd-43bd-b0e9-e7c915cdcca0.png)  

### Apply config

- Run "ApplyMouseConfig.py" (e.g. ```~/etc/RawAccelForLinux$ python3 ApplyMouseConfig.py```)  
- Changes should be applied immediately but restarting the OS will reset the settings  
- So I recommend running "ApplyMouseConfig.py" on startup  
  - e.g. with the startup manager:  
  ![image](https://user-images.githubusercontent.com/108423881/218272855-b5bc1704-94ad-447c-9847-4b27b3af7818.png)  



