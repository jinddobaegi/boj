-- 입양 못 간 동물 중, 가장 오래 있었던 동물 3마리
-- 이름, 보호 시작일 조회

-- in은 있는데, out이 없는

SELECT i.name, i.datetime
FROM Animal_ins AS i LEFT JOIN Animal_outs AS o
    ON i.animal_id = o.animal_id
WHERE o.datetime IS NULL
ORDER BY i.datetime ASC
LIMIT 3;