-- 코드를 입력하세요

-- 만원단위 가격대 별 상품 개수 출력
-- 가격대 오름차순 정렬

SELECT FLOOR(price/10000) * 10000 AS price_group, COUNT(*) AS products
FROM Product
GROUP BY FLOOR(price/10000) * 10000
ORDER BY price_group;