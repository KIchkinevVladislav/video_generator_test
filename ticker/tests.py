import os
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import TickerText
from .forms import TickerTexForm


class IndexViewTest(TestCase):
    def test_index_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Video generator')
        self.assertTemplateUsed(response, 'ticker/index.html')


class TickerViewTest(TestCase):
    def setUp(self):
        self.path = reverse('ticker:ticker_generator')

    def test_get_request(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticker/ticker_generator.html')
        self.assertIsInstance(response.context['form'], TickerTexForm)
        self.assertContains(response, 'Create video')        

    def test_post_request_valid_data(self):
        data = {
            'text': 'Valid text',
            'text_color': 'white',
            'frame_color': 'black',
            'video_size': '100'
        }
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TickerText.objects.count(), 1)
        ticker_text = TickerText.objects.first()
        self.assertEqual(ticker_text.text, 'Valid text')
        self.assertIn('attachment; filename="new_video_ticker.mp4"', response['Content-Disposition'])

    def test_post_request_invalid_dat(self):
        data = {
            'text': 'A' * 33,
            'text_color': 'white', 
            'frame_color': 'black',
            'video_size': '100'
        }
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TickerText.objects.count(), 0)

    def test_post_request_empty_text(self):
        data = {
            'text': '',
            'text_color': 'white', 
            'frame_color': 'black',
            'video_size': '100'
        }
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TickerText.objects.count(), 0)

    def test_video_deletion(self):
        data = {
            'text': 'Valid text',
            'text_color': 'white',
            'frame_color': 'black',
            'video_size': '100'
        }
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, 200)
        
        video_filename = 'new_video_ticker.mp4'
        video_path = os.path.join('video', video_filename)
        self.assertFalse(os.path.exists(video_path))
