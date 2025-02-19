import flask

from app.repositories import urls as urls_repository

from .form_models import LinkForm


def link_form_submission():
    form = LinkForm(flask.request.form)

    if form.validate():
        urls_repository.create(form.url.data)
        return flask.redirect(flask.url_for("front_page"))

    return flask.abort(400, "Invalid form submission")
