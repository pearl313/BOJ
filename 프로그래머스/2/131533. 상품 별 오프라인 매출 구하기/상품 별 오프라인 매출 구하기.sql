-- 코드를 입력하세요
select
    p.PRODUCT_CODE PRODUCT_CODE,
    sum(o.sales_amount) * p.price SALES
from product p join offline_sale o
on p.product_id = o.product_id
group by p.product_id
order by SALES DESC, p.PRODUCT_CODE




# SELECT P.PRODUCT_CODE, SUM(O.SALES_AMOUNT) * P.PRICE AS SALES
# FROM PRODUCT AS P
# JOIN OFFLINE_SALE AS O
# ON P.PRODUCT_ID = O.PRODUCT_ID
# GROUP BY P.PRODUCT_ID
# ORDER BY SALES DESC, P.PRODUCT_CODE