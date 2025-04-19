from flask import Flask, request, jsonify, redirect, render_template
from flask_pymongo import PyMongo
from models import URL
from config import Config
import os
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB with proper error handling
try:
    mongo = PyMongo(app, uri=app.config['MONGO_URI'])
    # Get the database using the name from config
    db = mongo.cx[app.config['MONGO_DB']]
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

# Ensure the collection exists
if 'urls' not in db.list_collection_names():
    db.create_collection('urls')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Generate a short code
    short_code = generate_short_code()
    
    # Create a new URL document
    url = URL(original_url=original_url, short_code=short_code)
    
    # Save to MongoDB
    db.urls.insert_one(url.to_dict())
    
    return jsonify({
        'original_url': original_url,
        'short_url': f"{request.host_url}{short_code}",
        'short_code': short_code
    })

@app.route('/shorten/<short_code>', methods=['GET'])
def get_url(short_code):
    url_data = db.urls.find_one({'short_code': short_code})
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    url = URL.from_dict(url_data)
    return jsonify({
        'original_url': url.original_url,
        'short_code': url.short_code,
        'created_at': url.created_at.isoformat()
    })

@app.route('/shorten/<short_code>', methods=['PUT'])
def update_url(short_code):
    data = request.get_json()
    new_url = data.get('url')
    
    if not new_url:
        return jsonify({'error': 'URL is required'}), 400
    
    result = db.urls.update_one(
        {'short_code': short_code},
        {'$set': {'original_url': new_url}}
    )
    
    if result.matched_count == 0:
        return jsonify({'error': 'URL not found'}), 404
    
    return jsonify({'message': 'URL updated successfully'})

@app.route('/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    result = db.urls.delete_one({'short_code': short_code})
    
    if result.deleted_count == 0:
        return jsonify({'error': 'URL not found'}), 404
    
    return '', 204

@app.route('/shorten/<short_code>/stats', methods=['GET'])
def get_stats(short_code):
    url_data = db.urls.find_one({'short_code': short_code})
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    url = URL.from_dict(url_data)
    return jsonify({
        'original_url': url.original_url,
        'short_code': url.short_code,
        'created_at': url.created_at.isoformat()
    })

@app.route('/shorten', methods=['GET'])
def list_urls():
    urls = list(db.urls.find())
    return jsonify([{
        'original_url': url['original_url'],
        'short_code': url['short_code'],
        'created_at': url['created_at'].isoformat()
    } for url in urls])

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Find the URL document
    url_data = db.urls.find_one({'short_code': short_code})
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    url = URL.from_dict(url_data)
    return redirect(url.original_url)

def generate_short_code():
    import string
    import random
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(6))
        if not db.urls.find_one({'short_code': short_code}):
            return short_code

if __name__ == '__main__':
    app.run(debug=True)
