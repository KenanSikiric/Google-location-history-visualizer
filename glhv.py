import sys
import json
from PIL import Image, ImageDraw

MAP_WIDTH, MAP_HEIGHT = 4096, 2048 # Resolution of template map image

with open(sys.argv[1]) as f: 
    print("\nOpening location history file...")
    data = json.load(f)
    print("Parsing coordinates...")
    ll = [[],[]] # Coordinates array, idx 0 is latitudes, idx 1 is longitudes
    for loc in data['locations']: # Extract latitudes and longitudes
        ll[0].append(loc['latitudeE7'])
        ll[1].append(loc['longitudeE7'])
    data = None # Remove loaded json from memory to save RAM (python will handle file unloading)

'''
Google provides the coordinates in E7 format. The following
two lines convert latitudes and longitudes into a decimal 
format and adjusts them according to the map template.

NOTE: I am unsure whether coordinates in the southern 
hemisphere work correctly as I am unable to test them,
but i doubt they do :d
'''
ll[0] = [-((lat/1e7)/180)*MAP_HEIGHT + (MAP_HEIGHT/2) for lat in ll[0]] # Latitude or Y value
ll[1] = [((lon/1e7)/360)*MAP_WIDTH + (MAP_WIDTH/2) for lon in ll[1]] # Longitude or X value

print("Successfully loaded coordinates!\nOpening image...")

earth_template = Image.open('earth.jpg') # Loads template map image. Must be a full, cylindrical (plate carrée) projection
draw = ImageDraw.Draw(earth_template)

print("Drawing locations:")
for i in range(len(ll[0])):
    print(i, "/", len(ll[0]), "\r", end="") if i%100 == 0 else None # \r = carriage return, neat very old character. Comment this line to save a couple of milliseconds
    draw.point((ll[1][i], ll[0][i]), fill=255) # Places red one-pixel-sized points on image

print("Saving image to disk...")
earth_template.save("my_map.png", "PNG")
print("Finished! Open 'my_map.png' to see the results!")