-- 

SELECT car_type, COUNT(car_type) AS cars
FROM Car_rental_company_car
WHERE options LIKE '%시트%'
GROUP BY car_type
ORDER BY car_type ASC;