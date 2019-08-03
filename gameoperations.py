
from steem import Steem
import steembase

def prepareoperations(*args):

 account=args[0]
 vobject=args[1]
 vtype=args[2]
 global myplanet
 myjson={

            "id": "nextcolony",
            "json": {
              'username' : account,
              "type": vtype,
              "command":{"tr_var1": account,"tr_var2": "P-Z8GX19NDGF4","tr_var3": vobject}
            },
            "required_auths": [],
            "required_posting_auths": [account],
        }
 if vtype == "upgrade": myjson["json"]["command"] = {"tr_var1": "P-Z8GX19NDGF4", "tr_var2": vobject}

 ops=steembase.operations.CustomJson(myjson)

 return(ops)


if __name__ == "__main__":
    a=prepareoperations("lll","ioio","upgrade")
    print(a)
