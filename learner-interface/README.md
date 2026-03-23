# Learner Interface

A simple, fast web application for searching educational content from a **local database**. No external API calls needed!

## Features

- **Local Database**: All content stored locally - fast and reliable
- **Simple Search Interface**: Search by title, author, topic, or category
- **No Network Issues**: Works offline with zero connectivity problems
- **Multiple Categories**: Programming, Physics, Biology, History, Psychology, and more
- **Responsive Design**: Works on desktop and mobile devices

## Project Structure

```
learner-interface/
├── app.py                 # Flask backend with local database search
├── data.json              # Local educational content database
├── test_connection.py     # Database functionality test
├── templates/
│   └── index.html        # Web interface with search box
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
   ```bash
   cd learner-interface
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

## Running the Application

### 1. Test the Database First

```bash
python test_connection.py
```

You should see:
- ✓ Database loaded successfully!
- ✓ Search working!
- ✓ Available categories

### 2. Start the Flask Server

```bash
python app.py
```

### 3. Open in Browser

Navigate to:
```
http://localhost:5001
```

## Usage

### Basic Search

1. Type any keyword in the search box (e.g., "Python", "Machine Learning", "History")
2. Press Enter or click the Search button
3. Browse through the results
4. Click on any result to read the full description

### Example Searches

- **Programming**: "python", "web development", "algorithms"
- **Science**: "physics", "biology", "chemistry"
- **History & Social Studies**: "history", "economics", "psychology"
- **Authors**: "Hawking", "watson", "Skiena"

## API Endpoints

### GET `/api/search`
Searches the local database for educational content.

**Query Parameters:**
- `q` (required): Search query

**Response:**
```json
{
  "query": "python",
  "results": [
    {
      "title": "Python Programming for Beginners",
      "snippet": "by Mark Lutz (2013). A comprehensive guide...",
      "author": "Mark Lutz",
      "year": 2013,
      "id": "python-programming",
      "category": "Programming"
    }
  ],
  "count": 1
}
```

### GET `/api/book/<book_id>`
Fetches full details of a specific book.

**Parameters:**
- `book_id` (required): Unique book identifier

**Response:**
```json
{
  "title": "Python Programming for Beginners",
  "description": "A comprehensive guide to learning Python...",
  "author": "Mark Lutz",
  "year": 2013,
  "category": "Programming"
}
```

### GET `/api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "message": "Local database service is running"
}
```

## Database Content

The application includes 12+ educational materials covering:

- **Programming**: Python, Web Development, Algorithms, Databases
- **Data Science & ML**: Machine Learning, Data Science with Python
- **Sciences**: Physics, Biology
- **History & Social Sciences**: History, Economics, Psychology

All stored locally in `data.json`

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data**: JSON local database
- **API Type**: RESTful JSON API

## Advantages of Local Database

✅ **Speed**: Instant search results - no network latency  
✅ **Reliability**: Works offline - no external dependencies  
✅ **Privacy**: All data stays on your system  
✅ **No Issues**: No timeouts, SSL errors, or proxy problems  
✅ **Simple**: Pure local data - zero complexity  

## Adding More Content

To add more books/topics to the database:

1. Open `data.json`
2. Add a new entry to the `books` array with fields:
   - `id`: Unique identifier (lowercase, with hyphens)
   - `title`: Book/Topic title
   - `author`: Author name
   - `year`: Publication year
   - `category`: Topic category
   - `description`: Detailed description (max 500 chars recommended)

Example:
```json
{
  "id": "quantum-computing",
  "title": "Introduction to Quantum Computing",
  "author": "Phillip Kaye",
  "year": 2014,
  "category": "Computer Science",
  "description": "A guide to quantum computing fundamentals..."
}
```

## Troubleshooting

**Search returns no results:**
- Try different keywords or more specific terms
- Check the available categories

**Port already in use:**
- Edit app.py and change `port=5001` to another number
- Or stop other applications using port 5001

**Database not loading:**
- Ensure `data.json` is in the same directory as `app.py`
- Check that `data.json` has valid JSON syntax

## License

Feel free to use this application for educational and personal purposes.

