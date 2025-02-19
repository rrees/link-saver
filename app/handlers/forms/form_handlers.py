import flask

from .form_models import LinkForm


def link_form_submission():
    form = LinkForm(flask.request.form)

    if form.validate():
        return flask.redirect(flask.url_for("front_page"))

    return flask.abort(400, "Invalid form submission")
