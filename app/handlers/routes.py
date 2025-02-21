from . import pages

routes = [
    ("/", "front_page", pages.front_page, ["GET"]),
    ("/home", "home_page", pages.home, ["GET"]),
    ("/links/tagged/<tag_name>", "post_by_tag", pages.tag, ["GET"]),
]
