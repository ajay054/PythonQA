## Select the database to work with
USE sakila;

## 1. Display the first & last names of all actors
SELECT first_name, last_name FROM actor;

## 1a. Concatenate first and last names of all actors into a single column
SELECT CONCAT(first_name, " ", last_name) AS Actor_Name FROM actor;

## 2a. Find the ID number, first name, and last name of an actor named "Joe"
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = "Joe";

## 2b. Find all actors whose last names contain the letters GEN
SELECT last_name
FROM actor
WHERE last_name LIKE '%GEN%';

## 2c. Find all actors whose last names contain the letters LI, ordered by last name and first name
SELECT last_name, first_name
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

## 2d. Retrieve specific countries using IN
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

## 3a. Add a column, modify, and drop it in the `actor` table
USE sakila;
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(45);

ALTER TABLE actor
MODIFY middle_name BLOB;

ALTER TABLE actor
DROP COLUMN middle_name;

## 4a. Count of each last name in the `actor` table
SELECT last_name, COUNT(last_name) AS "Count of Last Name"
FROM actor
GROUP BY last_name;

## 4a. Count of each last name in the `actor` table
SELECT last_name, COUNT(last_name) AS "Count of Last Name"
FROM actor
GROUP BY last_name;

## 4c. Update first name from "GROUCHO" to "HARPO" for actor with last name "WILLIAMS"
UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

## 4d. Update first name based on condition
UPDATE actor
SET first_name = CASE 
                    WHEN first_name = 'HARPO' THEN 'GROUCHO'
                    ELSE 'MUCHO GROUCHO'
                 END
WHERE actor_id = 172;

## 5a. Show the schema of the `address` table
SHOW CREATE TABLE address;

## 6a. Join staff and address tables to show each staff member's name and address
SELECT first_name, last_name, address
FROM staff s
INNER JOIN address a ON s.address_id = a.address_id;

## 6b. Calculate total payment by each staff member
SELECT first_name, last_name, SUM(amount) AS total_payment
FROM staff s
INNER JOIN payment p ON s.staff_id = p.staff_id
GROUP BY s.first_name, s.last_name;

## 6c. Count the number of actors in each film
SELECT f.title, COUNT(fa.actor_id) AS actor_count
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title;

## 6d. Count copies of the film "Hunchback Impossible" in inventory
SELECT COUNT(i.inventory_id) AS copies_count
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
WHERE f.title = "Hunchback Impossible";

## 6e. Sum of payment by each customer, ordered by last name alphabetically
SELECT c.last_name, c.first_name, SUM(p.amount) AS total_paid
FROM customer c
INNER JOIN payment p ON p.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY c.last_name ASC;

## 6f. Subquery for films starting with "K" or "Q" and in English
SELECT title
FROM film
WHERE language_id = (
    SELECT language_id
    FROM language
    WHERE name = "English"
) AND (title LIKE 'K%' OR title LIKE 'Q%');

## 7a. Subquery to find actors in the film "Alone Trip"
SELECT first_name, last_name
FROM actor
WHERE actor_id IN (
    SELECT actor_id
    FROM film_actor
    WHERE film_id = (
        SELECT film_id
        FROM film
        WHERE title = 'Alone Trip'
    )
);

## 7b. Find email addresses of Canadian customers using a LEFT JOIN
SELECT c.country, cu.last_name, cu.first_name, cu.email
FROM country c
LEFT JOIN customer cu ON c.country_id = cu.customer_id
WHERE c.country = 'Canada';

## 7c. List all family films (using the `film_list` view)
USE sakila;
SELECT title, category
FROM film_list
WHERE category = "Family";

 ## 7d. Most frequently rented movies in descending order
SELECT f.title, COUNT(r.rental_id) AS rental_count
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC;

## 7e. Total payment amount by store
SELECT s.store_id, SUM(p.amount) AS total_payment
FROM payment p
JOIN staff s ON p.staff_id = s.staff_id
GROUP BY s.store_id;

## 7f. Display store ID, city, and country for each store
SELECT st.store_id, cit.city, co.country
FROM store st
JOIN address ad ON st.address_id = ad.address_id
JOIN city cit ON ad.city_id = cit.city_id
JOIN country co ON cit.country_id = co.country_id;

## 7g. Top 5 grossing categories based on rental payments
SELECT c.name AS category, SUM(p.amount) AS total_gross
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY total_gross DESC
LIMIT 5;

## 8a. Create a view for the top 5 grossing genres
CREATE VIEW Top_Five_Grossing_Genres AS
SELECT c.name AS genre, SUM(p.amount) AS gross
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY gross DESC
LIMIT 5;

## 8b. Retrieve data from the view
SELECT * FROM Top_Five_Grossing_Genres;

## 8c. Drop the view if needed and recreate it
DROP VIEW IF EXISTS Top_Five_Grossing_Genres;

CREATE VIEW Top_Five_Grossing_Genres AS
SELECT c.name AS genre, SUM(p.amount) AS gross
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY gross DESC
LIMIT 5;
