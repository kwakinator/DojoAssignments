SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2, city.city, country.country
FROM customer
JOIN address ON customer.address_id=address.address_id
JOIN city ON address.city_id=city.city_id
JOIN country ON city.country_id=country.country_id
WHERE city.city_id=312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id= film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name='Comedy';

SELECT actor.actor_id, CONCAT_ws(' ', actor.first_name, actor.last_name) AS name, film.title, film.release_year, film.description
FROM actor
JOIN film_actor ON actor.actor_id=film_actor.actor_id
JOIN film ON film_actor.film_id=film.film_id
WHERE film_actor.actor_id=5;

SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2, city.city, country.country, store.store_id
FROM customer
JOIN address ON customer.address_id=address.address_id
JOIN city ON address.city_id=city.city_id
JOIN country ON city.country_id=country.country_id
JOIN store ON store.store_id = customer.store_id
WHERE store.store_id=1
	AND city.city_id IN(1, 42, 312, 459);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id=15
	and film.rating='G'
    and film.special_features like '%Behind the Scenes';

SELECT CONCAT_ws(' ', actor.first_name, actor.last_name) as actor_name, actor.last_update
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id=369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Drama' and film.rental_rate = 2.99;

SELECT film.title, film.description, film.release_year, film.special_features, category.name AS genre, CONCAT_ws(' ', actor.first_name, actor.last_name)
FROM film 
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id=film_actor.actor_id
WHERE category.name = 'action' AND actor.first_name='Sandra' and actor.last_name = 'Kilmer';