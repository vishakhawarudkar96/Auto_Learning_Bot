import json
dish = input("Please Enter Dish Name :")
dish = dish.title()
def write_json(data, filename="test_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=5)
with open("test_data.json") as json_file:
    data = json.load(json_file)
    indian = data["indian"]
    chinese = data["chinese"]
    italian = data["italian"]
    if dish in indian:
        print(dish,"is a Indian Dish")
    elif dish in chinese:
        print(dish,"is a Chinese Dish")
    elif dish in italian:
        print(dish,"is a Italian Dish")
    else:
        print(dish,"is a not Found in our record\n")
        que = input("Can you please suggest it (Yes/No):")
        que = que.title()
        if que == 'Yes':
            print("please Select Appropriate Country from Below List:")
            print("1. Indian \n2. Chinese \n3. Italian")
            country=input("Please Enter your choice (* Numbers Only)")
            if country == '1':
                indian.append(dish)
                print("Thank for your time! We Appreciate your Knowledge!")
                print(indian)
            elif country == '2':
                chinese.append(dish)
                print("Thank for your time! We Appreciate your Knowledge!")
                print(chinese)
            elif country == '3':
                italian.append(dish)
                print("\nThank for your time! We Appreciate your Knowledge!")
                print(italian)
            else:
                print("This is Not Valid Choice")
        elif que == 'No':
            print("Thanks for your time!, Have a Great Day Ahead!")
        else:
            print("Please Select Appropriate Option")
write_json(data)
