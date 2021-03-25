SELECT version, parameters FROM SFibersStackCalibratorPar as conf  JOIN files ON
  files.start_time >= conf.valid_from AND files.stop_time <= conf.valid_to;

CREATE TABLE tablename LIKE configuration;

SELECT table_name FROM information_schema.tables WHERE table_name NOT IN ("configuration", "files") AND table_schema = "praktyki";

ALTER TABLE tablename ADD CONSTRAINT unique_version_date UNIQUE (valid_from,  version);


