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

if __name__ == '__main__':
    app.run(debug=True)
