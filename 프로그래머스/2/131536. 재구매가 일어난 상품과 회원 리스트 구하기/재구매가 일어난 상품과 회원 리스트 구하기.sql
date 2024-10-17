-- 코드를 입력하세요
-- S F W G H O

SELECT user_id, product_id
FROM Online_sale
GROUP BY user_id, product_id
HAVING count(*) > 1
ORDER BY user_id, product_id DESC;