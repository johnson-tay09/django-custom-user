from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Card


class CardTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.card = Card.objects.create(
            title="pickle",
            body="refreshing",
            author=self.user,
        )

    # def test_string_representation(self):
    #     card = Card(title="Snicker")
    #     self.assertEqual(str(card), card.title)

    # def test_card_content(self):
    #     self.assertEqual(f"{self.card.title}", "pickle")
    #     self.assertEqual(f"{self.card.author.username}", "tester")
    #     self.assertEqual(f"{self.card.body}", "refreshing")

    def test_card_list_view(self):
        response = self.client.get(reverse("card_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "card-list.html")

    # def test_card_detail_view(self):
    #     response = self.client.get(reverse("card_detail", args="1"))  #'/Cards/1/')
    #     no_response = self.client.get("/Cards/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "refreshing")
    #     self.assertTemplateUsed(response, "card-detail.html")

    # def test_card_create_view(self):
    #     response = self.client.post(
    #         reverse("card_create"),
    #         {
    #             "title": "Chicharrones",
    #             "body": "Low carb",
    #             "author": self.user,
    #         },
    #     )

    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Chicharrones")
    #     self.assertContains(response, "Low carb")
    #     self.assertTemplateUsed(response, "card-create.html")

    # def test_card_update_view(self):
    #     response = self.client.post(
    #         reverse("card_update", args="1"),
    #         {
    #             "title": "Updated title",
    #             "body": "Updated body",
    #         },
    #     )
    #     self.assertEqual(response.status_code, 302)

    # def test_card_update_view_redirect(self):
    #     response = self.client.post(
    #         reverse("card_update", args="1"),
    #         {
    #             "title": "Updated title",
    #             "body": "Updated body",
    #         },
    #         follow=True,
    #     )

    #     self.assertEqual(response.status_code, 200)

    #     self.assertContains(response, "Updated title")

    #     self.assertTemplateUsed("card-detail.html")

    # def test_card_delete_view(self):
    #     response = self.client.get(reverse("card_delete", args="1"))
    #     self.assertEqual(response.status_code, 200)