import os
from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer
from app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    if os.getenv("SERVER_ENV") == "PRODUCTION":
        http_server = WSGIServer((str(os.getenv("SERVER_HOST"), int(os.getenv("SERVER_POST")))))
        http_server.serve_forever()
    else:
        app.run(debug=bool(os.getenv("SERVER_DEBUG"), host=str(os.getenv("SERVER_HOST"), port=int(os.getenv("SERVER_PORT")))))