import json
import os

# 합칠 JSON 파일들이 있는 디렉토리 경로
directory_path = r"C:\Users\user\project\senior_project\test2\json"

# 결과를 저장할 파일 경로
output_file_path = r'C:\Users\user\project\senior_project\test2\result\result.json'

# 모든 JSON 파일을 저장할 빈 리스트
all_data = []

# 디렉토리 내의 모든 파일에 대해 반복
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)
        
        # JSON 파일을 읽어서 딕셔너리로 로드
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # 키만을 추가
            all_data.append(data)

# 결과를 하나의 파일로 저장
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(all_data, output_file, ensure_ascii=False, indent=2)

print(f'Successfully merged {len(all_data)} JSON files into {output_file_path}')
