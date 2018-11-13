from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import HeritageSite, HeritageSiteCategory


class IndexViewTest(TestCase):

	def test_view_route_redirection(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 302)


class HomeViewTest(TestCase):

	def test_view_route(self):
		response = self.client.get('/heritagesites/')
		self.assertEqual(response.status_code, 200)

	def test_view_route_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

	def test_view_template(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'heritagesites/home.html')


class AboutViewTest(TestCase):

	def test_view_route(self):
		response = self.client.get('/heritagesites/about/')
		self.assertEqual(response.status_code, 200)

	def test_view_route_fail(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 404)

	def test_view_route_name(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)

	def test_view_template(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'heritagesites/about.html')


class SiteModelTest(TestCase):

	def setUp(self):
		HeritageSiteCategory.objects.create(category_name='Cultural')
		category = HeritageSiteCategory.objects.get(pk=1)
		HeritageSite.objects.create(
			# TODO restore missing properties and values
			site_name='Cultural Landscape and Archaeological Remains of the Bamiyan Valley',
			heritage_site_category_id=category.category_id,
			description='The cultural landscape and archaeological remains of the Bamiyan Valley represent the artistic and religious developments which from the 1st to the 13th centuries characterized ancient Bakhtria, integrating various cultural influences into the Gandhara school of Buddhist art. The area contains numerous Buddhist monastic ensembles and sanctuaries, as well as fortified edifices from the Islamic period. The site is also testimony to the tragic destruction by the Taliban of the two standing Buddha statues, which shook the world in March 2001.',

			justification='Criterion (i): The Buddha statues and the cave art in Bamiyan Valley are an outstanding representation of the Gandharan school in Buddhist art in the Central Asian region.\nCriterion (ii) : The artistic and architectural remains of Bamiyan Valley, and an important Buddhist centre on the Silk Road, are an exceptional testimony to the interchange of Indian, Hellenistic, Roman, Sasanian influences as the basis for the development of a particular artistic expression in the Gandharan school. To this can be added the Islamic influence in a later period.\nCriterion (iii): The Bamiyan Valley bears an exceptional testimony to a cultural tradition in the Central Asian region, which has disappeared.\nCriterion (iv): The Bamiyan Valley is an outstanding example of a cultural landscape which illustrates a significant period in Buddhism.\nCriterion (vi): The Bamiyan Valley is the most monumental expression of the western Buddhism. It was an important centre of pilgrimage over many centuries. Due to their symbolic values, the monuments have suffered at different times of their existence, including the deliberate destruction in 2001, which shook the whole world.',
			date_inscribed='2003',
			longitude='67.82525000',
			latitude='34.84694000',
			area_hectares='158.9265',
			transboundary=0)

	def test_site_name(self):
		site = HeritageSite.objects.get(pk=1)
		expected_object_name = f'{site.site_name}'
		# aa = f'{site.heritage_site_category_id}'
		self.assertEqual(expected_object_name, 'Cultural Landscape and Archaeological Remains of the Bamiyan Valley')


class SiteListViewTest(TestCase):

	def test_view_route(self):
		response = self.client.get('/heritagesites/sites/')
		self.assertEqual(response.status_code, 200)

	def test_view_route_fail(self):
		response = self.client.get('/sites/')
		self.assertEqual(response.status_code, 404)

	def test_view_route_name(self):
		response = self.client.get(reverse('sites'))
		self.assertEqual(response.status_code, 200)

	def test_view_template(self):
		response = self.client.get(reverse('sites'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'heritagesites/site.html')