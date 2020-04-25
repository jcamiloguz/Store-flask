from flask import Flask, jsonify, render_template
app = Flask(__name__)

from products import products

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/products')
def getproducts():
    return jsonify({"Products":products,"message":"Product's list"})
if __name__=='__main__':
    app.run(debug=True,port=4000)git