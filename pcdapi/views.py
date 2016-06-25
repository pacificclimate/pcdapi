from flask.ext.sqlalchemy import SQLAlchemy

import ce.api

def add_routes(app):

    db = SQLAlchemy(app)

    @app.route("/<request_type>")
    def api_request(*args, **kwargs):
        return ce.api.call(db.session, *args, **kwargs)
