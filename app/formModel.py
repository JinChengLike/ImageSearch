# coding=utf-8
from flask_wtf import Form
from wtforms import FileField, SubmitField, RadioField


class NewFileForm(Form):
    newfile = FileField(u"新图片上传至图库")
    submit = SubmitField("submit")


class FileCheck(Form):
    file = FileField(u"选择检索的图片")
    type = RadioField('Choice 1:', choices=[(1, u'直方图法'), (2, u'平均哈希法'), (3, u'感知哈希法'), (4, u'转换哈希法')])
    submit = SubmitField("Search")
