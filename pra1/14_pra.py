from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "HELLO WORLD"


app.run(port=8000)

#FLASKnoモジュールをインポート