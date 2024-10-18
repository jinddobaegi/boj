-- 코드를 작성해주세요
-- Ecoli_data: id, parent_id, size_of_colony, differentiation_date, genotypoe

SELECT a.id, a.genotype, b.genotype AS parent_genotype
FROM Ecoli_data AS a, Ecoli_data AS b
WHERE a.parent_id = b.id AND a.genotype & b.genotype = b.genotype
ORDER BY id;