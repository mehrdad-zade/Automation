'''
1. make sure you have python installed
2. save this script as "generate-iconset-from-png.py"
3. choose a png file and rename it to "applet"
4. copy below to the terminal and provide the path to applet.png and .py files
5. python /path/to/generate-iconset-from-png.py /path/to/original/icon.png
6. go to /path/to/original/ and find "applet.icnc" and copy it
7. right click on the application file you want to change the icon
8. choose "show package content" -> "content" -> "resources"
9. delete the exisiting icnc file
10. paste the new one yu had copied in step 6
'''

import os
import sys
import pathlib
import subprocess

if len(sys.argv) < 2:
    print("No path to original / hi-res icon provided")
    raise SystemExit

if len(sys.argv) > 2:
    print("Too many arguments")
    raise SystemExit

originalPicture = sys.argv[1]
if not (os.path.isfile(originalPicture)):
    print(f"There is no such file: {sys.argv[1]}")
    raise SystemExit

fname = pathlib.Path(originalPicture).stem
ext = pathlib.Path(originalPicture).suffix
destDir = pathlib.Path(originalPicture).parent

iconsetDir = os.path.join(destDir, f"{fname}.iconset")
if not (os.path.exists(iconsetDir)):
    pathlib.Path(iconsetDir).mkdir(parents=False, exist_ok=True)

class IconParameters():
    width = 0
    scale = 1
    def __init__(self,width,scale):
        self.width = width
        self.scale = scale
    def getIconName(self):
        if self.scale != 1:
            return f"icon_{self.width}x{self.width}{ext}"
        else:
            return f"icon_{self.width//2}x{self.width//2}@2x{ext}"

# https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon#app-icon-sizes
ListOfIconParameters = [
    IconParameters(16, 1),
    IconParameters(16, 2),
    IconParameters(32, 1),
    IconParameters(32, 2),
    IconParameters(64, 1),
    IconParameters(64, 2),
    IconParameters(128, 1),
    IconParameters(128, 2),
    IconParameters(256, 1),
    IconParameters(256, 2),
    IconParameters(512, 1),
    IconParameters(512, 2),
    IconParameters(1024, 1),
    IconParameters(1024, 2)
]

# generate iconset
for ip in ListOfIconParameters:
    subprocess.call(
        [
            # option 1: sips
            "sips",
            "-z",
            str(ip.width),
            str(ip.width),
            originalPicture,
            "--out",

            os.path.join(iconsetDir, ip.getIconName())
            
        ]
    )
    #print(f"Generated {ip.getIconName()}")

# convert iconset to icns file
subprocess.call(
    [
        "iconutil",
        "-c",
        "icns",
        iconsetDir,
        "-o",
        os.path.join(destDir, f"{fname}.icns")
    ]
)