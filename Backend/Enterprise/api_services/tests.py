from django.test import TestCase

# Create your tests here.

# test cases employee APIs
class EmployeeViewsTestCase(TestCase):

    def test_get_employee_details(self):
        response = self.client.get('/api/get_employee_details/')  # employee get url
        self.assertEqual(response.status_code, 200)


# test cases notification APIs
# class NotificationViewTestCase(TestCase):
#
#     def test_get_notifications(self):
#         response = self.client.get('/api/get_notification_details/')  # employee get url
#         print(response)
#         self.assertEqual(response.status_code, 200)
#
#     def test_post_notifications(self):
#         response = self.client.post('/api/get_notification_details/', {'message':"test notification" })  # employee get url
#         self.assertEqual(response.status_code, 200)
#
# class TrainingViewTestCase(TestCase):
