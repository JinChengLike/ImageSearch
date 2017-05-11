# coding=utf-8
from app import app
from app import formModel
from flask import render_template, request
from werkzeug.utils import secure_filename
from app import ImageCheckModel, ImageHandleModel
import os
import time

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])


@app.route('/')
def index():
    form = formModel.NewFileForm()
    return render_template("index.html", form=form)


@app.route('/insertNewImage', methods=['GET', 'POST'])
def insertNewImage():
    form = formModel.NewFileForm()
    img = form.newfile.data
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    fname = secure_filename(img.filename)
    ext = fname.rsplit('.', 1)[1]
    unix_time = int(time.time())
    new_filename = str(unix_time) + '.' + ext
    img.save(os.path.join(file_dir, new_filename))
    # obj = ImageHandleModel.ImageHandle(img=img)
    # haming = obj.ImageWay()
    return "1"
