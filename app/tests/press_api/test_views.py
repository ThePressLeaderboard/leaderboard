from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from press.models import Category

# class MalePressRankingTest(APITestCase):
#     def setUp(self):
#         # 크롤링 데이터 이미 넣음
#         pass

#     def test_male_press_ranking(self):
#         # 실제 랭킹 10위 가져옴
#         actual_top_10_press = Press.objects.annotate(
#             male_subscriber_count=Sum(
#                 F("journalist__subscriber_count")
#                 * F("journalist__gender__percentage")
#                 / 100,
#                 output_field=models.IntegerField(),
#                 filter=models.Q(journalist__gender__gender="M"),
#             )
#         ).order_by("-male_subscriber_count")[:10]

#         # api 실행 결과 가져옴
#         response = self.client.get(reverse("male-press-ranking"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # 언론사 이름만 추출
#         api_top_10_press = [press["press_name"] for press in response.data]

#         # 실제 랭킹 언론사와 api 결과 언론사 이름 비교
#         self.assertCountEqual(
#             [press.press_name for press in actual_top_10_press], api_top_10_press
#         )


# class FemalePressRankingTest(APITestCase):
#     def setUp(self):
#         # 크롤링 데이터 이미 넣음
#         pass

#     def test_female_press_ranking(self):
#         # 실제 랭킹 10위 가져옴
#         actual_top_10_press = Press.objects.annotate(
#             male_subscriber_count=Sum(
#                 F("journalist__subscriber_count")
#                 * F("journalist__gender__percentage")
#                 / 100,
#                 output_field=models.IntegerField(),
#                 filter=models.Q(journalist__gender__gender="F"),
#             )
#         ).order_by("-male_subscriber_count")[:10]

#         # api 실행 결과 가져옴
#         response = self.client.get(reverse("female-press-ranking"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # 언론사 이름만 추출
#         api_top_10_press = [press["press_name"] for press in response.data]

#         # 실제 랭킹 언론사와 api 결과 언론사 이름 비교
#         self.assertCountEqual(
#             [press.press_name for press in actual_top_10_press], api_top_10_press
#         )


# class JournalistGenderDetailTest(APITestCase):
#     def setUp(self):
#         # 크롤링 데이터 이미 넣음
#         pass

#     def test_journalist_gender_detail(self):
#         journalist_id = 79204
#         genders = Gender.objects.filter(journalist_id=journalist_id)

#         url = reverse("journalist-gender-detail", kwargs={"pk": journalist_id})
#         response = self.client.get(url)

#         self.assertEqual(response.status_code, 200)

#         data = response.json()
#         self.assertEqual(len(data), len(genders))


