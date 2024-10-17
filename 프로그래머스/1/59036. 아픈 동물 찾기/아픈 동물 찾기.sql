-- 코드를 입력하세요
SELECT animal_id, name
FROM Animal_ins
WHERE intake_condition LIKE "%Sick%"
ORDER BY animal_id;