import math
import subprocess

degreesOfClockwiseSensorRotation = 12
r = math.radians(degreesOfClockwiseSensorRotation)

# Rotation Matrix Elements (top-down => left-right):
    # Row 1
a = math.cos(r)
b = -math.sin(r)
c = 0
    # Row 2
d = math.sin(r)
e = math.cos(r)
f = 0
    # Row 3
g = 0
h = 0
i = 1           

subprocess.run(["xinput", "--set-prop", "9", "Coordinate Transformation Matrix", f"{a}",f"{b}",f"{c}",f"{d}",f"{e}",f"{f}",f"{g}",f"{h}",f"{i}"])