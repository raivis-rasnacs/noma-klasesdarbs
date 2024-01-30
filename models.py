from __init__ import db

class Nomnieks(db.Model):
    __table__ = db.Model.metadata.tables["Nomnieks"]

class Noma(db.Model):
    __table__ = db.Model.metadata.tables["Noma"]

class Nomnieks(db.Model):
    __table__ = db.Model.metadata.tables["Kategorija"]

class Produkts(db.Model):
    __table__ = db.Model.metadata.tables["Produkts"]

class ProduktsNoma(db.Model):
    __table__ = db.Model.metadata.tables["ProduktsNoma"]