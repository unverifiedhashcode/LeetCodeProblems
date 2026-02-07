SELECT firstName, lastName, city, state 
    from Person
    left join Address on Address.personID = Person.personID 