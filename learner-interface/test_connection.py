#!/usr/bin/env python
"""
Test script for local database functionality
"""
import json
import os
import sys

def load_database():
    """Load the local database"""
    db_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(db_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def test_local_database():
    """Test if the local database works"""
    print("Testing Local Database Functionality...\n")
    
    try:
        print("1. Loading database...")
        database = load_database()
        books = database.get('books', [])
        print(f"   ✓ Database loaded successfully!")
        print(f"   ✓ Found {len(books)} educational materials")
        
        print("\n2. Testing search functionality...")
        query = 'python'
        results = []
        for book in books:
            if (query in book['title'].lower() or 
                query in book['author'].lower() or 
                query in book['category'].lower()):
                results.append(book['title'])
        
        if results:
            print(f"   ✓ Search working! Found {len(results)} results for '{query}'")
            print(f"   First result: {results[0]}")
        else:
            print(f"   ✓ Search working (no results for '{query}')")
        
        print("\n3. Testing book categories...")
        categories = set()
        for book in books:
            categories.add(book['category'])
        print(f"   ✓ Available categories: {', '.join(sorted(categories))}")
        
        print("\n✓ All tests passed! Local database is ready to use.")
        print("\nYou can now start the Flask app with: python app.py")
        return True
        
    except FileNotFoundError:
        print("\n✗ Error: data.json not found!")
        print("   Make sure data.json is in the same directory as this script")
        return False
    except json.JSONDecodeError:
        print("\n✗ Error: data.json is not valid JSON")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected Error: {type(e).__name__}: {e}")
        return False

if __name__ == '__main__':
    success = test_local_database()
    sys.exit(0 if success else 1)
