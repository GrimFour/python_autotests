# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

#1
new_record = ('Maks', 'Skam', 44, 'Builder', 'Kenugard')
people_records.append(new_record)

#2
index_one = people_records[1]
index_five = people_records[5]

people_records[1] = index_five
people_records[5] = index_one
print(people_records)

#3

# def is_age_above_30_no_index(data):
#   for i in range(len(data)):
#     if data[i][2] >= 30:
#        print(f'\n Person #{i} is older than 30. OK')
#     else:
#        print(f'\n Person #{i} is more than 30. NOT OK')
#
# is_age_above_30_no_index(people_records)

index_to_check = [6, 10, 13]
age_index = 2

def is_age_above_30(data, indexes, age_idx):
  for i in indexes:
    if data[i][age_idx] <= 30:
       print(f'\n Person #{i} is less than 30. NOT OK')
    else: print(f'\nPerson #{i} is more than 30. OK')

is_age_above_30(people_records, index_to_check, age_index)