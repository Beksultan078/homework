laptop = { "brand": "dell", "model": "alienware", "year": 2010 }

# 1. Print the brand value of the dictionary
print("Brand:", laptop["brand"])

# 2. Add new information (key: value) by using a boolean data type as value and home as key
#    This laptop is at home now, so "home": True
laptop["home"] = True
print("Updated laptop with 'home' information:", laptop)

# 3. Modify the value of the key year to 2019
laptop["year"] = 2019
print("Updated laptop with modified 'year' value:", laptop)
