-- 코드를 작성해주세요

SELECT COUNT(*) AS fish_count, b.fish_name
FROM Fish_info AS a INNER JOIN Fish_name_info AS b
ON a.fish_type = b.fish_type
GROUP BY b.fish_name
ORDER BY fish_count DESC;

/*
SELECT에서 b.fish_name을 쓰려면
GROUP BY를 할 때 b.fish_name으로 묶어야 한다
*/