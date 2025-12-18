-- Write your PostgreSQL query statement below
select today.id
    from weather today
    left join weather yesterday
        on today.recordDate = yesterday.recordDate + INTERVAL '1 day' --today = yesterday + 1
        where today.temperature > yesterday.temperature