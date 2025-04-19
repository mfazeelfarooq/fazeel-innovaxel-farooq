from flask import Flask, request, jsonify, abort, render_template, redirect
from models import db, URL
from utils import generate_short_code
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def create_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    short_code = generate_short_code()
    while URL.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code()

    new_url = URL(url=url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "id": new_url.id,
        "url": new_url.url,
        "shortCode": new_url.short_code,
        "createdAt": new_url.created_at.isoformat(),
        "updatedAt": new_url.updated_at.isoformat()
    }), 201

@app.route('/shorten/<short_code>', methods=['GET'])
def get_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)

    url_entry.access_count += 1
    db.session.commit()

    return jsonify({
        "id": url_entry.id,
        "url": url_entry.url,
        "shortCode": url_entry.short_code,
        "createdAt": url_entry.created_at.isoformat(),
        "updatedAt": url_entry.updated_at.isoformat()
    })

@app.route('/shorten/<short_code>', methods=['PUT'])
def update_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)

    data = request.get_json()
    new_url = data.get('url')
    if not new_url:
        return jsonify({'error': 'New URL is required'}), 400

    url_entry.url = new_url
    db.session.commit()

    return jsonify({
        "id": url_entry.id,
        "url": url_entry.url,
        "shortCode": url_entry.short_code,
        "createdAt": url_entry.created_at.isoformat(),
        "updatedAt": url_entry.updated_at.isoformat()
    })

@app.route('/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)

    db.session.delete(url_entry)
    db.session.commit()
    return '', 204

@app.route('/shorten/<short_code>/stats', methods=['GET'])
def get_stats(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)

    return jsonify({
        "id": url_entry.id,
        "url": url_entry.url,
        "shortCode": url_entry.short_code,
        "createdAt": url_entry.created_at.isoformat(),
        "updatedAt": url_entry.updated_at.isoformat(),
        "accessCount": url_entry.access_count
    })

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if not url_entry:
        abort(404)
    
    url_entry.access_count += 1
    db.session.commit()
    
    return redirect(url_entry.url)

if __name__ == '__main__':
    # Ensures database tables are created before the app starts
    with app.app_context():
        db.create_all()

    app.run(debug=True)
