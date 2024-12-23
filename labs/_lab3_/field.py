def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            key = args[0]
            value = item.get(key)
            if value is not None:
                yield value
        else:
            result = {key: item.get(key) for key in args}
            result = {key: value for key, value in result.items() if value is not None}
            if result:
                yield result

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стол', 'price': None, 'color': 'brown'},
    {'title': None, 'price': 1500, 'color': 'white'}
]

print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))
