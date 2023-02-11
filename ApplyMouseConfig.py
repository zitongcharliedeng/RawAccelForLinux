import math
import subprocess

# Config
mouseId = 9
sensitivityMultiplier = 0.1
degreesOfClockwiseSensorRotation = 11

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
	# Overall Transformation Matrix (i.e. from rotation and sens...)
subprocess.run(["xinput", "--set-prop", f"{mouseId}", "Coordinate Transformation Matrix", f"{a}",f"{b}",f"{c}",f"{d}",f"{e}",f"{f}",f"{g}",f"{h}",f"{i}"])
