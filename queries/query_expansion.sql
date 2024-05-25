SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('double-decker bus' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('military vehicle' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('a military bus with an automobile on a bus' IN NATURAL LANGUAGE MODE WITH QUERY EXPANSION);
