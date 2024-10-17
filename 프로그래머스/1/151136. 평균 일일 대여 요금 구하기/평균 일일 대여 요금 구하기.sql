-- 코드를 입력하세요
-- SFWGHO

SELECT round(avg(daily_fee), 0) AS "average_fee"
FROM Car_rental_company_car
WHERE car_type = "SUV";