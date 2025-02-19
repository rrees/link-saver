from . import form_handlers

routes = [
    (
        "/forms/link/submit",
        "link_form_submission",
        form_handlers.link_form_submission,
        ["POST"],
    )
]
