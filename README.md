# AnimatorGPT
A project that uses LLMs to create SVG-based sprite animations

# Process
1. Given a story idea, such as "boy on a desert planet discovers two droids and finds his father's old lightsaber," the program prompts an LLM for a "storyboard" - a sequence of visual scenes that treats sprites as puppets
2. For each scene in the storyboard, the program extracts all necessary sprites and generates visuals for them, either with the Bing API or stable diffusion
3. For each scene, the program prompts an LLM for a .svg animation that demonstrates the desired interaction, which usually consists of basic descriptions of transformations in position or size
4. Using ffmpeg, the program stitches the .svg animations together into an .mp4 file
5. With an LLM and the Freesound API, the program inserts appropriate sound effects into each scene
