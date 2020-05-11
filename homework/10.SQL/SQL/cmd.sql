SELECT name, age, cls_id FROM students WHERE gender='男';
SELECT * FROM students WHERE id<4 OR is_delete<>0;
SELECT * FROM students WHERE name LIKE '黄_';
SELECT * FROM students WHERE id=1 OR id=3 OR id=8;
SELECT * FROM students WHERE id BETWEEN 3 AND 8;
SELECT * FROM students WHERE gender='男' AND is_delete=0 ORDER BY age DESC;
SELECT COUNT(*) AS total FROM students WHERE gender='女';
SELECT AVG(age) AS aver_age FROM students;
SELECT * FROM
(SELECT gender AS gender, AVG(age) AS avg_age FROM students GROUP BY gender) AS total
WHERE gender='男' OR gender='女';
SELECT gender, GROUP_CONCAT(name) FROM students GROUP BY gender;