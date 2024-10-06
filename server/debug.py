#!/usr/bin/env python3

from app import app
from models import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()  # This will set a breakpoint for debugging
        app.run(debug=True)  # Start the Flask app in debug mode


        