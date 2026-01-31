with expiredManagers as (
    select 
            manager_id 
        from Employees
            where manager_id is not null
        except 
            (select employee_id from employees)
)
select employee_id 
    from Employees
    where
    manager_id in (select manager_id from expiredManagers)
        and salary < 30000
    order by employee_id asc