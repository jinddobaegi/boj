-- 코드를 입력하세요
-- food_type 별, favorite이 가장 많은 식당

SELECT food_type, rest_id, rest_name, favorites
FROM Rest_info
WHERE (food_type, favorites) IN (SELECT food_type, MAX(favorites)
                                FROM Rest_info
                                GROUP BY food_type)
ORDER BY food_type DESC;