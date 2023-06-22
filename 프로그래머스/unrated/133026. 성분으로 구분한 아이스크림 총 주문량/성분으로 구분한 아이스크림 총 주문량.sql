-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from first_half as f
join icecream_info as i
on f.flavor = i.flavor
group by ingredient_type
order by total_order 