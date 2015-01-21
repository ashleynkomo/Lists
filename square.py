def squared_numbers():
    numbers = [x**2 for x in range(51)]
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(numbers)))

#main program
squared_numbers()


