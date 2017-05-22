from app import ImageCheckModel, ImageHandleModel, db, ImageSearchHandle


class Check:
    def __init__(self, img, type):
        self.img = img
        self.type = type

    def doCheck(self):
        if self.type == '1':
            img = ImageSearchHandle.SearchHandle(self.img).ImageWay()
            path = Check.compWay(self, img)
            return path
        elif self.type == '2':
            img = ImageSearchHandle.SearchHandle(self.img).AverageHash()
            type = "hamingAverage"
            path = Check.compOther(self, img, type)
            return path
        elif self.type == '3':
            img = ImageSearchHandle.SearchHandle(self.img).feelHash()
            type = "hamingFeel"
            path = Check.compOther(self, img, type)
            return path
        elif self.type == '4':
            img = ImageSearchHandle.SearchHandle(self.img).changeHash()
            type = "hamingChange"
            path = Check.compOther(self, img, type)
            return path

    def compWay(self, img):
        rs = db.db().select_path()
        mo = ImageCheckModel.ImageCheckModel()
        le = len(rs)
        r = []
        i = 0
        while i < le:
            temp = rs[i]
            tt = "app/" + temp[0]
            tt = ImageSearchHandle.SearchHandle(tt).ImageWay()
            r.append(mo.checkByImageWay(img, tt))
            i = i + 1
        res = max(r)
        ind = r.index(res) + 1
        path = db.db().getPath(ind)
        return path

    def compOther(self, img, type):
        rs = db.db().select(type)
        mo = ImageCheckModel.ImageCheckModel()
        le = len(rs)
        r = []
        i = 0
        while i < le:
            temp = rs[i]
            tt = temp[1]
            r.append(mo.checkByOther(img, tt))
            i = i + 1
        res = min(r)
        ind = r.index(res) + 1
        path = db.db().getPath(ind)
        return path
