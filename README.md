# Google location history visualizer

Simple plotting tool written in Python 3.7 that parses your Google location history and outputs a map with visited locations.

Visit [Google Takeout](https://takeout.google.com/) to download your own data.

Find and extract the LocationHistory.json file to this folder to get started. The name of this file may vary by region. It is usually very big.

## Requirements
- Python3
- [Pillow](https://github.com/python-pillow/Pillow)

## Run
```
python3 glhv.py LocationHistory.json
```

## Output example

![output image](examples/my_map.png)