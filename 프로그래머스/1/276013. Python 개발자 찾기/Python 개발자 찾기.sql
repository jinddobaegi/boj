-- 코드를 작성해주세요

SELECT id, email, first_name, last_name
FROM Developer_infos
WHERE "Python" IN (skill_1, skill_2, skill_3)
ORDER BY id;