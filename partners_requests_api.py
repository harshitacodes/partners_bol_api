# import requests
# import pprint
# import json

# # api of the bol partners
# url = "http://join.navgurukul.org/api/partners"



# #  this function will get the data throungh giving the request to api
# def get_data(link):
#     res = requests.get(link)
#     return res.text
# data = get_data(url)



# # by json.loads we'll get the data in dictionary
# dic_data = json.loads(data)
# data_ = dic_data['data']



# # this will give the names from the data
# def name_data(data_nam):
#     name_list = []
#     for i in data_nam:
#         names = i['name']
#         name_list.append(names)
#     return name_list
# names_of_dic = name_data(data_)



# # this function will gives the sorted data can be assending or descending according to the user choice
# def accending_sorted_data(id_data):
#     if users_choice == "a":
#         for j in range(0,len(id_data)):
#             for i in range(0,len(id_data)-1):
#                 if id_data[i]['id']>id_data[i+1]['id']:
#                     id_data[i], id_data[i+1] = id_data[i+1], id_data[i]
        
#         return id_data
#     elif users_choice == "d":
#         for j in range(0,len(id_data)):
#             for i in range(0,len(id_data)-1):
#                 if id_data[i]['id']<id_data[i+1]['id']:
#                     id_data[i], id_data[i+1] = id_data[i+1], id_data[i]
#         return id_data
# users_choice = input("enter the choice ---for ascending enter a, and for descending enter d........:")
# pprint.pprint(accending_sorted_data(data_))

import requests
import json

city_name = input("enter the name of city: ")
try:
    weatherapi_url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(city_name) + "&appid=05964be4af2fc2a2b7525c680828da7c&units=metric"
    res = requests.get(weatherapi_url)
    r_text = res.text
    weather_data = json.loads(r_text)
    dict_data = weather_data["main"]["temp"]
    print(dict_data)
except KeyError:
    print("incorrect city name")

except Exception as e:
    print("error",e)