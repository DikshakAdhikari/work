from flask import Flask,jsonify,request

app= Flask(__name__)

books= [
    {"id":1, "book":"Book 1", "author":"Author 1"},
    {"id":2, "book":"Book 2", "author":"Author 2"},
    {"id":3, "book":"Book 3", "author":"Author 3"},
    {"id":4, "book":"Book 4", "author":"Author 4"},
    {"id":5, "book":"Book 5", "author":"Author 5"},
]

@app.route('/', methods=["GET"])
def get_books():
    return jsonify(books)

@app.route('/<int:bookId>', methods=["GET"])
def get_by_id(bookId):
    return jsonify(bookId)

@app.route('/', methods=["POST"])
def post_book():
    new_book=  {"id":request.json["id"],"book":request.json["book"], "author":request.json["author"]}
    books.append(new_book)
    return jsonify(books)

@app.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book_single in books:
        if(book_single['id'] == book_id):
            return jsonify({'message':'User updated successfully!'})
    return jsonify('Error: Book not found')

if __name__ == '__main__':
    app.run(debug=True)
