from flask import Flask, render_template, request
import dao
from SaleApp.dao import load_products

app = Flask(__name__)

@app.route("/")
def index():
    name = "Thanh Tuan"
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    return render_template("index.html", name = name, prods = load_products(q=q, cate_id = cate_id))

@app.route("/product/<int:id>")
def details(id):
    return render_template("product-details.html")

@app.context_processor
def common_atribute():
    return{
        "cates": dao.load_category()
    }


if __name__ == "__main__":
    app.run(debug=True, port = 1507)
