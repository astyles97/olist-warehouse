CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;

COMMENT ON SCHEMA raw IS 'Untouched ingested data from CSVs';
COMMENT ON SCHEMA staging IS 'Lightly cleaned and typed';
COMMENT ON SCHEMA marts IS 'Star schema: dims and facts';