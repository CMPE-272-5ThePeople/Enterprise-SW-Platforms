from django.test import TestCase

# Create your tests here.

# test cases employee APIs
class EmployeeViewsTestCase(TestCase):

    def test_get_employee_details(self):
        response = self.client.get('/api/get_employee_details/')  # employee get url
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "include template name to render the response")  # to check the template

    def test_add_employee(self):
        response = self.client.post('/api/get_employee_details/', {
                                    "employee_id": 1,
                                    "employee_first_name": "first_name",
                                    "employee_last_name": "last_name",
                                    "employee_designation": "test_employee",
                                    "employee_gender": "Male",
                                    "employee_contact_number": "+12345678976",
                                    "employee_manager_id": 1,
                                    "employee_email_id": "test@gmail.com"
                                    })
        self.assertEqual(response.status_code, 200)

    def test_addinValid_employeedata(self):
        response = self.client.post('/api/get_employee_details/', {
                            "employee_id": 1,
                            "employee_first_name": "first_name",
                            "employee_last_name": "last_name",
                            "employee_designation": "test_employee",
                            "employee_gender": "Male",
                            "employee_contact_number": "+1345678976",
                            "employee_manager_id": 1,
                            "employee_email_id": "test@gmail.com"
                            })
        self.assertEqual(response.status_code, 400)

    # test foreign key constraint of employee and department table
    # def setUpTestData(cls):
    #     # Set up non-modified objects used by all test methods
    #     user = User.objects.create( < fill
    #     params
    #     here >)
    #     NewsLetter.objects.create(NewsLetterID=1, Email='test@test.com', Connected=False, UserID=user)

# test cases notification APIs
class NotificationViewTestCase(TestCase):

    def test_get_notifications(self):
        response = self.client.get('/api/get_all_notifications/')  # employee get url
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_post_notifications(self):
        response = self.client.post('/api/get_all_notifications/', {'message':"test notification" })  # employee get url
        self.assertEqual(response.status_code, 200)
