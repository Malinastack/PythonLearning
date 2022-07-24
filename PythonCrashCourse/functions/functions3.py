def sandwich(*ingredients):
    print('You ordered this ingredients in your sandwich: ')
    for i in ingredients:
        print(f'- {i}')

sandwich('cheese', 'tomato', 'ham')
sandwich('cheese')
sandwich('cheese', 'tomato', 'ham', 'bacon')


def build_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


user_profile = build_profile('Szymon', 'Malinowski', location='Poland', age=22)

print(user_profile)

for k, v in user_profile.items():
    print(type(k))


def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)





