import sys
import string
import random
from urllib.parse import urlparse

from flask import Flask, request, jsonify, redirect
from database import db_session, init_db, init_engine
from models import Url


app = Flask(__name__)


def short_url_exists(url):
    if not url:
        return True
    return Url.query.filter(Url.short_url == url).count() != 0


def get_random_short_url():
    """Generates a random string of 7 ascii letters and digits
    Can provide in the order or 10^12 unique strings
    """
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for _ in range(7))


def get_new_short_url():
    """Generate random urls until a new one is generated"""
    url = None
    while short_url_exists(url):
        url = get_random_short_url()
    return url


@app.route('/', methods=['POST'])
def shorthen():
    req_url = request.get_json(force=True)['url']
    
    url = Url.query.filter(Url.url == req_url).first()
    
    if not url:
        scheme = urlparse(req_url).scheme
        if not scheme: # check if url contains http://
            req_url = 'http://' + req_url
        
        short_url = get_new_short_url()
        db_session.add(Url(req_url, short_url))
        db_session.commit()
    else:
        short_url = url.short_url # I'm fucking sorry
    
    return jsonify(url=req_url, short_url=app.config['API_URL'] + short_url)


@app.route('/<short_url>', methods=['GET'])
def get_shorten_url(short_url):
    
    short_url = Url.query.filter(Url.short_url == short_url).first()
    if not short_url:
        return 'The requested url does not exist.', 404
    else:
        url = short_url.url # I'm sorry again
        return redirect(url, code=302)


if __name__ == "__main__":
    app.config.from_pyfile('config/default_config.py')

    if len(sys.argv) == 2:
        conf = sys.argv[1]
        print('Loading additional config %s...', conf)
        app.config.from_pyfile('config/' + conf + '_config.py')

    init_engine(app.config['DATABASE_URI'])
    init_db()
    app.run()