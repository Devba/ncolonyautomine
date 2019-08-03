import urllib.request, json,datetime,time
import settings
vplanetresources=[];coalactual=[];oreactual=[];copperactual=[];uraniumactual=[]
vplanetbuildings=[]
res=[]
planetname=settings.mylist["myplanet"]
user=settings.mylist["myuser"]
planetskills=[]


def planetresources():
    global vplanetresources,planetname
    url = "https://api.nextcolony.io/loadqyt?id=" + planetname
    with urllib.request.urlopen(url) as r:     vplanetresources = json.load(r)


def planetbuildings():
    global vplanetbuildings,planetname
    url = "https://api.nextcolony.io/loadbuildings?id="+planetname
    with urllib.request.urlopen(url) as r:   vplanetbuildings= json.load(r)


def actualresources():
    global vplanetresources
    global coalactual,oreactual,copperactual,uraniumactual

    lastupdatesec = (time.time() - vplanetresources["lastUpdate"]) / 86400

    coalactual = (lastupdatesec * vplanetresources["coalrate"]) + vplanetresources["coal"]
    oreactual = (lastupdatesec * vplanetresources["orerate"]) + vplanetresources["ore"]
    copperactual = (lastupdatesec * vplanetresources["copperrate"]) + vplanetresources["copper"]
    uraniumactual = (lastupdatesec * vplanetresources["uraniumrate"]) + vplanetresources["uranium"]

def getskills():
    global coalactual, oreactual, copperactual, uraniumactual
    global vplanetresources,planetskills
    global res,user
    planetresources()
    actualresources()

    res=[]
    url = "https://api.nextcolony.io/loadskills?user=" +user
    with urllib.request.urlopen(url) as r:
        planetskills = json.load(r)
        for l in planetskills:
            diftime= l["busy"] -time.time()
            difcoal=coalactual -l["coal"]
            difcopper = copperactual - l["copper"]
            difore = oreactual - l["ore"]
            difuranium = uraniumactual - l["uranium"]
            #skilllevel=[v["current"] for v in planetskills if v["name"] == "oremine"][0]

            if diftime<0 and difcoal>0 and difcopper>0 and difore>0 and difuranium>0 and "mine" in l["name"] :l["tipo"] = "enhance"; res.append(l)


        getbuildings()
        return (res)


def getbuildings():
    global coalactual, oreactual, copperactual, uraniumactual
    global vplanet
    global vplanetbuildings,res
    global user,planetskills
    planetbuildings()


    for l in vplanetbuildings:
            diftime= l["busy"] -time.time()
            difcoal=coalactual -l["coal"]
            difcopper = copperactual - l["copper"]
            difore = oreactual - l["ore"]
            difuranium = uraniumactual - l["uranium"]
            skilllevel=[v["current"] for v in planetskills if v["name"] == l["name"]][0]

            if diftime<0 and difcoal>0 and difcopper>0 and difore>0 and difuranium>0 and ("mine" in l["name"] or "depot" in l["name"]) and skilllevel>=l["current"]:
                    l["tipo"] = "upgrade"
                    res.append(l)

if __name__ == "__main__":
 getbuildings()