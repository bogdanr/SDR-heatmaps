SDR Heatmaps
============

This repo will host high resolution heatmaps that can be easily viewed in a browser.

The key is to use the [Deep Zoom](https://en.wikipedia.org/wiki/Deep_Zoom) technology to generate tiles which would display only the visible parts of an image. *It's similar to how Google Maps allows us to view all the world in a browser.*

### Usage:

1. Fork this repo and make a local clone
2. Copy your high resolution heatmap in the `highrez` directory
3. Run `generate.py` to generate the tiles and the .dzi images
4. Edit `index.html` to add the link of the newly generated .html file
5. Commit, push and submit pull request :) 
