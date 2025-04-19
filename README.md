# URL Shortener

A simple and efficient URL shortener built with Flask and SQLite. This application allows you to shorten long URLs and provides both a web interface and REST API endpoints.

## Features

- Modern web interface for URL shortening
- REST API endpoints for programmatic access
- Automatic redirection from short URLs to original URLs
- Access statistics tracking
- Copy to clipboard functionality
- Responsive design

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd url_shortener
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter a URL in the input field and click "Shorten URL"

## API Endpoints

### Create Short URL
```
POST /shorten
Content-Type: application/json

{
    "url": "https://example.com"
}
```

### Get URL Information
```
GET /shorten/<short_code>
```

### Update URL
```
PUT /shorten/<short_code>
Content-Type: application/json

{
    "url": "https://new-url.com"
}
```

### Delete URL
```
DELETE /shorten/<short_code>
```

### Get URL Statistics
```
GET /shorten/<short_code>/stats
```

## Project Structure

```
url_shortener/
├── app.py              # Main application file
├── models.py           # Database models
├── utils.py            # Utility functions
├── templates/          # HTML templates
│   └── index.html     # Web interface
└── instance/          # Database file location
```

## Technologies Used

- Flask - Web framework
- SQLite - Database
- Bootstrap 5 - Frontend framework
- JavaScript - Frontend interactivity

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation
- Bootstrap documentation