# Script tested with Pop_OS 19.04 + Nvidia driver
# Xeon E3 1230, GTX 670 2GB, 8GB DDR3

import subprocess, os

# Change this according to your preferred path for things to install to
APPS_PATH = "/home/meow/Apps"
os.chdir(APPS_PATH)

def run(cmd):
    # hacky translation of cd
    if cmd.startswith('cd '):
        os.chdir(cmd[3:])
        return
    try:
        subprocess.call(cmd, shell=True)
    except:
        print (cmd, "failed to run.")

def run_many(cmds):
    os.chdir(APPS_PATH)
    cmds = cmds.split('\n')
    for cmd in cmds:
        run(cmd)

apps = {}

# Install snap
# A package manager for linux
apps['snap'] = 'sudo apt install snapd'

# Install Lutris
# A games manager for linux
apps['lutris'] = '''sudo add-apt-repository ppa:lutris-team/lutris
sudo apt-get update
sudo apt-get install lutris'''

# Install Discord
# A communication app for games and work, similar to slack
apps['discord'] = 'sudo snap install discord'

# Install VS Code
# A code editor
apps['vs-code'] = 'sudo snap install --classic code'

# Install flameshot
# A screenshot utility similar to lightshot
# Configure hotkey manually in settings > devices > keyboard 
apps['flameshot'] = '''sudo apt install libqt5dbus5 libqt5network5 libqt5core5a libqt5widgets5 libqt5gui5 libqt5svg5-dev
sudo apt-get install libqt5svg5*
sudo apt install flameshot'''

# Install ffnvcodec
# Dependency of ffmpeg-nvenc
apps['ffnvcodec'] = '''git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
cd nv-codec-headers
make
sudo make install'''

# Install Nvidia Video SDK
# Dependency of ffmpeg-nvenc
apps['nvidia-video-sdk'] = '''wget https://developer.nvidia.com/video-sdk-601
sudo apt install unzip
unzip video-sdk-601
sudo cp nvidia_video_sdk_6.0.1/Samples/common/inc/*.h /usr/local/include/'''

# Install ffmpeg and additional deps
# Build of ffmpeg with nvenc for harware acceleration in OBS
ffmpeg_dir = [d for d in os.listdir() if os.path.isdir(d) and d.startswith("ffmpeg")][0]
apps['ffmpeg'] = '''sudo apt update
sudo apt build-dep ffmpeg
sudo apt install libfdk-aac-dev
apt-get source ffmpeg
cd {}
./configure --prefix=/usr --extra-version=0ubuntu1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-avresample --disable-filter=resample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared --enable-nonfree --enable-nvenc --enable-libfdk-aac
make
sudo make install'''.format(ffmpeg_dir)

# Install OBS
# A screen recording and streaming utility 
apps['obs'] = '''git clone --recursive https://github.com/lutris/ffmpeg-nvenc.git
cd ffmpeg-nvenc
sudo ./build.sh --dest {}
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt-get update
sudo apt-get install obs-studio'''.format(APPS_PATH)

# Install htop
# A better version of top
apps['htop'] = "sudo apt install htop"

# Install Psensor and deps
# Allow monitoring of system temp sensors
apps['psensor'] = "sudo apt install lm-sensors hddtemp psensor"

# Install Chrome
# A web browser based on Chromium
apps['chrome'] = '''wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb'''

# Install Gnome tweak tool
# Allow greater customization of Gnome
apps['gnome_tweak'] = '''sudo add-apt-repository universe
sudo apt install gnome-tweak-tool'''

# Install Dash to Dock
# Allow Dock to be permenantly visible and placed on any side of the screen
# Must reload shell: Alt + F2, then type 'r' 
# Then go to gnome tweak tool and enable the extension
apps['dash-to-dock'] = '''git clone https://github.com/micheleg/dash-to-dock.git
cd dash-to-dock
make
sudo make install'''

# Install Steam
# A games marketplace
apps['steam'] = 'sudo apt install steam-installer'

# Run installation scripts for all apps
# for app in apps.keys():
#    run_many(apps[app])

# Run installation script for one app
run_many(apps['steam'])

print ("All done.")
