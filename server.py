from metasearch import scrape
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
        <html>
            <head>
                <title>Cheesy Metasearch Engine</title>
            </head>
            <body>
                <h2>This is a cheesy metasearch enginge. Go ahead and search for something!</h2>
                <br />
                <form action="/search" method="GET">
                    <input name="query" type="text">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>'''

@app.route('/search')
def search():
    if request.method == "GET":
        html = '''<!DOCTYPE html>
        <html>
            <head>
                <title>Cheesy Metasearch Engine</title>
            </head>
            <body>
                '''
        query = request.args.get('query', '')
        if len(query) > 0:
            for link in scrape(query):
                html = html + '<p><a href="' + link + '">' + link + '</a></p>'
        else:
            html = html + "<h3>Invalid request</h3>"

        html = html + '''</body>
        </html>'''
        return html
    else:
        return "Quit trying to hack me!"

@app.route('/test')
def test():
    return "test"
