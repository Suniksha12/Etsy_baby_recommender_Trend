import os
from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('product_data.csv')

data['Price'] = data['Price'].astype(str).str.replace(r'[^\d.-]', '', regex=True)
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

data = data.assign(favorites=data['favorites'].fillna(0), 
                   numberOfReviews=data['numberOfReviews'].fillna(0))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommend():
    user_input = request.json
    print(f"User input: {user_input}")

    try:
        price = float(user_input.get('price'))
        favorites = int(user_input.get('favorites'))
        reviews = int(user_input.get('reviews'))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input: price, favorites, and reviews must be numbers."}), 400

    data['score'] = (
        (data['Price'] - price).abs() * 0.5 + 
        (data['favorites'] - favorites).abs() * 0.3 + 
        (data['numberOfReviews'] - reviews).abs() * 0.2
    )

    top_products = data.sort_values(by='score').head(5)

    recommendations = top_products[['name', 'Price', 'favorites', 'numberOfReviews']].to_dict(orient='records')

    response = {
        "message": "Here are your top 5 recommended products based on your preferences:",
        "recommendations": recommendations,
        "count": len(recommendations)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


