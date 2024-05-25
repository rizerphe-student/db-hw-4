SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('double-decker' IN NATURAL LANGUAGE MODE);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('a bus' IN NATURAL LANGUAGE MODE);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('a double-decker bus vehicle automobile' IN NATURAL LANGUAGE MODE);
