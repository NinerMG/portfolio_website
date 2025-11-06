from flask import Flask, render_template, redirect

app = Flask(__name__)

# Projekty w języku polskim
MY_PROJECTS_PL = [
    {
        "name": "Morse Code Converter (Architektura & QA)",
        "description": "Wielomodułowa aplikacja (architektura MVC) z pełnym pokryciem testowym (Pytest). Udowadnia moją dbałość o jakość kodu, obsługę przypadków brzegowych i umiejętności inżynierskie (np. generowanie audio w NumPy).",
        "link": "https://github.com/NinerMG/MorseCodeConverter",
        "tags": ["OOP", "Tkinter", "Pytest", "NumPy", "QA"],
        "img_url": "images/projects/morse_code_generator.png"
    }
]

# Projekty w języku angielskim
MY_PROJECTS_EN = [
    {
        "name": "Morse Code Converter (Architecture & QA)",
        "description": "Multi-module application (MVC architecture) with full test coverage (Pytest). Demonstrates my attention to code quality, edge case handling, and engineering skills (e.g., audio generation in NumPy).",
        "link": "https://github.com/NinerMG/MorseCodeConverter",
        "tags": ["OOP", "Tkinter", "Pytest", "NumPy", "QA"],
        "img_url": "images/projects/morse_code_generator.png"
    }
]


@app.route('/')
def home():
    """Redirect to Polish version by default"""
    return redirect('/pl')


@app.route('/pl')
def home_pl():
    """Polish version"""
    return render_template('index_pl.html', projects=MY_PROJECTS_PL, lang='pl')


@app.route('/en')
def home_en():
    """English version"""
    return render_template('index_en.html', projects=MY_PROJECTS_EN, lang='en')


if __name__ == '__main__':
    app.run(debug=True)