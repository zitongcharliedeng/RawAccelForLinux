import math
import subprocess

# Config

mouseId = 9

sensitivityMultiplier = 1

degreesOfClockwiseSensorRotation = 0

accelSpeed = 0 # no idea how this works // default = 0 // after testing i think this is the mouse sensitivity in default linux options (the slider) it is nonlinear, and ranges -1 to 1

accelSpeedDefault = 0 # no idea how this works // default = 0

accelProfilesAvailable1 = 1 # no idea how this works // default = 1
accelProfilesAvailable2 = 1 # no idea how this works // default = 1

accelProfileEnabled1 = 0 # no idea how this works // default = 0
accelProfileEnabled2 = 1 # no idea how this works // default = 1

accelProfileEnabledDefault1 = 1 # no idea how this works // default = 1
accelProfileEnabledDefault2 = 0 # no idea how this works // default = 0


# Logic

r = math.radians(degreesOfClockwiseSensorRotation)

    # Rotation Matrix Elements (top-down => left-right) * by scalar sensitivityMultiplier:
        # Row 1
a = math.cos(r)*sensitivityMultiplier
b = -math.sin(r)*sensitivityMultiplier
c = 0
        # Row 2
d = math.sin(r)*sensitivityMultiplier
e = math.cos(r)*sensitivityMultiplier
f = 0
        # Row 3
g = 0
h = 0
i = 1           


# Shell Commands (buncha xinput set-proppings)

        # Apply custom accels (don't know what values mean rn) (but default values I put here seem to leave a static "raw" sens with my tests...)
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "libinput Accel Speed", f"{accelSpeed}"])
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "libinput Accel Speed Default", f"{accelSpeedDefault}"]) # => BadAccess (attempt to access private resource denied)
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "libinput Accel Profiles Available", f"{accelProfilesAvailable1}", f"{accelProfilesAvailable2}"])
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "libinput Accel Profile Enabled", f"{accelProfileEnabled1}", f"{accelProfileEnabled2}"])
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "libinput Accel Profile Enabled Default", f"{accelProfileEnabledDefault1}", f"{accelProfileEnabledDefault2}"]) # => BadAccess (attempt to access private resource denied)

	# Apply overall Transformation Matrix (i.e. from rotation and sens...)
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "Coordinate Transformation Matrix", f"{a}",f"{b}",f"{c}",f"{d}",f"{e}",f"{f}",f"{g}",f"{h}",f"{i}"])
