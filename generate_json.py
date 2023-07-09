import json
import os

def create_json_file():
    json_data = []
    for i in range(58):  # ファイルの数に応じて変更
        json_data.append([f"./data/test/rain_drop_test/gt/{i}_rain.png", f"./data/test/rain_drop_test/input/{i}_rain.png"])

    with open('output.json', 'w') as file:
        json.dump(json_data, file)

# Snow100K
def create_json_snow100k():
    json_data = []
    base_path = "./data/test"
    train_list = "./data/test/snowtest100k_L.txt"
    with open(train_list) as f:
        contents = f.readlines()
        input_names = [os.path.join(base_path, i.strip()) for i in contents]
        gt_names = [i.strip().replace('input','gt') for i in input_names]
        # json_data.append([input_names, gt_names])

    for gt, input in zip(gt_names, input_names):
        json_data.append([gt, input])

    with open('output.json', 'w') as file:
        json.dump(json_data, file)

# rainfog test1
def create_json_Rainfog():
    json_data = []
    base_path = "./data/test"
    train_list = "./data/test/test1.txt"
    with open(train_list) as f:
        contents = f.readlines()
        input_names = [os.path.join(base_path, i.strip()) for i in contents]
        gt_names = [i.strip().replace('input','gt') for i in input_names]
        gt_names = [i.rsplit('_', 2)[0] + '.' + i.rsplit('.', 1)[-1] for i in gt_names]

    for gt, input in zip(gt_names, input_names):
        json_data.append([gt, input])

    with open('Rainfog_meta_valid.json', 'w') as file:
        json.dump(json_data, file)

# Rain1400 Test
# input: 999_9.jpg, gt: 999.jpg
def create_json_Rain1400_valid():
    json_data = []
    for i in range(901, 1001):
        for j in range(1, 15):
            json_data.append([f"./data/test/Rain1400/gt/{i}.jpg", f"./data/test/Rain1400/input/{i}_{j}.jpg"])

    with open('Rain1400_meta_valid.json', 'w') as file:
        json.dump(json_data, file)

# OTS train
# # input: 0025_0.95_0.2.jpg, gt: 0025.jpg
def create_json_OTS():
    json_data = []
    input_path = "./data/train/OTS/input/part1"
    gt_path = "./data/train/OTS/gt"
    train_list = "./data/train/OTS_part1.txt"
    with open(train_list) as f:
        contents = f.readlines()
        input_names = [i.strip() for i in contents]
        gt_names = [i.split('_', 1)[0] + '.jpg' for i in input_names]

        input_names = [os.path.join(input_path, i) for i in input_names]
        gt_names = [os.path.join(gt_path, i) for i in gt_names]

    for gt, input in zip(gt_names, input_names):
        json_data.append([gt, input])

    json_data = json_data[:5000]

    with open('OTS_meta_train.json', 'w') as file:
        json.dump(json_data, file)


# 関数を呼び出してJSONファイルを作成
if __name__ == '__main__':
    create_json_OTS()
