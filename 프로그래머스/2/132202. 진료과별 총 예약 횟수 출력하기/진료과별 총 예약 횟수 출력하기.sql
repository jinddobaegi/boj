-- 진료과코드 별 예약 환자 수

SELECT mcdp_cd AS '진료과코드', COUNT(mcdp_cd) AS '5월예약건수'
FROM Appointment
WHERE apnt_ymd LIKE '2022-05%'
GROUP BY mcdp_cd
ORDER BY `5월예약건수` ASC, `진료과코드` ASC;