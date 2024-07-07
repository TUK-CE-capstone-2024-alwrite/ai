# 📺 노트 필기 어플리케이션 Alwrite

## 프로젝트 소개

- 다양한 필기 기능을 가지고 있는 노트 어플리케이션으로
- 기존 노트 어플리케이션에서 OCR를 활용한 텍스트 변환 기능과 녹음 요약 기능을 추가한 다용도 플랫폼입니다.
- 해당 레포지토리는 백엔드(AI)에 해당하는 레포지토리입니다.


## 팀원 구성

<div>

| **오하민** | **김민지** |
| :------: | :------: |
| [<img width="140px" src="https://avatars.githubusercontent.com/u/113972482?v=4" height=150 width=150> <br/> @ohamin26](https://github.com/ohamin26) | [<img width="140px" src="https://avatars.githubusercontent.com/u/102501739?v=4" height=150 width=150> <br/> @min9-525](https://github.com/min9-525) |

</div>


## 1. 개발 환경

- Language && Framework : python, pytorch, tensorflow, GCP
- 버전 및 이슈관리 : Github, Github Issues
- 서비스 배포 환경 : GCP
  <br>

## 2. 채택한 개발 기술과 브랜치 전략

### python, pytorch, tensorflow

- 기능 개발 중 OCR 기능을 추가 할 필요가 있었고, 모델을 생성하기 위해 딥러닝 라이브러리인 pytorch와 tensorflow를 사용해 개발하였습니다.

### GCP

- 딥러닝 모델을 학습시키기 위해 GPU가 필요하였습니다. 또한 팀원 간 원활한 코드와 데이터 셋 공유를 할 필요가 있었습니다.
- 모델을 학습 시킬 수 있는 공유 플랫폼인 colab, GCP, aws 중 비용적으로 가장 합리적인 GCP를 선택하였습니다.
  
### 브랜치 전략

- Git-flow를 채택하였으며, main, dev, feat로 구분하여 진행하였습니다.
  - **main** 배포용으로 최종적으로 적용할 기능만을 합쳤습니다.
  - **dev** 모든 기능을 합치고 개발과 테스트 단계에 사용하는 브랜치 입니다.
  - **Feat** 개발을 효율적으로 진행하기 위해 기능 단위로 브랜치을 생성하여 dev 브랜치에 합치는 방식으로 진행하였습니다.



## 3. 프로젝트 구조

```
├── README.md
├── .gitignore
├── english_handwriting_recognition
│    ├── data
│    └── src
└── ko_model_train
     ├── deep-text-recognition-benchmark
     ├── aihub_dataset.py
     ├── finetuning_dataset.py
     └── trans_json.py
```



## 4. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2023.12.20 ~ 2024.02.15



### 작업 관리

- Gihub와 google_drive 통해 관리하였습니다.

