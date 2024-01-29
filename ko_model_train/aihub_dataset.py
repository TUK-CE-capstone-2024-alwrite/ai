import json
import random
import os
from tqdm import tqdm
import re

# htr / ocr
data_type = 'htr'
# 파일명 패턴 설정
pattern = re.compile(r'책표지_사회과학_\d{6}\.json')

# 라벨링 파일들을 찾아 리스트에 저장
labeling_directory = './kor_dataset/aihub_data/htr/labels/'  # 라벨링 파일들이 있는 디렉토리 지정
labeling_filenames = [f for f in os.listdir(labeling_directory) if pattern.match(f)]

# 라벨링 파일들을 반복하여 처리
# 누적 결과를 저장할 변수 초기화
total_train_annotations = {}
total_validation_annotations = {}
total_test_annotations = {}

for labeling_filename in labeling_filenames:
    # Check Json File
    file = json.load(open(f'./kor_dataset/aihub_data/{data_type}/labels/{labeling_filename}', encoding="utf-8"))
    print(labeling_filename)
    # Separate dataset - train, validation, test
    image_files = os.listdir(f'./kor_dataset/aihub_data/{data_type}/images/') 
    total = len(image_files)

    random.shuffle(image_files)

    n_train = int(len(image_files) * 0.7)
    n_validation = int(len(image_files) * 0.15)
    n_test = int(len(image_files) * 0.15)

    train_files = image_files[:n_train]
    validation_files = image_files[n_train:n_train+n_validation]
    test_files = image_files[-n_test:]

    # Separate image id - train, validation, test
    train_img_ids = {}
    validation_img_ids = {}
    test_img_ids = {}

    for image in file['images']: # {filename}: {image id}
        if image['file_name'] in train_files:
            train_img_ids[image['file_name']] = image['id']
        elif image['file_name'] in validation_files:
            validation_img_ids[image['file_name']] = image['id']
        elif image['file_name'] in test_files:
            test_img_ids[image['file_name']] = image['id']
    
    # Annotations - train, validation, test 
    train_annotations = {f:[] for f in train_img_ids.keys()} # {image id}: []
    validation_annotations = {f:[] for f in validation_img_ids.keys()}
    test_annotations = {f:[] for f in test_img_ids.keys()}

    train_ids_img = {train_img_ids[id_]:id_ for id_ in train_img_ids}
    validation_ids_img = {validation_img_ids[id_]:id_ for id_ in validation_img_ids}
    test_ids_img = {test_img_ids[id_]:id_ for id_ in test_img_ids}

    for idx, annotation in enumerate(file['annotations']):
        if annotation['image_id'] in train_ids_img:
            train_annotations[train_ids_img[annotation['image_id']]].append(annotation)
        elif annotation['image_id'] in validation_ids_img:
            validation_annotations[validation_ids_img[annotation['image_id']]].append(annotation)
        elif annotation['image_id'] in test_ids_img:
            test_annotations[test_ids_img[annotation['image_id']]].append(annotation)
    
    # 결과를 누적
    total_train_annotations.update(train_annotations)
    total_validation_annotations.update(validation_annotations)
    total_test_annotations.update(test_annotations)

    # Write json files    
with open(f'{data_type}_train_annotation.json', 'w', encoding='utf-8') as file:
    json.dump(total_train_annotations, file)
with open(f'{data_type}_validation_annotation.json', 'w', encoding='utf-8') as file:
    json.dump(total_validation_annotations, file)
with open(f'{data_type}_test_annotation.json', 'w', encoding='utf-8') as file:
    json.dump(total_test_annotations, file)
        
data_root_path = f'./kor_dataset/aihub_data/{data_type}/images/'
save_root_path = f'./deep-text-recognition-benchmark/{data_type}_data/'

obj_list = ['test', 'train', 'validation']
for obj in obj_list:
    total_annotations = json.load(open(f'./{data_type}_{obj}_annotation.json', encoding='utf-8'))
    gt_file = open(f'{save_root_path}gt_{obj}.txt', 'w')
    for file_name in tqdm(total_annotations):
        annotations = total_annotations[file_name]
        for idx, annotation in enumerate(annotations):
            text = annotation['text']
            gt_file.write(f'{obj}/{file_name}\t{text}\n')