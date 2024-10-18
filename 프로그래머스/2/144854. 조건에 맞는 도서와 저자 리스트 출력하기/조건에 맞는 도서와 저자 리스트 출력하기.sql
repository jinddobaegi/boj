-- 책: 책id, 카테고리, 저자id, 가격, 출판일
-- 저자: 저자id, 저자이름

-- 카테고리가 '경제'인 도서의
-- 책id, 저자명, 출판일

SELECT b.book_id, a.author_name,
    DATE_FORMAT(b.published_date, '%Y-%m-%d') AS published_date
FROM Book AS b INNER JOIN Author AS a
    ON b.author_id = a.author_id
WHERE b.category = '경제'
ORDER BY b.published_date ASC;