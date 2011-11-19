from django.db import models
import datetime

class Taxtype(models.Model):
	tax_type_id=models.IntegerField(primary_key=True)
	tax_type_name=models.CharField(max_length=150)
	def __unicode__(self):
		return "%s " % self.tax_type_name

class BackOffice_dummy(models.Model):
	customer_id=models.IntegerField(primary_key=True)
	customer_name=models.CharField(max_length=50)
	customer_age=models.IntegerField()
	cust_street=models.CharField(max_length=150)
	cust_city=models.CharField(max_length=50)#to be added by digi
	cust_state=models.CharField(max_length=50)	
	def __unicode__(self):
		return "%s " % self.customer_id
	
class Accounts_dummy(models.Model):
	account_number=models.IntegerField(primary_key=True)
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	ATM_PIN=models.IntegerField(unique=True)
	amount=models.FloatField()
	tax_exemption=models.BooleanField()
	date_account_created=models.DateTimeField()
	service_tax_cut=models.IntegerField(editable=False,default=0)
	def __unicode__(self):
		return "%s " % self.account_number

class Online_Transaction_dummy(models.Model):
	transaction_id=models.AutoField(primary_key=True)
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	amount_paid=models.FloatField()
	def __unicode__(self):
		return "%s " % self.transaction_id

class Tax_transaction(models.Model):
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	tax_type_id=models.ForeignKey(Taxtype,to_field='tax_type_id')
	transaction_id=models.ForeignKey(Online_Transaction_dummy,to_field='transaction_id',primary_key=True)
	date=models.DateField()
	amount_paid=models.FloatField()
	asses_year=models.CharField(max_length=50)
