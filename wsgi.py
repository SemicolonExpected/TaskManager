from os import environ, path
from task_manager import create_app
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = create_app(environ['FLASK_CONFIG'])
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
