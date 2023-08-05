# all base python imports
import os, ctypes, sys, platform, subprocess

# get the uname, just for debugging.
uname = platform.uname()

banner = rf"""
a script by...
      .o.                       .                                                Meta Link White Bar Fixer
     .888.                    .o8                                                © Autumn 2023
    .8"888.     oooo  oooo  .o888oo oooo  oooo  ooo. .oo.  .oo.   ooo. .oo.      written in:     Python 3.11.3
   .8' `888.    `888  `888    888   `888  `888  `888P"Y88bP"Y88b  `888P"Y88b     running on:     {uname.machine} {uname.system} {uname.release}
  .88ooo8888.    888   888    888    888   888   888   888   888   888   888     installed at:   <** REDACTED **>
 .8'     `888.   888   888    888 .  888   888   888   888   888   888   888     documentation:  <unavailable>
o88o     o8888o  `V88V"V8P'   "888"  `V88V"V8P' o888o o888o o888o o888o o888o    supprt:         <unavailable>
"""

# print it, if you want, idk.
print(banner)

def main():
    print("This will patch the white bar on oculus link because Meta can't be bothered to fix it themselves.")
    print(r"""
          
__          __     _____  _   _ _____ _   _  _____
\ \        / /\   |  __ \| \ | |_   _| \ | |/ ____|
 \ \  /\  / /  \  | |__) |  \| | | | |  \| | |  __
  \ \/  \/ / /\ \ |  _  /| . ` | | | | . ` | | |_ |
   \  /\  / ____ \| | \ \| |\  |_| |_| |\  | |__| |
    \/  \/_/    \_\_|  \_\_| \_|_____|_| \_|\_____|
""")
    print("it is advised you make a system restore point before running!")
    input("[ Press RETURN to CONTINUE. . . ]")
    os.system('reg add "HKEY_CURRENT_USER\SOFTWARE\Oculus\RemoteHeadset" /v "numSlices" /t REG_DWORD /d "1" /f')
    print("Done.")
    print("Verifying...")
    registryResponse = os.system("reg query HKCU\SOFTWARE\Oculus\RemoteHeadset /v numSlices")
    if registryResponse == 0:
        print("Checks passed!")
    else:
        print("Error! Key writing failed!")
    input("[ Press RETURN to EXIT. . . ]")

# set the window title
os.system("title Meta Link White Bar Fixer")

# create a function for checking if the user is an admin.
def is_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        return False

# woah...
if is_admin():
    # allow the main function to be run.
    elevated = True
else:
    # prompt for admin.
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f" \"{sys.argv[0]}\"", None, 1)
    # mark this iteration for termination.
    elevated = False

if elevated:
    # run the main function if we have admin.
    main()
else:
    # the script auto reboots so quit this iteration.
    exit()
