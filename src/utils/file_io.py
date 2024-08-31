import json

def load_data(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)
    
def load_korean_data(json_path):
    with open(json_path, "r", encoding='utf-8') as f:
        return json.load(f)

def write_korean_data(json_path, data):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def rePath(data_list, path_from,path_to):
    if isinstance(data_list, list) is False:
        data_list = [data_list['image'].replace(path_from, path_to)]
 
    for item in data_list:
            item['image'] = item['image'].replace(path_from, path_to)
    return data_list