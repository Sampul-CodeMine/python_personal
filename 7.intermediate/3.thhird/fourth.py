tenThings = 'Apple Oranges Crows Telephone Light Sugar'
print()
print('Wait! there isn\'t up to 10 (ten) objects in that list. Let us fix it.')

stuff = tenThings.split(' ')
print()
print(tenThings)
print('--------------------------------------------------------------')
print(stuff)
print('--------------------------------------------------------------')
moreStuff = ['Day', 'Night', 'Snow', 'Corn', 'Boy', 'Girl', 'Puppy', 'Man']
print(moreStuff)
print('---------------------------------------------------------------')
while len(stuff) != 10:
    next_one = moreStuff.pop()
    print('Adding: ', next_one)
    stuff.append(next_one)
    print('There is {} items now.'.format(len(stuff)))
print()
print('There we go: ', stuff)
print('Let us do some things with stuff.')
print('----------------------------------------------------------------')
print(moreStuff)
print('----------------------------------------------------------------')
print(stuff)
print('----------------------------------------------------------------')
print(stuff[1])
print(stuff[-1])  # whoa fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool
print('#'.join(stuff[3:5]))  # super stellar!
