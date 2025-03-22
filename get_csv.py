import requests
import pandas as pd
import os
import json 
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('FLIC_TOKEN')
header = {'Flic-token': f'{token}'}

data_viewed = requests.get('https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if')
data_liked = requests.get('https://api.socialverseapp.com/posts/like?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if')
data_inspired = requests.get('https://api.socialverseapp.com/posts/inspire?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if')
data_rated = requests.get('https://api.socialverseapp.com/posts/rating?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if')
data_all_posts = requests.get('https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000', headers=header) 
data_all_users = requests.get('https://api.socialverseapp.com/users/get_all?page=1&page_size=1000', headers=header)

# print(len(data_all_posts.json()["posts"])) # 1000
# print(len(data_all_users.json()["posts"])) # 1019
names = ["data_viewed", "data_liked", "data_inspired", "data_rated"]
datas = [data_viewed, data_liked, data_inspired, data_rated]

def make_csv(data, name):
    data = data.json()["posts"]
    df = pd.DataFrame(data)
    df.to_csv(name,index=False)

for i in range(len(names)):
    make_csv(datas[i], names[i])

def save_json(filename, my_dict):
    with open(filename, 'w') as file:
        json.dump(my_dict, file, indent=4)

save_json("data_all_posts.json", data_all_posts.json())
save_json("data_all_users.json", data_all_users.json())





