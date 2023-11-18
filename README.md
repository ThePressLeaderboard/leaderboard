# leaderboard

## 프로젝트 주제: 언론사 영향력
![logo2](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/45270fd6-b0e2-44a4-a9ab-a49441596ff7)
## 프로젝트 개요
### 내용
언론사 영향력 프로젝트는 2024년 총선을 앞두고, 연령 및 성별을 기준으로 어느 신문사가 가장 영향력이 있는지를 가늠할 수 있도록 하는 프로젝트입니다.
### 기간

- 2023년 11월 6일부터 2023년 11월 10일까지

### 팀원

| 이름   | 역할               |
| ------ | ------------------ |
| 박지호 | 프로젝트 관리, CI/CD, 프론트엔드 |
| 이상혁 | 백엔드 (API)       |
| 이상평 | 백엔드 (API)       |
| 권우상 | 백엔드 (API)       |
| 임동빈 | 크롤링, 데이터베이스 디자인 |

### 기술 스택

- Back-end: Python, Django
- DB: SQLite
- Crawler: Selenium, BeautifulSoup, Requests
- Front-end: Vue.js
- 협업 도구: Slack, GitHub

## 설치 및 실행 방법

### 백엔드

1. `git clone https://github.com/ThePressLeaderboard/leaderboard.git` 명령어로 프로젝트를 복제합니다.
2. `cd app`로 프로젝트 폴더로 이동합니다.
3. 가상 환경을 생성합니다:
   - macOS/Linux: `python -m venv env` 
   - Windows: `python -m venv env`
4. 가상 환경을 활성화합니다:
   - macOS/Linux: `source env/bin/activate`
   - Windows: `.\env\Scripts\activate.bat`
5. 필요한 패키지를 설치합니다: `pip install -r requirements.txt`

### 프론트엔드

1. `git clone https://github.com/ThePressLeaderboard/front.git` 명령어로 프로젝트를 복제합니다.
2. 프로젝트 폴더로 이동합니다.
3. 필요한 패키지를 설치합니다: `npm install`
4. Vue.js를 실행합니다: `npm run dev`

## 프로젝트 진행 과정

### 1. ERD

![ERD 다이어그램](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/a9e0cccb-e9a0-4eb7-8239-fd59357edfdd)

### 2. 크롤링

위의 ERD를 기반으로 Selenium, BeautifulSoup, Requests를 활용하여 카테고리, 언론사, 기자, 연령, 성별에 대한 정보를 수집하고 CSV 파일로 생성합니다.

![CSV 파일](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/3c1164c8-ee29-45f0-a166-963b249c8e65)
<br></br>
![image](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/f852affa-1a99-4836-aa08-b62121762070)


### 3. Django

수집한 CSV 데이터를 기반으로 Django 모델을 구성하고, Serializer를 사용하여 API를 구현합니다.

### 4. 프론트엔드

메인 페이지와 카테고리별 구독자 수 랭킹 페이지 등을 구현합니다.

## 프로젝트 결과

### 메인 페이지

![메인 페이지](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/563bcc8c-e4a4-4d5c-9e29-4b549ecfdf02)

### 카테고리별 구독자 수 랭킹 페이지

![랭킹 페이지 예시](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/347f089c-3cf1-4ef7-b5d5-937ed8a25b3d)

### 특정 언론사 연령별 구독자 수 정보 페이지

![KBS 연령 분포](https://github.com/ThePressLeaderboard/leaderboard/assets/88651495/434111e5-aa71-4282-9d1d-091f6845437f)

