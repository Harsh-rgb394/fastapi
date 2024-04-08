def singleitem(item)->dict:
    address=item.get("address",{})
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "age":int(item["age"]),
        "address":{
            "city":address.get("city"),
            "country":address.get("country")

        }

    }

def getallitems(items)->list:
    return [singleitem(item) for item in items]