guests = {}
def read_guestlist(file_name):
  '''1a This feature has been modified to be a generator function that yield each read line so that each guest name is yielded each time for the generator.'''
  text_file = open(file_name,'r')
  line_data = text_file.readline().strip().split(",")
  while len(line_data) > 1:
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield (name, age)
    line_data = text_file.readline().strip().split(",")
  text_file.close()
        
def add_new_guest(file_name):
  ''' This function adding a new guest to the guestlist '''
  add_guest = yield
  if add_guest is not None:
    with open(file_name, 'a') as file:
      file.write(f'\n{add_guest}')

#5 Added 3 separate generator functions, one for each table, that yield tuples of ("Food Name", "Table X", "Seat Y") for each of the 5 seats at each table.
def table_one():
  for number in range(1, 6):
    table = (f'Chicken', f'Table 1', f'Seat {str(number)}')
    yield table

def table_two():
  for number in range(1, 6):
    table = (f'Beef', f'Table 2', f'Seat {str(number)}')
    yield table

def table_three():
  for number in range(1, 6):
    table = (f'Fish', f'Table 3', f'Seat {str(number)}')
    yield table

#1b Iterate through the generator object that is retrieved by calling the generator function read_guestlist() and print out the first 10 guests on the guestlist
print('Print out first 10 guests:')
guest_generator = read_guestlist("guest_list.txt")
guest_count = 1
while guest_count <= 10:
  print(next(guest_generator))
  guest_count += 1

#2 Calling function add_new_guest and adding new guest to the guestlist
add_new_guest_name = add_new_guest("guest_list.txt")
next(add_new_guest_name)
# when first time run this project, we must commented code line 50, because is
# stop execute program
#add_new_guest_name.send('Jane,35') 

#3  Yielding automatically the rest of the names from the guestlist
print('Print rest of the names from the guestlist:')
try:
  while guest_count <= 15:
    print(next(guest_generator))
    guest_count += 1
except StopIteration:
  pass

#4 In variable guest_over_21 is a generator expression that use the guests dictionary to retrieve a generator of names of all guests who are aged 21 and over.
guest_over_21 = (f'{guest} ({guests[guest]})' for guest in guests if guests[guest] >= 21)
print('List of names of all guests who are aged 21 and over:')
for guest in guest_over_21:
  print(guest)

#5 Add all_tables_generator to connected all three generator functions for table 1, table 2 and table 3 with different meals
def all_tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

all_tables_generator = all_tables()

#6 Assign a table and seat number with meal selection to each guest in seating_generator
def seating_order():
  for name in guests:
    yield (name, next(all_tables_generator))

print('Meal seating:')
seating_generator = seating_order() 
for seat in seating_generator:
  print(seat)

