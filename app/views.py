# coding=utf-8
from app import app
from app import formModel
from flask import render_template, request
from werkzeug.utils import secure_filename
from app import ImageCheckModel, ImageHandleModel, db, Check
import os
import time

UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])


@app.route('/')
def index():
    checkform = formModel.FileCheck()
    form = formModel.NewFileForm()
    return render_template("index.html", form=form, checkform=checkform)


@app.route('/insertNewImage', methods=['GET', 'POST'])
def insertNewImage():
    checkform = formModel.FileCheck()
    form = formModel.NewFileForm()
    img = form.newfile.data
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    fname = secure_filename(img.filename)
    ext = fname.rsplit('.', 1)[1]
    unix_time = int(time.time())
    new_filename = str(unix_time) + '.' + ext
    img.save(os.path.join(file_dir, new_filename))
    path = "static/upload/" + new_filename
    hamingWay = ImageHandleModel.ImageHandle(new_filename).ImageWay()
    hamingAverage = ImageHandleModel.ImageHandle(new_filename).AverageHash()
    hamingChange = ImageHandleModel.ImageHandle(new_filename).changeHash()
    hamingFeel = ImageHandleModel.ImageHandle(new_filename).feelHash()
    db.db().insertNew(path, hamingWay, hamingAverage, hamingChange, hamingFeel)
    return render_template("index.html", form=form, checkform=checkform)


@app.route('/search', methods=['GET', 'POST'])
def search():
    checkform = formModel.FileCheck()
    form = formModel.NewFileForm()
    file = checkform.file.data
    type = checkform.type.data
    ch = Check.Check(file, type)
    path = ch.doCheck()
    return render_template("index.html", form=form, checkform=checkform,path=path)
