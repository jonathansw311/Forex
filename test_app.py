from unittest import TestCase
from app import app, checkFloat, checkCur, convert



class FlaskTests(TestCase):

    def test_app(self):
        with app.test_client() as client:
            
            
            res=client.get('/')
            html=res.get_data(as_text=True)
 
            self.assertEqual(res.status_code, 200)
            self.assertIn('<option value="CZK">CZK</option>\n', html)
            self.assertEqual(checkFloat(10), True)
            self.assertEqual(checkFloat('ten'), False)
            self.assertEqual(checkCur('USD', 'EUR'), True)
            self.assertEqual(checkCur('USD', 'EUR0'), False)
            self.assertEqual(convert('USD', 'USD', 1), 1)
    
    def test_route(self):
        with app.test_client() as client:
            
            calc=client.post('/calc', data={'begCurr':'USD', 'endCurr': 'EUR', 'amt': '1'})
            calc_html=calc.get_data(as_text=True)
 
            self.assertEqual(calc.status_code, 200)
            self.assertIn('<h1>We calculated', calc_html)