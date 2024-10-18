-- 코드를 작성해주세요
-- Skillcodes: name, category, code(2의 제곱수)
-- Developers: id, first_name, last_name, email, skill_code

-- 위 테이블에서 Python이나 C#의 코드를 조회하고
-- 아래 테이블에서 skill_code랑 & 연산

SELECT id, email, first_name, last_name
FROM Developers
WHERE skill_code & (SELECT code FROM Skillcodes WHERE name = "Python")
      OR skill_code & (SELECT code FROM Skillcodes WHERE name = "C#")
ORDER BY id;