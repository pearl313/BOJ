-- 코드를 입력하세요
SELECT
    f.flavor FLAVOR
    # sum(f.total_order)
from first_half f join july j
on f.flavor = j.flavor
group by f.flavor
order by sum(f.total_order) + sum(j.total_order) desc
limit 3