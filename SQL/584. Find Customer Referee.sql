-- Write your PostgreSQL query statement below
select name from Customer 
    where referee_id is null or 
    (referee_id is not null and referee_id != 2)