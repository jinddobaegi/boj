-- 고양이, 개 마리 수
-- 고양이를 우선

SELECT animal_type, COUNT(animal_type) AS count
FROM Animal_ins
GROUP BY animal_type
HAVING animal_type in ('Cat', 'Dog')
ORDER BY animal_type;