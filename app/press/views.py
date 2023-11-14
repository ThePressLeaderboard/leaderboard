from django.shortcuts import render
from django.urls import reverse
from press_api.views import AgePressRanking
from rest_framework.test import APIClient
import requests



# def display_age_press_ranking(request):
#     api_url = request.build_absolute_uri(reverse('press-ranking-by-age'))  # press_api 앱의 API 엔드포인트 URL
#     # response = requests.get(api_url)
#     # data = response.json()  # API 응답 데이터 파싱

#     # return render(request, 'press/home.html', {'data': data})
#     response = requests.get(api_url)
#     data = response.json()  # API 응답 데이터 파싱

#     # 데이터를 카테고리 목록과 함께 전달
#     categorized_data = {}
#     category_list = []  # 카테고리 목록 생성

#     for item in data:
#         for category in item['categories']:
#             category_name = category['category_name']
#             press_ranking = category['press_ranking']

#             if category_name not in categorized_data:
#                 categorized_data[category_name] = []

#             categorized_data[category_name].append({
#                 'age_group': item['age_group'],
#                 'press_ranking': press_ranking
#             })

#             if category_name not in category_list:
#                 category_list.append(category_name)  # 중복되지 않는 카테고리만 추가

#     return render(request, 'press/home.html', {'categorized_data': categorized_data, 'category_list': category_list})


# def category_view(request, category):
#     api_url = request.build_absolute_uri(reverse('press-ranking-by-age'))  # press_api 앱의 API 엔드포인트 URL
#     response = requests.get(api_url)
#     data = response.json()  # API 응답 데이터 파싱

#     # 선택한 카테고리에 해당하는 데이터 필터링
#     filtered_data = [item for item in data if any(category_data['category_name'] == category for category_data in item['categories'])]

#     # 데이터를 나이대 별로 그룹화
#     categorized_data = {}
#     for item in filtered_data:
#         for age_group_data in item['categories']:
#             if age_group_data['category_name'] == category:
#                 age_group = age_group_data['age_group']
#                 press_ranking = age_group_data['press_ranking']

#                 if age_group not in categorized_data:
#                     categorized_data[age_group] = []

#                 categorized_data[age_group].append({
#                     'category_name': category,
#                     'press_ranking': press_ranking
#                 })

#     return render(request, 'press/category.html', {'categorized_data': categorized_data, 'selected_category': category})

# def display_age_press_ranking(request):
#     api_url = request.build_absolute_uri(reverse('press-ranking-by-age'))  # press_api 앱의 API 엔드포인트 URL
#     response = requests.get(api_url)
#     data = response.json()  # API 응답 데이터 파싱

#     # 데이터를 카테고리 목록과 함께 전달
#     categorized_data = {}
#     category_list = []  # 카테고리 목록 생성

#     for item in data:
#         for category in item['categories']:
#             category_name = category['category_name']
#             press_ranking = category['press_ranking']

#             if category_name not in categorized_data:
#                 categorized_data[category_name] = []

#             categorized_data[category_name].append({
#                 'age_group': item['age_group'],
#                 'press_ranking': press_ranking
#             })

#             if category_name not in category_list:
#                 category_list.append(category_name)  # 중복되지 않는 카테고리만 추가

#     return render(request, 'press/home.html', {'categorized_data': categorized_data, 'category_list': category_list})

# def category_view(request, category):
#     api_url = request.build_absolute_uri(reverse('press-ranking-by-age'))  # press_api 앱의 API 엔드포인트 URL
#     response = requests.get(api_url)
#     data = response.json()  # API 응답 데이터 파싱

#     # 선택한 카테고리에 해당하는 데이터 필터링
#     filtered_data = [item for item in data if any(category_data['category_name'] == category for category_data in item['categories'])]

#     # 데이터를 나이대 별로 그룹화
#     categorized_data = {}
#     for item in filtered_data:
#         for age_group_data in item['categories']:
#             if age_group_data['category_name'] == category:
#                 age_group = age_group_data['age_group']
#                 press_ranking = age_group_data['press_ranking']

#                 if age_group not in categorized_data:
#                     categorized_data[age_group] = []

#                 categorized_data[age_group].append({
#                     'category_name': category,
#                     'press_ranking': press_ranking
#                 })

#     return render(request, 'press/category.html', {'categorized_data': categorized_data, 'selected_category': category})