USE sakila; #use the database

SET SQL_SAFE_UPDATES = 0; #set safe updates to 0

#1.a
SELECT first_name, last_name FROM actor; 

#1.b
ALTER TABLE actor ADD actor_name VARCHAR(60); 
UPDATE actor
SET actor_name = CONCAT(first_name, ' ', last_name);

#2.a
SELECT actor_id, first_name, last_name  
FROM actor
WHERE first_name = 'Joe';

#2.b
SELECT * FROM actor WHERE last_name LIKE '%GEN%'; 

#2.c
SELECT * FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name; 

#2.d
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China'); 

#3.a
ALTER TABLE actor ADD middle_name varchar(30) AFTER first_name; 

#3.b
ALTER TABLE actor MODIFY middle_name BLOB; 

#3.c
ALTER TABLE actor DROP middle_name; 

#4.a
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name; 

#4.b
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name HAVING COUNT(*) > 1; 

#4.c
UPDATE actor SET first_name='Harpo' WHERE first_name = 'Groucho' AND last_name = 'Williams'; 

#4.d

#5.a
SHOW CREATE TABLE address; 

#6.a
SELECT first_name, last_name, address FROM staff JOIN address ON address.address_id = staff.address_id; 

#6.b
SELECT first_name, last_name, SUM(amount) FROM staff JOIN payment ON staff.staff_id = payment.staff_id GROUP BY first_name; 

#6.c
SELECT title, count(actor_id) FROM film INNER JOIN film_actor on film.film_id = film_actor.film_id GROUP BY film.film_id; 

#6.d
SELECT COUNT(inventory.film_id) FROM inventory 
JOIN film ON inventory.film_id = film.film_id 
WHERE film.film_id IN (SELECT film.film_id FROM film WHERE title = 'Hunchback Impossible'); 

#6.e
SELECT customer.first_name, customer.last_name, SUM(payment.amount) FROM payment
JOIN customer ON payment.customer_id = customer.customer_id
GROUP BY payment.customer_id ORDER BY customer.last_name, customer.first_name;

#7.a
SELECT title FROM film 
JOIN language ON film.language_id = language.language_id
WHERE title LIKE 'Q%' OR title LIKE 'P%'
AND language.language_id IN(SELECT language.language_id FROM language WHERE name = 'English');

#7.b
SELECT actor.first_name, actor.last_name FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id IN (SELECT film_actor.film_id FROM film_actor
							 JOIN film ON film.film_id = film_actor.film_id
                             WHERE film.title = 'Alone Trip');
                             
#7.c
SELECT customer.first_name, customer.last_name FROM customer
JOIN address ON address.address_id = customer.address_id
WHERE address.address_id IN (SELECT address.address_id FROM address
							 JOIN city ON city.city_id = address.city_id
                             WHERE city.country_id IN (SELECT city.country_id FROM city
													JOIN country ON country.country_id = city.country_id
                                                    WHERE country.country = 'Canada'));
                                                    
#7.d
SELECT film.title from film
JOIN film_category ON film_category.film_id = film.film_id
WHERE film_category.category_id IN (SELECT film_category.category_id FROM film_category
									JOIN category on category.category_id = film_category.category_id
                                    WHERE category.name = 'Family');
                                    
#7.e
SELECT film.title, COUNT(rental.rental_id) AS total_rentals FROM film
JOIN inventory ON inventory.film_id = film.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
GROUP BY film.title;

#7.f
SELECT store.store_id, SUM(payment.amount) AS revenue_store FROM store
JOIN staff ON staff.store_id = store.store_id
JOIN payment ON payment.staff_id = staff.staff_id
GROUP BY store.store_id;

#7.g
SELECT store.store_id, city.city, country.country FROM store
JOIN address ON address.address_id = store.store_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id;

#7.h
SELECT category.name, SUM(payment.amount) AS top_5 FROM category
JOIN film_category ON film_category.category_id = category.category_id
JOIN inventory ON inventory.film_id = film_category.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
JOIN payment ON payment.rental_id = rental.rental_id
GROUP BY category.name
ORDER BY top_5 desc
LIMIT 5;

#8.a
CREATE VIEW top_5_categories AS
	SELECT category.name, SUM(payment.amount) AS top_5 FROM category
	JOIN film_category ON film_category.category_id = category.category_id
	JOIN inventory ON inventory.film_id = film_category.film_id
	JOIN rental ON rental.inventory_id = inventory.inventory_id
	JOIN payment ON payment.rental_id = rental.rental_id
	GROUP BY category.name
	ORDER BY top_5 desc
	LIMIT 5;
    
#8.b
#I would use a histogram to display this information for a quick snapshot of the data

#8.c
DROP VIEW top_5_categories;