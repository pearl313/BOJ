-- 코드를 입력하세요
select
    b.book_id BOOK_ID,
    a.author_name AUTHOR_NAME, 
    date_format(b.PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
from book b join author a
on b.author_id = a.author_id
where b.category = '경제'
order by PUBLISHED_DATE

# SELECT 
# b.BOOK_ID AS BOOK_ID,
# a.AUTHOR_NAME AS AUTHOR_NAME,
# date_format(b.PUBLISHED_DATE, 'yyyy-mm-dd') AS PUBLISHED_DATE
# FROM BOOK b
# JOIN AUTHOR a
# ON b.AUTHOR_ID = a.AUTHOR_ID
# WHERE b.CATEGORY = '경제'
# ORDER BY PUBLISHED_DATE