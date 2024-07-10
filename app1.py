from flask import Flask, request, render_template
import requests
import server

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        amazon_price, flipkart_price, croma_price = server.get_price(product_name)
        return render_template('form1.html', amazon_price=amazon_price, ebay_price=flipkart_price, walmart_price=croma_price)
    return render_template('form1.html', amazon_price='', ebay_price='', walmart_price='')

if __name__ == '__main__':
    app.run(debug=True)