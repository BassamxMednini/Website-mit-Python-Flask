from flask import Flask, render_template

# Flask "aufrufen"
app = Flask(__name__)

# Debugger aktivieren
# Dient dazu bei Aktualisierung nicht ständig Server neuzustarten
app.debug = True

# Ausgabe beim Starten der Datei
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()