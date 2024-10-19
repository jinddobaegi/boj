-- 도서정보: 책id, 카테고리, 저자id, 판매가, 출판일
-- 판매정보: 책id, 판매일, 판매량

-- 2022년 1월 "카테고리" 별 도서 판매량 합

SELECT b.category, SUM(s.sales) AS total_sales
FROM Book_sales AS s INNER JOIN Book AS b
    ON s.book_id = b.book_id
WHERE s.sales_date LIKE '2022-01%'
GROUP BY b.category
ORDER BY category;