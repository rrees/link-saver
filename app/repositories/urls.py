from .connection import connect

from .sql import urls as urls_sql


def create(url, notes=None, tags=None):
    if not notes:
        notes = ""

    if not tags:
        tags = []

    if isinstance(tags, str):
        tags = tags.split()

    params = {"url": url, "notes": notes, "tags": tags}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(urls_sql.insert, params)

            return cursor.fetchone().get("row")


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(urls_sql.all)

            return [row for row in cursor]


def by_tag(tag_name):
    params = {"tag_name": tag_name}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(urls_sql.tagged, params)

            return [row for row in cursor]
