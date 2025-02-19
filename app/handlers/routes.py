from . import pages

routes = [
    ("/", "front_page", pages.front_page, ["GET"]),
    ("/home", "home_page", pages.home, ["GET"]),
]
