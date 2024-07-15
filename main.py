from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

wardrobe = {
    'hats': [],
    'tops': [],
    'bottoms': [],
    'underwear': [],
    'socks': [],
    'shoes': [],
    'accessories': []
}

@app.route('/')
def index():
    return render_template('index.html', wardrobe=wardrobe)

@app.route('/add_item', methods=['POST'])
def add_item():
    category = request.form['category']
    item = request.form['item']
    wardrobe[category].append(item)
    return redirect(url_for('index'))

@app.route('/choose_outfit')
def choose_outfit():
    outfit = {}
    for category in wardrobe:
        if wardrobe[category]:
            outfit[category] = random.choice(wardrobe[category])
        else:
            outfit[category] = "未登録"
    return render_template('outfit.html', outfit=outfit)

if __name__ == '__main__':
    app.run(debug=True)