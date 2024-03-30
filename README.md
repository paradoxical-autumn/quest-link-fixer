<h1 align="center">meta-link-fixer</h1>
<p align="center">An app used for fixing the white bar when using Meta Quest Link.</p>

## About
This app fixes that annoying white bar that appears when using quest link on a meta headset since meta isn't gonna fix it themselves.<br/>
Note: This app might not be required in all cases, such as when using air link, but fixes the issue when it is present.

## Download
### GitHub (Recommended)
You can download a release from the [GitHub releases page](https://github.com/paradoxical-autumn/meta-link-fixer/releases)

### Building from source
This is a Python project so compilation *isn't required* but can be done. I use [PyInstaller](https://pypi.org/project/pyinstaller/) with the following command to build the script:
```bat
pyinstaller --clean -F fixer.py -n "Meta Link White Bar Fixer" --uac-admin -i "icon.png"
```