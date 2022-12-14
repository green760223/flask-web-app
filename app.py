from flask import Flask, render_template
import os
from handleRequests import index_path

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(index_path)


def main():
    port = int(os.environ.get('PORT', 4000))
    return port


if __name__ == "__main__":
    port_number = main()
    app.run(debug=False, port=port_number, host='0.0.0.0')
