use twitter;

INSERT INTO users (first_name, last_name, handle, birthday, created_at, updated_at)
VALUES('Harry', 'Potter', 'no1wizard', '1998-12-12', NOW(), NOW());

SELECT * FROM users;

DELETE FROM users
WHERE id='10';

SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) AS full_name FROM users;

select concat_ws(' ', 'hello', first_name, last_name) AS full_name FROM users;

select users.first_name, users.last_name, tweets.tweet
from users
join tweets ON users.id = tweets.user_id;

select * from tweets;


select *
from users
left join tweets on users.id=tweets.user_id
where users.id='1';