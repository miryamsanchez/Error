import random
from flask import Flask, abort, render_template

# Creación del objeto que controla la aplicación
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
        app.run(debug=True)

