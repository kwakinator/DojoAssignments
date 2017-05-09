/* 
INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 1, 2);

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 1, 3);

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 1, 4);

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 2, 1);

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 3, 1);

INSERT INTO friendships(created_at, updated_at, user_id, friend_id)
VALUES(now(), now(), 4, 1);

INSERT INTO users(first_name, last_name, created_at, updated_at)
VALUES('Chris', 'Baker', now(), now());

INSERT INTO users(first_name, last_name, created_at, updated_at)
VALUES('Diana', 'Smith', now(), now());

INSERT INTO users(first_name, last_name, created_at, updated_at) 
VALUES('James', 'Johnson', now(), now());

INSERT INTO users(first_name, last_name, created_at, updated_at) 
VALUES('Jessica', 'Davidson', now(), now());
*/ 

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as user2 ON friendships.friend_id=user2.id
ORDER BY friend_last_name;