from . import pages

routes = [
    ("/", "front_page", pages.front_page, ["GET"]),
    ("/home", "home_page", pages.home, ["GET"]),
    ("/links", "links", pages.links, ["GET"]),
    ("/links/tagged/<tag_name>", "links_by_tag", pages.tag, ["GET"]),
]
