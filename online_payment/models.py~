##@author Digvijay Singh and Shlok Chaurasia
from django.db import models
import datetime

##This is used to create a Taxtype table in the database,which containes the different types of taxes and their ids
class Taxtype(models.Model):
	##ID of the Taxtype,integer,primary key of this table
	tax_type_id=models.IntegerField(primary_key=True)
	##Name of the Taxtype,a Character Field of Max Length 150
	tax_type_name=models.CharField(max_length=150)
	##Used to print the Taxtype name in place of the object
	##@param self: The object calling this method
	##@return string: The taxtype name
	def __unicode__(self):
		return "%s " % self.tax_type_name

##This is used to create a BackOffice dummy table in the database,which containes customers' records.
##We used the dummy because we needed the API from another group,which was not ready
class BackOffice_dummy(models.Model):
	##ID of the Customer,integer,primary key of this table
	customer_id=models.IntegerField(primary_key=True)
	##Name of the Customer,a Character Field of Max Length 50
	customer_name=models.CharField(max_length=50)
	##Age of the Customer,Integer
	customer_age=models.IntegerField()
	##Street Name,Customer's address,a Character Field of Max Length 150
	cust_street=models.CharField(max_length=150)
	##City,Customer's address,a Character Field of Max Length 50
	cust_city=models.CharField(max_length=50)
	##State,Customer's address,a Character Field of Max Length 50
	cust_state=models.CharField(max_length=50)	
	##Used to print the Customer name in place of the object
	##@param self: The object calling this method
	##@return string: The Customer's name
	def __unicode__(self):
		return "%s " % self.customer_name
	
##This is used to create an Accounts dummy table in the database,which containes customers' accounts.
##We used the dummy because we needed the API from another group,which was not ready
class Accounts_dummy(models.Model):
	##Account Number of the Customer,integer,primary key of this table
	account_number=models.IntegerField(primary_key=True)
	##ID of the Customer,integer,foreign key to Backoffice dummy
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	##ATM Pin of the Customer,integer,unique
	ATM_PIN=models.IntegerField(unique=True)
	##Amount in Customer's account,float
	amount=models.FloatField()
	##Boolean Field to check if the customer was exempted from paying Tax,i.e if he has filled 15G/15H forms
	tax_exemption=models.BooleanField()
	##Date of Account creation of Customer
	date_account_created=models.DateTimeField()
	##Used in the logic of cutting Rs 100 from the customer's account every year as service tax
	service_tax_cut=models.IntegerField(editable=False,default=0)
	##Used to print the Customer's Account number in place of the object
	##@param self: The object calling this method
	##@return string: The Customer's account number
	def __unicode__(self):
		return "%s " % self.account_number

##This is used to create an Online_Transaction dummy table in the database,which containes records of the customers' online transactions.
##We used the dummy because we needed the API from another group,which was not ready
class Online_Transaction_dummy(models.Model):
	##ID of the Transaction,primary key,Automatically increases on adding another transaction
	transaction_id=models.AutoField(primary_key=True)
	##Account Number of the Customer,foreign key to Accounts dummy
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	##Amount paid as tax by the Customer,float
	amount_paid=models.FloatField()
	##Used to print the Transaction ID in place of the object
	##@param self: The object calling this method
	##@return string: Transaction ID
	def __unicode__(self):
		return "%s " % self.transaction_id

##This is used to create an Tax_Transaction table in the database,which containes records of the Tax payed by the customers.
class Tax_transaction(models.Model):
	##ID of the Customer,integer,foreign key to Backoffice dummy
	customer_id=models.ForeignKey(BackOffice_dummy,to_field='customer_id')
	##Account Number of the Customer,foreign key to Accounts dummy
	account_number=models.ForeignKey(Accounts_dummy,to_field='account_number')
	##Tax Type ID,foreign key to Taxtpye table
	tax_type_id=models.ForeignKey(Taxtype,to_field='tax_type_id')
	##ID of the Transaction,foreign key to Online Transaction dummy
	transaction_id=models.ForeignKey(Online_Transaction_dummy,to_field='transaction_id')
	##Date of the Tax Transaction
	date=models.DateField()
	##Amount payed as Tax,float
	amount_paid=models.FloatField()
	##Assesment Year
	asses_year=models.CharField(max_length=50)
