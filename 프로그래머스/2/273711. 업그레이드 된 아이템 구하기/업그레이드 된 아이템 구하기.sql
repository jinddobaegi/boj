-- 코드를 작성해주세요
-- S F W G H O

SELECT item_id, item_name, rarity
FROM item_info
WHERE item_id in (SELECT t.item_id
                  FROM Item_info i, Item_tree t
                  WHERE i.item_id = t.parent_item_id AND i.rarity = "RARE"
                 )
ORDER BY item_id DESC;