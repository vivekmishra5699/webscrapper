'''from flask import Flask, request, render_template
from scrape import get_amazon_price  # Importing the function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        product_url = request.form.get('product_url')
        price = get_amazon_price(product_url)  # Now the function is accessible
        return render_template('form.html', price=price)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)'''
