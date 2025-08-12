# # # SETS # # #

#  1. Create a Set

fruits = {"coconut", "papaya", "watermelon", "pineapple", "mango"}
print("Step 1.0: Fruits in set: ", fruits)


# 2. Check Membership

if "watermelon" in fruits:
    print("Step 2.0: Watermelon is in 'fruits'")


# 3. Add and Update Items

fruits.add("pomegranate")
print("Step 3.1: Added 'pomegranate' to 'fruit'set: ", fruits)

more_fruits = {"tomato", "kiwi", "lemon"}
print("Step 3.2: Created a new set: ", more_fruits)

fruits.update(more_fruits)
print("Step 3.3: Combined set of fruits: ", fruits)


# 4. Remove Items

fruits.remove("pomegranate")
print("Step 4.1: Removed 'pomegranate': ", fruits)

fruits.discard("cherry")
print("Step 4.2: After attempt to remove 'cherry':", fruits)

print("Step 4.3: A random fruit removed: ", fruits.pop(), fruits)

fruits_copy = fruits.copy()
fruits_copy.clear()
print("Step 4.4: Empty set: ", fruits_copy)


# 5. Set Operations 

set_a = {"apple", "mango", "cherry"}
set_b = {"avocado", "banana", "lime"}
set_ab_union = set_a.union(set_b)

print("Step 5.1: Combined sets: ", set_ab_union)

set_ab_intersection = set_a.intersection(set_b)
print("Step 5.2: Common elements in both sets: ", set_ab_intersection)

set_ab_difference = set_a.difference(set_b)

print("Step 5.3: Difference in sets: ", set_ab_difference)

set_ab_symmetric_difference = set_a.symmetric_difference(set_b)

print("Step 5.4: Symmetric Difference in sets: ", set_ab_symmetric_difference)


# 6. In-place Set Operations

set_c = {"blueberry","strawberry", "raspberry"}
set_d = {"blueberry","peach", "raspberry"}

set_c.difference_update(set_d)
print("Step 6.1: A fruit only in set_c: ", set_c)

set_c = {"blueberry","strawberry", "raspberry"}
set_d = {"blueberry","peach", "raspberry"}

set_c.intersection_update(set_d)
print("Step 6.2: A fruits in both sets: ", set_c)

set_c.update(set_d)
print("Step 6.3: Added fruits from set_d to set_c: ", set_c)


# 7. Relational Methods

small_set = {1,2,3,4}
large_set = {1,2,3,4,5}
print("Step 7.1: small is subset to large: ", small_set.issubset(large_set))
print("Step 7.2: small is < subset to large: ", small_set<large_set)

print("Step 7.3: large is superset to small: ", large_set.issuperset(small_set))
print("Step 7.4: large is > superset to small: ", large_set>small_set)

print("Step 7.5: small is disjoint to large: ", small_set.isdisjoint(large_set))



# # # DICTIONARIES # # #

# 1. Create and Print a Dictionary

person = {"name": "Max",
          "age": 30,
          "city": "Musterstadt"
          }
print("Step 1.0: Entire person dictionary: ", person)


# 2. Access Dictionary Elements

print("Step 2.1: Printing the value of 'name':", person["name"])

print("Step 2.2: Printing 'email' using 'get': ", person.get("email"))

print("Step 2.3: Printing: ", person.keys())
print("Step 2.4: Printing: ", person.values())
print("Step 2.5: Printing: ", person.items())


# 3. Check for Key Existence

if "age" in person:
    print("Step 3.1: Age is included in 'person'")
else: print("Step 3.1: Age is not included in 'person'")

# alternative way:
print("Step 3.1: Is age included?", "age" in person)


# 4. Change and Update Dictionary Elements

person["city"] = "SinCity"
print("Step 4.1: updated city: ", person["city"]) 

person.update({"name": "Jack", "age": 35, "height": 1.9})

print("Step 4.2: updated person: ", person)


# 5. Add New Items to the Dictionary

person["country"] = "USA"
print("Step 5.1: updated person: ", person)


person.update({"eyes": "blue"})
print("Step 5.2: updated person: ", person)


# 6. Remove Items from the Dictionary

print("Step 6.1: value of removed item : ", person.pop("height"))

print("Step 6.2: removed last inserted key-value pair: ", person.popitem())

del person["age"]
print("Step 6.3: removed the 'age key-pair':", person)

### commented out for Step 7:
# person.clear()                                
# print("Step 6.4: person cleared:", person)

# 7. Copy a Dictionary

shallow_copy = person.copy()
print("Step 7.1: A shallow copy via .copy(): ", shallow_copy)

shallow_copy2 = dict(person)
print("Step 7.2: A shallow copy via dict(): ", shallow_copy2)

person["age"] = 35
print("Step 7.3: Modified original dictionary: ", person)
print("Step 7.3: Unchanged shallow copy: ", shallow_copy)
print("Step 7.3: Unchanged shallow copy 2: ", shallow_copy2)

# 8. Using setdefault()

weight = person.setdefault("weight", 90)
age = person.setdefault("age", 70)
gender = person.setdefault("gender", "male")
print("Step 8.0: Modified person data via .setdefault(): ", person)