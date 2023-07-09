from PIL import Image
import json

datasets = []
with open("./meta/train/OTS_meta_train.json", "r") as f:
    print("Load meta file")
    datasets.append(json.load(f)) # jsonファイルに記述されたlistを追加

dataset = datasets[0]
target_path, input_path = dataset[0]

target_image = Image.open(target_path).convert('RGB')
input_image = Image.open(input_path).convert('RGB')
print(target_image.size)
print(len(dataset))
print(len(dataset[0]))
