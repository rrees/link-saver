insert = """
INSERT INTO links(
	url,
	notes,
	tags
) VALUES (
	%(url)s,
	%(notes)s,
	%(tags)s
)
ON CONFLICT DO NOTHING
RETURNING (id, external_id)
;
"""

all = """
SELECT *
FROM links
ORDER BY created DESC
"""
