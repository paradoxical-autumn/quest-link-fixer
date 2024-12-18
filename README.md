>[!NOTE]
>
>This repo has been retired in place for [Paradoxical VR Shenanigans](https://github.com/paradoxical-autumn/paradoxical-vr-shenanigans) which has the same functionality.<br>
>However, downloading the direct .REG files from [here](https://github.com/paradoxical-autumn/quest-link-fixer/releases) is still recommended if you don't want a full app to do the installation.

<h1 align="center">quest link fixer</h1>
<p align="center">An app used for fixing the white bar when using Meta Quest Link.</p>

## About
This app fixes that annoying white bar that appears when using quest link on a meta headset since meta isn't gonna fix it themselves.<br/>
Note: This app might not be required in all cases, such as when using air link, but fixes the issue when it is present.

### Raw Reg Files
I also distribute a raw .reg file for the fix, which is a a lot lighter than a full app. However, you will need either reboot OVR yourself or reboot your computer.

## Download
### GitHub (Recommended)
You can download a release from the [GitHub releases page](https://github.com/paradoxical-autumn/meta-link-fixer/releases)

### Building from source
This is a Python project so compilation *isn't required* but can be done. I use [PyInstaller](https://pypi.org/project/pyinstaller/) with the following command to build the script:
```bat
pyinstaller --clean -F fixer.py -n "Quest Link White Bar Fixer" --uac-admin -i "icon.png"
```
