import os
import subprocess
import urllib.parse

vlc_config_path = os.path.join(os.getenv('APPDATA'), 'vlc', 'vlc-qt-interface.ini')

# Path to the VLC
vlc_executable_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'

with open(vlc_config_path, 'r') as file:
    lines = file.readlines()

# Find the line that contains the recent list
recent_list_line = [line for line in lines if line.startswith('list=')][0]

# Extract the most recent file from the list
most_recent_file = recent_list_line.split('=')[1].split(',')[0]

# Remove the 'file:///' prefix and unquote the file path
most_recent_file = urllib.parse.unquote(most_recent_file[8:])

# Replace forward slashes with backslashes (Windows file paths use backslashes)
most_recent_file = most_recent_file.replace('/', '\\')

# Open the most recent file with VLC without showing the command prompt window
subprocess.Popen([vlc_executable_path, most_recent_file], creationflags=subprocess.CREATE_NO_WINDOW)
