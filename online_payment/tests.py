"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime
from django.test import Client
from django.test import TestCase
from online_payment.models import Taxtype, BackOffice_dummy, Accounts_dummy, Online_Transaction_dummy, Tax_transaction



class PrintTransaction(TestCase):
  
  def setUp(self):
    self.customer= BackOffice_dummy.objects.create(customer_id=1123,customer_name="manu",customer_age=13,cust_street="asdfasd",cust_city="hyderabad",cust_state="AP")
    self.account=Accounts_dummy.objects.create(account_number=1000,customer_id_id=1123,ATM_PIN=123,amount=100000,tax_exemption=True,date_account_created=datetime.now(),service_tax_cut=100)
    self.tax_type=Taxtype.objects.create(tax_type_id=1,tax_type_name='FBT')
    self.tax_type1=Taxtype.objects.create(tax_type_id=2,tax_type_name='XYZ')
    self.tax_type2=Taxtype.objects.create(tax_type_id=3,tax_type_name='ABC')

  def test_count(self):
    count1 = Taxtype.objects.all().count()
    self.assertEqual(count1,3)
    
    
    
  def test_onli(self):
    c=Client()
    response = c.get('/onlinePayment/')
    self.assertEqual(response.status_code,200)
    
  def test_detail1(self):
    c=Client()
    response = c.get('/homePage/',{'type':1 ,'accno':1000})
    self.assertEqual(response.status_code,200)
   
  def test_detail2(self):
    c=Client()
    response = c.get('/homePage/',{'accno':1000})
    self.assertEqual(response.status_code,302)
  
  def test_detail2a(self):
    c=Client()
    response = c.get('/homePage/',{'type':1})
    self.assertEqual(response.status_code,302)
    
  def test_detail4(self):
    c=Client()
    response = c.get('/homePage/',{'type':1 ,'accno':1000})
    self.assertEqual(response.status_code,200)
    account_number_referred = response.context['custac']
    self.assertEqual(account_number_referred.customer_id_id,1123)
    
  def test_confirm_payment(self):
    c=Client()
    response = c.post('/homePage2/',{'custid': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 123,'taxtype':1,'ayear':2012,'amount':1000})
   ## print type(response)
    self.assertEqual(response.status_code,200)
  
  def test_confirm_payment1(self):
    c=Client()
    response = c.post('/homePage2/',{'custid': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':1000})
   ## print type(response)
    self.assertEqual(response.status_code,200)
  
  def test_onl_validatin(self):
    c=Client()
    response = c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':1000 ,'pin':1234})
    self.assertNotEqual(response.status_code,302)
    
  def test_onl_validatin2(self):
    c=Client()
    response = c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':1000 ,'pin':123})
    self.assertEqual(response.status_code,200)
  
  
  def test_show(self):
    c=Client()
    response= c.get('/showtaxes/',{'accno' : 121212})
    self.assertEqual(response.status_code,200)
  
  def test_tax_transantion(self):
    c=Client()
    try:
      response=c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':100 ,'pin':123})
      count = Tax_transaction.objects.get(account_number = 1000)
    except:
      self.assertEqual(2,1)
  
  def test_tax_transantion(self):
    c=Client()
    try:
      response=c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 100,'taxtype':1,'ayear':2012,'amount':100 ,'pin':123})
      count = Tax_transaction.objects.get(account_number = 100)
    except:
      self.assertEqual(1,1)
  
  def test_amount_insufficient(self):
    c=Client()
    response=c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':1000000000 ,'pin':123})
    self.assertEqual(response.status_code,200)
  
  def test_amount_insufficient1(self):
    c=Client()
    response=c.post('/homePage3/',{'id': 1123,'name':"manu" ,'street':"asdfasd",'city':"hyderabad",'state':"AP",'age':13,'accno': 1000,'taxtype':1,'ayear':2012,'amount':50000 ,'pin':123})
    count = Accounts_dummy.objects.get(account_number = 1000).amount 
    self.assertEqual(count,50000)
    
    
    
    
