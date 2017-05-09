use world;

SELECT countries.name AS Name, languages.language AS Language, languages.percentage AS Percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.language= 'Slovene' 
ORDER BY percentage DESC;


SELECT countries.name AS country, COUNT(cities.id) AS cities 
FROM countries
JOIN cities ON countries.id=cities.country_id
GROUP BY countries.name
ORDER BY cities DESC;

SELECT cities.name, cities.population
FROM countries
JOIN cities on countries.id=cities.country_id
WHERE countries.name = 'Mexico' and cities.population > 500000;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages on countries.id = languages.country_id
WHERE percentage > 89
ORDER BY languages.percentage DESC; 

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 and population > 100000;

SELECT name, life_expectancy, government_form , capital
FROM countries
WHERE government_form = 'Constitutional Monarchy' and life_expectancy > 75 and capital > 200;

