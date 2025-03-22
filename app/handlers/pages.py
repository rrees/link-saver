import flask


from app.repositories import urls as urls_repository


def front_page():
    return flask.render_template("index.html")


def home():
    links = urls_repository.all()

    return flask.render_template("home.html", links=links)


def links():
    links = urls_repository.all()

    return flask.render_template("links.html", links=links)


def tag(tag_name):
    return flask.render_template(
        "links-by-tag.html", tag_name=tag_name, links=urls_repository.by_tag(tag_name)
    )
