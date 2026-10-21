import json

def load_category():
    with open("data/categories.json", encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None, cate_id=None):
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)

        if q:
            prods = [p for p in prods if p["name"].find(q) >= 0]
        if cate_id:
            prods = [p for p in prods if p["id_cates"].__eq__(int(cate_id))]

        return prods

if __name__=="__main":
    print(load_category())