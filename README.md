# nlp_writer_scaffold
A scaffold for deploying dockerized flask applications showing student natural language processing projects using aitextgen and pytorch.

### File Structure
The files/directories which you will need to edit are **bolded**, and the files you may need to edit are *italicized*.
DO NOT TOUCH OTHER FILES.

- .gitignore
- Dockerfile
- READMD.md
- entrypoint.sh
- nlp
- app/
     - **main.py**
     - **pytorch_model.bin** <- you will need to upload this yourself after cloning the repo when developing the site
     - *requirements.txt*
     - simple_site.py
     - st_app.py
     - utils.py
     - uwsgi.ini
     - wsgi.py
     - **weights_location**
     - static/
          - **images/**
          - *Home.css*
          - *Results.css*
          - *Write-your-story-with-AI.css*
          - jquery.js
          - nicepage.css
          - nicepage.js
          - text_gen.js
          - duck.gif
          - duck2.gif
          - loader.gif
          - puppy.jpg
     - templates/
          - **Write-your-story-with-AI.html**
          - **writer_home.html**
          - simple_index.html
### pytorch_model.bin ###
The weights file - must upload if you are running file on coding center.
### st_app.py ###
Has code for streamlit.
### main.py ###
Contains the main flask app itself.
### requirements.txt ###
Contains list of packages and modules required to run the flask app. Edit only if you are using additional packages that need to be pip installed in order to run the project.
### static/ ###
Contains the static images, CSS, & JS files used by the flask app for the webpage. Home.css is for the landing page, Results.css is for the landing page. Place all your images used for your website in static/images/.
### templates/ ###
Contains the HTML pages used for the webpage. Edit these to fit your project. writer_home.html is the landing page, Write-your-story-with-AI.html is the result page.
### Files used for deployment ###
`Dockerfile`
`uwsgi.ini`
`wsgi.py`
`nlp`
Do not touch these files.
