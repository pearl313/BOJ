-- 코드를 입력하세요
select
    o.animal_id ANIMAL_ID,
    o.name NAME
from ANIMAL_INS i right join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where i.animal_id is null





# SELECT O.ANIMAL_ID, O.NAME
# FROM ANIMAL_INS AS I
# RIGHT JOIN ANIMAL_OUTS AS O
# ON I.ANIMAL_ID = O.ANIMAL_ID
# WHERE I.ANIMAL_ID IS NULL