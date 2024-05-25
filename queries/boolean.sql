SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('+military -train' IN BOOLEAN MODE);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('"double-decker"' IN BOOLEAN MODE);
SELECT * FROM bus_characteristics WHERE MATCH(description) AGAINST('tra*' IN BOOLEAN MODE);
