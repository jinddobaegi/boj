-- 코드를 작성해주세요
-- 1) Fish_info: id, fish_type, length, time
-- 2) Fish_name_info: fish_type, fish_name

-- 1에서 타입으로 2에서 이름 가져와야 함

SELECT COUNT(*) AS fish_count
FROM Fish_info AS a, Fish_name_info AS b
WHERE a.fish_type = b.fish_type AND b.fish_name IN ("BASS", "SNAPPER");