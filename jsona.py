import json

# Sample JSON string (as received from an API)
json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby"
    
}
'''

# Parse JSON string to Python dictionary
book = json.loads(json_string)


print("Book Title:", book['title'])