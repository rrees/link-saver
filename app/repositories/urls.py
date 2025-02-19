from .connection import connect

from .sql import urls as urls_sql


def create(url, notes=None, tags=None):
    if not notes:
        notes = ""

    if not tags:
        tags = []

    params = {"url": url, "notes": notes, "tags": tags}

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(urls_sql.insert, params)

            return cursor.fetchone().get("row")
