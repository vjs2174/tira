from django.test import TestCase, override_settings
from django.http import HttpResponse, HttpResponseServerError
from django.urls import path
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from http import HTTPStatus
from tira.views import forbidden, not_found, server_error


# def response_403_handler(request, exception=None):
#     return render(request, 'tira/error.html', status=HTTPStatus.FORBIDDEN)

# def response_404_handler(request, exception=None):
#     return render(request, 'tira/error.html', status=HTTPStatus.NOT_FOUND)

# def response_500_handler(request, exception=None):
#     return render(request, 'tira/error.html', status=HTTPStatus.INTERNAL_SERVER_ERROR)

def forbidden_error_view(request):
    raise PermissionDenied

def server_error_view(request):
    raise Exception("")

urlpatterns = [
    path('403', forbidden_error_view),
    path('500', server_error_view)
]
handler403 = forbidden
handler404 = not_found
handler500 = server_error

@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(TestCase):
    def test_handler_renders_template_at_403_response(self):
        response = self.client.get('/403')
        self.assertContains(response, '403 - FORBIDDEN', status_code=403)

    def test_handler_renders_template_at_404_response(self):
        response = self.client.get('/404')
        self.assertContains(response, '404 - NOT_FOUND', status_code=404)
        
    def test_handler_renders_template_at_500_response(self):
        response = self.client.get('/500')
        self.assertContains(response, '500 - INTERNAL_SERVER_ERROR', status_code=500)


class TestSetup(TestCase):
    def setUp(self) -> None:
        self.setup = True

    def test_setup_success(self):
        """ test if tests work """
        self.assertTrue(self.setup)
