import wtforms

from wtforms import validators


class LinkForm(wtforms.form.Form):
    url = wtforms.URLField("url", [validators.InputRequired()])
    notes = wtforms.TextAreaField("notes")
    tags = wtforms.StringField("tags")
