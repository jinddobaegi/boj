-- in: id, 타입, 일자, 상태, 이름, 성별
-- out: id(FK), 타입, 일자, 이름, 성별

-- in날짜보다 빠른 out날짜 가진
-- 동물의 id, 이름 조회

SELECT i.animal_id, i.name
FROM Animal_ins AS i LEFT JOIN Animal_outs AS o
    ON i.animal_id = o.animal_id
WHERE i.datetime > o.datetime
ORDER BY i.datetime;