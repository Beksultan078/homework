user_tp= ("name" , "age" , "country" , "user_info" )
dict_user=dict.fromkeys(user_tp)
dict_user["name"] = input("what is the user's name? ")
dict_user["age"] = int(input("what is the user's age?"))
dict_user["country"] = input("what is the user's country of birth? ")
dict_user["user_info"] = input("what is the user known for? ")
for key , value in dict_user.items():
    print(f"{key} :{value}")
