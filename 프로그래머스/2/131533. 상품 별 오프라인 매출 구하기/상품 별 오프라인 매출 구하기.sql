-- 상품 테이블: 상품id, 코드, 판매가
-- 판매 테이블: 핀메id, 상품id, 판매량, 판매일

-- 상품코드 별 => 그룹
-- 매출액 => 집계함수

SELECT p.product_code, SUM(p.price * s.sales_amount) AS sales
FROM Offline_sale AS s LEFT JOIN Product AS p
    ON s.product_id = p.product_id
GROUP BY p.product_code
ORDER BY sales DESC, p.product_code ASC;