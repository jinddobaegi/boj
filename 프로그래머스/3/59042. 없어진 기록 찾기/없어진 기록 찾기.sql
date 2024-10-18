-- in: id, 타입, 일자, 상태, 이름, 성별
-- out: id(FK), 타입, 일자, 이름, 성별
-- 데이터 일부 유실!
-- out 기록 있는데 in 기록 없는 동물 id랑 이름 조회

SELECT animal_id, name
FROM Animal_outs
WHERE animal_id NOT IN (SELECT i.animal_id
                        FROM Animal_outs AS o INNER JOIN Animal_ins AS i
                        ON o.animal_id = i.animal_id)
ORDER BY animal_id;