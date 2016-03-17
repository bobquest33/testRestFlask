# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from testRestFlask import create_app


app = create_app(app_name="testRestFlask")
mgr = Manager(app)


@mgr.command
def run():
    app.run()


if __name__ == "__main__":
    mgr.run()
