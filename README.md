# meta-link-fixer
An app used for fixing the white bar on Meta Quest Link.

## About
This app fixes that annoying white bar that appears when using quest link on a meta headset since meta isn't gonna fix it themselves.

## Download
### GitHub (Recommended)
You can download a release from the [GitHub releases page](https://github.com/Pixel-Tgc2019/meta-link-fixer/releases)

### Building from source
This is a Python project so compilation *isn't required* but can be done. The tool I use it [PyInstaller](https://pypi.org/project/pyinstaller/) with the following command:
```bat
pyinstaller --clean -F fixer.py -n "Meta Link White Bar Fixer" --uac-admin -i "icon.png"
```