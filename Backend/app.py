import os 
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes.web_routes import bp

load_dotenv(os.path.join(os.path.dirname(__file__),'.env'))

app = Flask(
    __name__,
    template_folder='../Web/resources',
    static_folder='../Web/assets',
    static_url_path='/assets'
)


#Cross origin resource sharing
#Access control allow origin دا تبعي يا رجالة
CORS(app)

app.register_blueprint(bp)



if __name__ == '__main__':
    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', '5000'))
    DEBUG = os.getenv('DEBUG', 'True').lower() 
    app.run(host=HOST, port=PORT, debug=DEBUG)

