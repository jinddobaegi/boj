-- 코드를 작성해주세요

SELECT route,
    CONCAT(ROUND(SUM(d_between_dist), 1), 'km') AS total_distance,
    CONCAT(ROUND(AVG(d_between_dist), 2), 'km') AS average_distance
FROM Subway_distance
GROUP BY route
ORDER BY SUM(d_between_dist) DESC;

/*
이 경우엔 SELECT에서 d_between_dist 컬럼에 대해
집계 함수를 사용했기 때문에
GROUP BY의 route 컬럼에 대해 집계가 가능하다
*/