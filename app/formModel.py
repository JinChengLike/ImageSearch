# coding=utf-8
from flask_wtf import Form
from wtforms import FileField,SubmitField


class NewFileForm(Form):
    newfile = FileField("select new pic")
    submit = SubmitField("submit")