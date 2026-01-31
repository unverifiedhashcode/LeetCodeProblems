select
    query_name,
    round(avg(rating / position),2) as quality,
    Round(avg(case when rating < 3 then 1 else 0 end) * 100,2) as poor_query_percentage --note that this is not actually slower than performing the count of hits and then dividing by total size, both are O(n)
    from Queries
    group by query_name
