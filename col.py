from steem import Steem
import time
import datetime
import planets
import random
from steem.transactionbuilder import TransactionBuilder
import gameoperations
import  settings

print("empezamos")

cl=settings.mylist["key"]
s = Steem(keys=[cl])
#myplanet=settings.mylist["myplanet"]

def custom_json():

    global s
    minelist=planets.getskills()
    if not minelist:  print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')," ningun mine skill o building "); return

    vsele=random.randint(0,len(minelist) -1)
    account = settings.mylist["myuser"]
    ops=gameoperations.prepareoperations(account,minelist[vsele]["name"],minelist[vsele]["tipo"])
    tb = TransactionBuilder()
    tb.appendOps(ops)
    tb.appendSigner(account, "posting")
    tb.sign()
    tb.broadcast()
    print((datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),minelist[vsele]["name"]))


while True:
 custom_json()
 print("sleeping 1800")
 time.sleep(1800)