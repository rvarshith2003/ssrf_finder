from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            return str(e)
    return 'Usage: /?url=<url_to_fetch>'

if __name__ == '__main__':
    app.run(debug=True)
