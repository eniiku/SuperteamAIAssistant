







    app.run(debug=True)if __name__ == "__main__":app.register_blueprint(bot_bp)app = Flask(__name__)from .bot import bot_bpfrom flask import Flask