#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json

try:
    import deepzoom
except ImportError:
    sys.exit("""You need deepzoom!
                https://github.com/openzoom/deepzoom.py""")

try:
    import jinja2
except ImportError:
    sys.exit("""You need Jinja2!
                run pip install jinja2.""")

hirezdir="hirez/"
htmldir="tiles/"

# We prepare to load the html template from the filesystem
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
TEMPLATE_ENVIRONMENT = Environment(autoescape=False, loader=FileSystemLoader('.'), trim_blocks=False)

# Create Deep Zoom Image creator with weird parameters
creator = deepzoom.ImageCreator(tile_size=128, tile_overlap=2, tile_format="png", image_quality=0.8, resize_filter="bicubic")

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_heatmap_html():
    context = {
        'dziname': filename + ".dzi"
    }
    with open(htmldir + filename + ".html", 'w') as f:
        html = render_template('heatmap.jinja', context)
        f.write(html)

def create_index_html():
    with open('maps.json') as json_file, open('index.html', 'w') as f:
        maps = json.load(json_file)
        index_template=TEMPLATE_ENVIRONMENT.get_template('index.jinja')
        index_html=index_template.render(maps = maps).encode('utf-8')
        f.write(index_html)


for hirezname in os.listdir(hirezdir):
    if hirezname.endswith(".png") or hirezname.endswith(".jpg"): 
        filename, file_extension = os.path.splitext(hirezname)
        dziname = htmldir + filename + '.dzi'
        if os.path.isfile(dziname):
            print "skipping " + dziname
            continue
        else:
            print "generating " + dziname
            creator.create(hirezdir + hirezname, dziname)
            create_heatmap_html()
            continue
        continue
    else:
        continue


create_index_html()
