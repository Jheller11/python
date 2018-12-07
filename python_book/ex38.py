ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not ten things...")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Girl',
              'Boy', 'Frisbee', 'Banana', 'Corn']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} now.")

print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
