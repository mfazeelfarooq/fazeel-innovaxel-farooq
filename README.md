# URL Shortener API

A robust and scalable URL shortening service built with Flask and MongoDB. This API allows you to create, manage, and track shortened URLs with a simple RESTful interface.

## Features

- 🔗 Create shortened URLs from long URLs
- 📊 Track URL statistics and usage
- 🔄 Update existing shortened URLs
- 🗑️ Delete shortened URLs
- 📋 List all shortened URLs
- 🔍 Get detailed information about specific URLs
- ⚡ Fast and efficient URL redirection

## Prerequisites

- Python 3.8+
- MongoDB Atlas account or local MongoDB instance
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd url-shortener
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following configuration:
```env
# MongoDB Configuration
MONGO_URI=your_mongodb_connection_string
MONGO_DB=url_shortener

# Flask Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. The API will be available at `http://localhost:5000`

3. To test the API endpoints, open a new terminal and run:
```bash
python test_api.py
```

Note: Make sure to keep the Flask server running in the first terminal while running the tests in the second terminal.

## API Endpoints

### Create Short URL
```http
POST /shorten
Content-Type: application/json

{
    "url": "https://example.com/very/long/url"
}
```

### Get URL Details
```http
GET /shorten/{short_code}
```

### Update URL
```http
PUT /shorten/{short_code}
Content-Type: application/json

{
    "url": "https://example.com/new/url"
}
```

### Delete URL
```http
DELETE /shorten/{short_code}
```

### Get URL Statistics
```http
GET /shorten/{short_code}/stats
```

### List All URLs
```http
GET /shorten
```

### Redirect to Original URL
```http
GET /{short_code}
```

## Testing

Run the test suite:
```bash
python test_api.py
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 204: Success (No Content)
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

## Security

- Environment variables for sensitive configuration
- Input validation for URLs
- Error handling and logging
- MongoDB connection security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
