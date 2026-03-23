from flask import Flask, render_template, request, jsonify
import json
import os
import sys

app = Flask(__name__)

# Load local database
def load_database():
    """Load the local educational database"""
    db_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Global database
try:
    DATABASE = load_database()
except Exception as e:
    print(f"Failed to load database: {e}", file=sys.stderr)
    DATABASE = {'books': []}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if the service is running"""
    return jsonify({'status': 'ok', 'message': 'Local database service is running'}), 200

@app.route('/api/search', methods=['GET'])
def search_content():
    """Search for books and topics in local database"""
    query = request.args.get('q', '').strip().lower()
    
    if not query:
        return jsonify({'error': 'No search query provided'}), 400
    
    try:
        # Search local database
        results = search_database(query)
        
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        }), 200
    
    except Exception as e:
        print(f"Search error: {type(e).__name__}: {str(e)}", file=sys.stderr)
        return jsonify({'error': f'Search failed: {str(e)}'}), 500

@app.route('/api/book/<book_id>', methods=['GET'])
def get_book(book_id):
    """Get detailed book information"""
    try:
        book = fetch_book_by_id(book_id)
        
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        return jsonify(book), 200
    
    except Exception as e:
        return jsonify({'error': f'Failed to fetch book: {str(e)}'}), 500

def search_database(query):
    """Search the local database for matching books"""
    results = []
    books = DATABASE.get('books', [])
    
    for book in books:
        title_match = query in book.get('title', '').lower()
        author_match = query in book.get('author', '').lower()
        category_match = query in book.get('category', '').lower()
        desc_match = query in book.get('description', '').lower()
        
        if title_match or author_match or category_match or desc_match:
            results.append({
                'title': book['title'],
                'snippet': f"by {book['author']} ({book['year']}). {book['description'][:100]}...",
                'author': book['author'],
                'year': book['year'],
                'id': book['id'],
                'category': book['category']
            })
    
    # Sort by relevance (title match first, then author, then others)
    results.sort(
        key=lambda x: (
            query not in x['title'].lower(),
            query not in x['author'].lower()
        )
    )
    
    return results

def fetch_book_by_id(book_id):
    """Fetch a specific book from the database"""
    books = DATABASE.get('books', [])
    
    for book in books:
        if book['id'] == book_id:
            return {
                'title': book['title'],
                'description': book['description'],
                'author': book['author'],
                'year': book['year'],
                'category': book['category']
            }
    
    return None

if __name__ == '__main__':
    app.run(debug=True, port=5001)
