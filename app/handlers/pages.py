import flask


from app.repositories import urls as urls_repository


def front_page():
    return flask.render_template("index.html")


def home():
    links = urls_repository.all()

    return flask.render_template("home.html", links=links)
