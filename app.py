from flask import Flask

# Flask "aufrufen"
app = Flask(__name__)

# Debugger aktivieren
# Dient dazu bei Aktualisierung nicht ständig Server neuzustarten
app.debug = True

# Ausgabe beim Starten der Datei
@app.route('/')
def index():
    return 'INDEX'

if __name__ == '__main__':
    app.run()