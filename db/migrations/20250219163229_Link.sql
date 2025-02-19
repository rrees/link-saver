--migrate:up

CREATE OR REPLACE FUNCTION update_modified_column() 
	RETURNS TRIGGER AS $$
	BEGIN
	    NEW.modified = now();
	    RETURN NEW; 
	END;
	$$ language 'plpgsql';


CREATE TABLE IF NOT EXISTS links (
	id INT GENERATED ALWAYS AS IDENTITY,
	external_id uuid UNIQUE NOT NULL DEFAULT gen_random_uuid (),
	url text NOT NULL,
	notes text NULL,
	tags text[] NULL,
	created timestamp default current_timestamp,
	updated timestamp default current_timestamp
);

CREATE TRIGGER update_links_modtime
BEFORE UPDATE ON links
FOR EACH ROW EXECUTE PROCEDURE update_modified_column();


-- migrate:down

DROP TRIGGER IF EXISTS update_links_modtime ON links;

DROP TABLE IF EXISTS links;

DROP FUNCTION update_modified_column;