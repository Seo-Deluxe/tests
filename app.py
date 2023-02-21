from flask import Flask, render_template, request
from search_engine_parser import GoogleSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        url = request.form['url']
        queries = request.form['queries'].split('\n')
        region = request.form['region']
        city = request.form['city']
        state = request.form['state']
        search_engine = request.form['search_engine']
        search = GoogleSearch()

        results = []
        for query in queries:
            params = {
                'q': query,
                'location': f'{city}, {state}, {region}'
            }
            if search_engine == 'google':
                data = search.search(query, num_results=100, **params)
                positions = [i+1 for i, d in enumerate(data) if d['link'] == url]
                results.append({'query': query, 'positions': positions})

        return render_template('results.html', results=results)

    return render_template('index.html')