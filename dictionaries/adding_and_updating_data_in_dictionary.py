# update/add values with dict[key]
movie = {
    "title": "Rogueie",
    "reviews": 10347,
    "imdb": 8.5,
    "runtime": '3h',
    "year": 2011,
    "rating": "R"
}

# to update, we just index the key and set it equal(=) to the updated value
movie['runtime'] = '4h'

movie['imdb'] += 0.5

print(movie['runtime'])  # 4h

print(movie["imdb"])  # 9.0

# to add, we just add new element by adding new keys and set it equal(=) to its corresponding values 

order = {"quantity": 5, "price": 5.99}

order['shipping'] = 6.50

print(order)  # {'quantity': 5, 'price': 5.99, 'shipping': 6.5}
