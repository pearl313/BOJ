-- 코드를 입력하세요
select
    i.name NAME,
    i.datetime DATETIME
from animal_ins i left join animal_outs o
on i.animal_id = o.animal_id
where o.animal_id is null
order by i.datetime
limit 3



















# SELECT I.NAME, I.DATETIME
# FROM ANIMAL_INS AS I
# LEFT JOIN ANIMAL_OUTS AS O
# ON I.ANIMAL_ID = O.ANIMAL_ID
# WHERE O.ANIMAL_ID IS NULL
# ORDER BY I.DATETIME
# LIMIT 3