-- 시간대 별 입양 건수
-- 09 ~ 19시


SELECT HOUR(datetime) AS hour, COUNT(*) AS count
FROM Animal_outs
GROUP BY HOUR(datetime)
HAVING hour BETWEEN 9 AND 19
ORDER BY hour;