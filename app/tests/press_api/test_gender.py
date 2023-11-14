from django.db.models import F, Sum
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from press.models import Gender, Press, models


class MalePressRankingTest(APITestCase):
    def setUp(self):
        # 크롤링 데이터 이미 넣음
        pass

    def test_male_press_ranking(self):
        # 실제 랭킹 10위 가져옴
        actual_top_10_press = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="M"),
            )
        ).order_by("-male_subscriber_count")[:10]

        # api 실행 결과 가져옴
        response = self.client.get(reverse("male-press-ranking"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 언론사 이름만 추출
        api_top_10_press = [press["press_name"] for press in response.data]

        # 실제 랭킹 언론사와 api 결과 언론사 이름 비교
        self.assertCountEqual(
            [press.press_name for press in actual_top_10_press], api_top_10_press
        )


class FemalePressRankingTest(APITestCase):
    def setUp(self):
        # 크롤링 데이터 이미 넣음
        pass

    def test_female_press_ranking(self):
        # 실제 랭킹 10위 가져옴
        actual_top_10_press = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="F"),
            )
        ).order_by("-male_subscriber_count")[:10]

        # api 실행 결과 가져옴
        response = self.client.get(reverse("female-press-ranking"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 언론사 이름만 추출
        api_top_10_press = [press["press_name"] for press in response.data]

        # 실제 랭킹 언론사와 api 결과 언론사 이름 비교
        self.assertCountEqual(
            [press.press_name for press in actual_top_10_press], api_top_10_press
        )


class JournalistGenderDetailTest(APITestCase):
    def setUp(self):
        # 크롤링 데이터 이미 넣음
        pass

    def test_journalist_gender_detail(self):
        journalist_id = 79204
        genders = Gender.objects.filter(journalist_id=journalist_id)

        url = reverse("journalist-gender-detail", kwargs={"pk": journalist_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), len(genders))

        for item in data:
            gender = Gender.objects.get(id=item["id"])
            self.assertIn(gender, genders)
