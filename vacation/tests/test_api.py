from rest_framework.test import APITestCase
from django.urls import reverse
from vacation.models import Villa, Yacht, Vehicle
from vacation.serializer import VillaSerializer, YachtSerializer, VehicleSerializer
from rest_framework import status


class VillaApiTestCase(APITestCase):

    def test_get_list(self):
        villa_1 = Villa.objects.create(title='Вилла_1', description='Описание', price_per_day=500)

        response = self.client.get(reverse('vacation_villas_api_list'))

        serial_data = VillaSerializer([villa_1], many=True).data
        serial_data = {'villas_list': serial_data}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)
