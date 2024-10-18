-- a) 상반기: 출하번호, 맛(PK), 총주문량
-- b) 아스정보: 맛(FK), 성분타입

SELECT b.ingredient_type AS ingredient_type,
    SUM(a.total_order) AS total_order
FROM First_half AS a INNER JOIN Icecream_info AS b
    ON a.flavor = b.flavor
GROUP BY b.ingredient_type
ORDER BY total_order;

