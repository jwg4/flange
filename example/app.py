from flask import Flask
from flange import Flange

app = Flask(__name__)
fl = Flange()
fl.init_app(app)

@fl.service_endpoint("/data/chickens")
def get_chickens():
    data = {
        'chickens': [
            "Chicken Licken",
            "Henny Penny"
        ]
    }
    return data


if __name__ == '__main__':
    app.run()
