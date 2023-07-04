import openai
import requests
openai.api_key = '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'

import subprocess
import shlex

def call_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0]['message']['content']
    return message




import pandas as pd

# Function to call Chatgpt
def call_Chatgpt(value):
    # Replace this function with your own logic
    # Example implementation: printing the value
    print(value)

# Read CSV file into a DataFrame
df = pd.read_csv('info.csv')

# Iterate over each row
for index, row in df.iterrows():
    # Get the value in 'column_5' for the current row
    svg_value = row['svg_' + str(row['chosen_svg'])]
    
    # Call the function with the column value
    #slowed_svg = call_chatgpt("Hi")
    slowed_svg = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 800 600">
  <style>
    .viking {
      animation: moveVikings 80s linear infinite;
    }
    
    @keyframes moveVikings {
      0% { transform: translate(0, 0); }
      100% { transform: translate(400px, 300px); }
    }
  </style>

  <image xlink:href="vikings.png" x="0" y="0" width="100" height="100" class="viking" />
  <image xlink:href="vikings.png" x="200" y="100" width="100" height="100" class="viking" />
  <image xlink:href="vikings.png" x="400" y="200" width="100" height="100" class="viking" />

  <image xlink:href="chests.png" x="50" y="50" width="100" height="100" />
  <image xlink:href="chests.png" x="250" y="150" width="100" height="100" />
  <image xlink:href="chests.png" x="450" y="250" width="100" height="100" />

  <image xlink:href="gold.png" x="70" y="70" width="60" height="60" />
  <image xlink:href="gold.png" x="270" y="170" width="60" height="60" />
  <image xlink:href="gold.png" x="470" y="270" width="60" height="60" />
</svg>
'''
    with open('item.svg', 'w') as file:
        file.write(slowed_svg)
    
    subprocess.run(shlex.split(f'./node_modules/timecut/cli.js frame.html -O segments/{index}.mp4 --viewport="1280,720,deviceScaleFactor=2" -R 120 -d 4'), shell=True, check=True)
    
