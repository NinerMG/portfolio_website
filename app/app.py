from flask import Flask, render_template, redirect
import json
import os

app = Flask(__name__)


def load_projects():
    """Wczytuje projekty z pliku JSON"""
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'projects.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['projects']


def get_projects_by_language(lang='pl'):
    """Zwraca projekty w wybranym języku"""
    projects = load_projects()
    localized_projects = []
    
    for project in projects:
        localized_project = {
            'name': project['name'][lang],
            'description': project['description'][lang],
            'link': project['link'],
            'tags': project['tags'],
            'img_url': project['img_url']
        }
        localized_projects.append(localized_project)
    
    return localized_projects


@app.route('/')
def home():
    """Redirect to Polish version by default"""
    return redirect('/pl')


@app.route('/pl')
def home_pl():
    """Polish version"""
    projects = get_projects_by_language('pl')
    return render_template('index_pl.html', projects=projects, lang='pl')


@app.route('/en')
def home_en():
    """English version"""
    projects = get_projects_by_language('en')
    return render_template('index_en.html', projects=projects, lang='en')


if __name__ == '__main__':
    app.run(debug=True)