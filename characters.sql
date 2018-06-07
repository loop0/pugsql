-- A ":result" value of ":*" specifies a vector of records
-- (as hashmaps) will be returned
-- :name all-characters :? :*
-- :doc Get all characters
select * from characters
order by id;

-- A ":result" value of ":1" specifies a single record
-- (as a hashmap) will be returned
-- :name character-by-id :? :1
-- :doc Get character by id
select * from characters
where id = :id;

-- :name character-by-name :? :1
-- :doc Get character by case-insensitive name
select * from characters
where upper(name) = upper(:name);

-- A ":result" value of ":n" below will return affected row count
-- :name insert-character :! :n
-- :doc Insert a single character
insert into characters (name, specialty)
values (:name, :specialty);
