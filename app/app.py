from flask import Flask, render_template

app = Flask(__name__)

MY_PROJECTS = [
    {
        "name": "Morse Code Converter (Architektura & QA)",
        "description": "Wielomodułowa aplikacja (architektura MVC) z pełnym pokryciem testowym (Pytest). Udowadnia moją dbałość o jakość kodu, obsługę przypadków brzegowych i umiejętności inżynierskie (np. generowanie audio w NumPy).",
        "link": "https://github.com/NinerMG/MorseCodeConverter",
        "tags": ["OOP", "Tkinter", "Pytest", "NumPy", "QA"],
        "img_url": "images/projects/morse_code_generator.png"
    }
]


@app.route('/')
def home():
    return render_template('index.html', projects=MY_PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)