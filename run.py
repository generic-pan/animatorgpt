import argparse
import math
import os
import io
from pydub import AudioSegment
import pandas as pd
import subprocess, shlex
from azure.storage.blob import BlobServiceClient
from mutagen.mp3 import MP3

parser = argparse.ArgumentParser(description='Get topic ID.')
parser.add_argument('number', type=int, help='An integer argument.')
parser.add_argument('folder', type=str, help='A string argument.')

# Parse the command-line arguments
args = parser.parse_args()

# Access the argument value
ind = args.number
folder = args.folder

# Read CSV file into a DataFrame
df = pd.read_csv('info.csv')


index = ind
row = df.iloc[ind]
svg_value = row['svg_' + str(row['chosen_svg'])]
    
slowed_svg = svg_value

with open('item.svg', 'w') as file:
    file.write(slowed_svg)


script_path = os.path.abspath(__file__)

# Print the absolute path
print(script_path)

blob_data = blob_client.download_blob().readall()

stream = io.BytesIO(blob_data)

# Load the audio from the byte stream
audio = AudioSegment.from_file(stream, format="mp3")

audio_duration = audio.duration_seconds

subprocess.run(shlex.split(f'/mnt/batch/tasks/startup/wd/node_modules/timecut/cli.js frame.html --viewport="1280,720,deviceScaleFactor=2" -R 60 -d {audio_duration}'))

subprocess.run(shlex.split(f'ffmpeg -i video.mp4 -i {index}.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 final.mp4'))

blob_client = blob_service_client.get_blob_client(container=container_name, blob="folder/" + str(ind) + ".mp4")

with open("final.mp4", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)