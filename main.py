from flask import Flask, send_file, render_template, request, jsonify
from flask_cors import CORS
from wikipedia import wikiFind
from wikiSearch import searchQ

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})


@app.route('/wiki')
def wiki():
    if request.method == 'GET':
        return jsonify(wikiFind(request.args.get('link')))


@app.route('/wikisearch')
def wikisearch():
    if request.method == 'GET':
        return jsonify(searchQ(request.args.get('q')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
