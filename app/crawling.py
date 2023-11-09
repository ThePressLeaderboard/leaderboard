import csv
from press_api.models import *

def save_data_to_models():
    with open('../crawling/category.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 첫 번째 줄은 헤더이므로 건너뜁니다.
        print(reader)
        for row in reader:
            print(row)
        #     # csv 파일의 각 행을 모델 객체로 변환합니다.
        #     model1 = Model1(field1=row[0], field2=row[1], ...)
        #     model2 = Model2(field1=row[2], field2=row[3], ...)
        #     model3 = Model3(field1=row[4], field2=row[5], ...)
            
        #     # 변환된 모델 객체를 데이터베이스에 저장합니다.
        #     model1.save()
        #     model2.save()
        #     model3.save()
save_data_to_models()