class CategoryRankingTest(APITestCase):
    def test_get_queryset(self):
        url = reverse("categoryranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_queryset_with_sort(self):
        url = reverse("categoryranking") + "?sort=category_name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_queryset_with_number(self):
        url = reverse("categoryranking") + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryDetailTest(APITestCase):
    def test_get_category_detail(self):
        category_name = "종합지"
        Category.objects.create(category_name=category_name)

        url = reverse("categorydetail", args=[category_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["category_name"], category_name)

    def test_delete_category_detail(self):
        category_name = "종합지"
        Category.objects.create(category_name=category_name)

        url = reverse("categorydetail", args=[category_name])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url_after_delete = reverse("categorydetail", args=[category_name])
        response_after_delete = self.client.get(url_after_delete)
        self.assertEqual(response_after_delete.status_code, status.HTTP_404_NOT_FOUND)


class CategoryPressRankingTest(APITestCase):
    def test_get_category_press_ranking(self):
        category_name = "종합지"
        url = reverse("categorypressranking", args=[category_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_press_ranking_with_sort(self):
        category_name = "종합지"
        url = reverse("categorypressranking", args=[category_name]) + "?sort=press_name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_press_ranking_with_number(self):
        category_name = "종합지"
        url = reverse("categorypressranking", args=[category_name]) + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryJournalistRankingTest(APITestCase):
    def test_get_category_journalist_ranking(self):
        category_name = "종합지"
        url = reverse("categoryjournalistranking", args=[category_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_journalist_ranking_with_sort(self):
        category_name = "종합지"
        url = reverse("categoryjournalistranking", args=[category_name]) + "?sort=name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_journalist_ranking_with_number(self):
        category_name = "종합지"
        url = reverse("categoryjournalistranking", args=[category_name]) + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PressRankingTest(APITestCase):
    def test_get_category_press_ranking(self):
        url = reverse("pressranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_press_ranking_with_sort(self):
        url = reverse("pressranking") + "?sort=press_name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_press_ranking_with_number(self):
        url = reverse("pressranking") + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""

#######################에러가 있어서 수정해야함##########################

class PressDetailTest(APITestCase):


    def test_get_press_detail(self):
        press_name = '국민일보'
        url = reverse('pressdetail', args=[press_name])
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.data['press_name'], self.press)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_get_category_detail(self):
    #     # 이미 데이터베이스에 존재하는 카테고리를 사용
    #     category_name = '종합지'
    #     Category.objects.create(category_name=category_name)

    #     url = reverse('categorydetail', args=[category_name])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['category_name'], category_name)

    def test_delete_press_detail(self):
        press_name = '국민일보'
        url = reverse('pressdetail', args=[press_name])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Press 데이터가 실제로 삭제되었는지 확인하는 코드 추가

"""


class PressJournallistRankingTest(APITestCase):
    def test_get_category_journalist_ranking(self):
        press_name = "국민일보"
        url = reverse("pressjournalistranking", args=[press_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_journalist_ranking_with_sort(self):
        press_name = "동아일보"
        url = reverse("pressjournalistranking", args=[press_name]) + "?sort=name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category_journalist_ranking_with_number(self):
        press_name = "문화일보"
        url = reverse("pressjournalistranking", args=[press_name]) + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SectionRankingTest(APITestCase):
    def test_get_section_ranking(self):
        url = reverse("sectionranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_section_ranking_with_sort(self):
        url = reverse("sectionranking") + "?sort=section_name"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_section_ranking_with_number(self):
        url = reverse("sectionranking") + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""

#######################에러가 있어서 수정해야함##########################

class SectionDetailTest(APITestCase):
    def setUp(self):
        self.section_name = '경제'

    def test_get_section_detail(self):
        url = reverse('sectiondetail', args=['경제'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['section_name'], self.section_name)

    def test_delete_section_detail(self):
        url = reverse('sectiondetail', args=[self.section_name])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url_after_delete = reverse('sectiondetail', args=[self.section_name])
        response_after_delete = self.client.get(url_after_delete)
        self.assertEqual(response_after_delete.status_code, status.HTTP_404_NOT_FOUND)
"""


class SectionJournallistRankingTest(APITestCase):
    def setUp(self):
        self.section_name = "경제"

    def test_get_section_journalist_ranking(self):
        url = reverse("setionjournalistranking", args=[self.section_name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_section_journalist_ranking_with_sort(self):
        url = (
            reverse("setionjournalistranking", args=[self.section_name]) + "?sort=name"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_section_journalist_ranking_with_number(self):
        url = reverse("setionjournalistranking", args=[self.section_name]) + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class JournalistRankingTest(APITestCase):
    def test_get_journalist_ranking(self):
        url = reverse("journalistranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_journalist_ranking_with_sort(self):
        url = reverse("journalistranking") + "?sort=subscriber_count"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_journalist_ranking_with_number(self):
        url = reverse("journalistranking") + "?number=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""

#######################에러가 있어서 수정해야함##########################

class JournalistDetailTest(APITestCase):
    def setUp(self):
        self.journalist_id = 77078

    def test_get_journalist_detail(self):
        url = reverse('journalistdetail', args=[self.journalist_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_journalist_detail(self):
        url = reverse('journalistdetail', args=[self.journalist_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response_after_delete = self.client.get(url)
        self.assertEqual(response_after_delete.status_code, status.HTTP_404_NOT_FOUND)
"""


class SubscriberAgeDetailTest(APITestCase):
    def test_get_subscriber_age_detail(self):
        url = reverse("subscribers-age-detail", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryWiseAgePressRankingTest(APITestCase):
    def test_get_category_wise_age_press_ranking(self):
        url = reverse("press-ranking-by-categoryage")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TotalAgeByPressTest(APITestCase):
    def test_get_total_age_by_press(self):
        url = reverse("press-ranking-by-age")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MalePressRankingTest(APITestCase):
    def test_get_male_press_ranking(self):
        url = reverse("male-press-ranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FemalePressRankingTest(APITestCase):
    def test_get_male_press_ranking(self):
        url = reverse("female-press-ranking")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class JournalistGenderDetailTest(APITestCase):
    def test_get_journalist_gender_detail(self):
        url = reverse("journalistgenderdetail", args=[self.journalist.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["gender"], "M")
