-- 코드를 입력하세요
select
    i.animal_id ANIMAL_ID,
    i.name NAME
from animal_ins i join animal_outs o
on i.animal_id = o.animal_id
where i.datetime > o.datetime
order by i.datetime




















# SELECT I.ANIMAL_ID, I.NAME
# FROM ANIMAL_INS AS I
# JOIN ANIMAL_OUTS AS O
# ON I.ANIMAL_ID = O.ANIMAL_ID
# WHERE I.DATETIME > O.DATETIME
# ORDER BY I.DATETIME