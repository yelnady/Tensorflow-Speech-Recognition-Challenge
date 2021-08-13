#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run by typing
#      python3 flask_app.py
# in a terminal (or just ./main.py).

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

port = 12345
def project_id():
    import json
    import os
    info = json.load(open(os.path.join(os.environ['HOME'], ".smc", "info.json"), 'r'))
    return info['project_id']

base_url = "/%s/port/%s/" % (project_id(), port)
static_url = "/%s/port/%s/static" % (project_id(), port)

from flask import Flask, render_template
app = Flask(__name__, static_url_path=static_url)

# notice the url here is just base and nothing else.
@app.route(base_url)
def home():
    # this is how you can render a template
    # check the template to see how to send a static file into the template.
    name = "AI Camp"
    return render_template('simple_index.html', name=name)

if __name__ == "__main__":
    # you will need to change code.ai-camp.org to other urls if you are not running on the coding center.
    print("Try to open\n\n    https://coding.ai-camp.org" + base_url + '\n\n')
    app.run(host = '0.0.0.0', port = port, debug=True)
    import sys; sys.exit(0)
