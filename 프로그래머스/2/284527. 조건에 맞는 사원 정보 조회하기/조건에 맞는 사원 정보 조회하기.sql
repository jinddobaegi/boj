-- 코드를 작성해주세요
-- 1) 부서 정보 => 필요 x
-- 2) 사원 정보
-- 3) 사원 평가 정보


-- 22년도 평가 점수 가장 높은 사원들
-- 점수(상+하), 사번, 성명, 직책, 이메일

SELECT SUM(g.score) AS score, g.emp_no,
e.emp_name, e.position, e.email
FROM Hr_grade AS g INNER JOIN Hr_employees AS e
ON g.emp_no = e.emp_no
GROUP BY g.emp_no, g.year
HAVING g.year = '2022'
ORDER BY score DESC
LIMIT 1;