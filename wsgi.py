from os import environ, path
from task_manager import create_app
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = create_app(environ['FLASK_CONFIG'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
