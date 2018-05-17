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

-- :name characters-by-name-like :?
-- :doc Get characters by name like, :name-like should include % wildcards
select * from characters
where name like :name-like;

-- Let's specify some columns with the
-- identifier list parameter type :i* and
-- use a value list parameter type :v* for SQL IN()
-- :name characters-by-ids-specify-cols :? :*
-- :doc Characters with returned columns specified
select :i*:cols from characters
where id in (:v*:ids);