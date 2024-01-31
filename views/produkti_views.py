from flask import (
    request,
    render_template,
    redirect
)
from models import (
    Produkts,
    ProduktsNoma,
    Kategorija,
    Nomnieks,
    Noma
)
from __init__ import db

def produkti():
    if request.method == "POST":
        pass
    else:
        visi_produkti = db.session.query(Produkts, Kategorija).join(Kategorija).all()
        #print(visi_produkti)
        #for produkts, kategorija in visi_produkti:
        #    print(produkts)
        #    print(kategorija)
        return render_template(
            "produkti.html",
            produkti=visi_produkti)
produkti.methods = ["GET", "POST"]