# RawAccelForLinux

## Usage

### Finding your mouseId

- Open your terminal
- Type "Xinput list" and enter
- You will find the id number next to mouse name (e.g. Finalmouse Starlight ... id=9)

- If you don't see your mouse (i.e. wayland recievers) try booting your linux into XORG (e.g.https://itsfoss.com/switch-xorg-wayland/), this would likely also fix some mouse stutter issues too as it did for m

### Edit your config

- Edit "ApplyMouseConfig.py" config to your liking

### Apply config

- Run "ApplyMouseConfig.py" (e.g. in terminal "~/etc/RawAccelForLinux$ python3 ApplyMouseConfig.py")
- Changes should be applied immediately but restarting the OS will reset the settings
- So I recommend running "ApplyMouseConfig.py" on startup (e.g. with startup manager)

