##@author Digvijay Singh
#This module is used to change the look of the native django-admin site
from django.contrib import admin
from online_payment.models import Tax_transaction,BackOffice_dummy,Accounts_dummy,Online_Transaction_dummy,Taxtype

##This is used by the admin site to modify the display of Tax_transaction table
class TaxAdmin(admin.ModelAdmin):
	##Change display format of fields
	list_display=('customer_id','account_number','transaction_id','date','amount_paid')
	##The tax transactions are filtered by date
	list_filter=['date']
	##The table can be searched based on Customer ID,Account Number and Date
	search_fields=['customer_id','account_number','transaction_id','date',]

##This is used by admin site to modify the display of BackOffice table    
class BOAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display=('customer_id','customer_name','customer_age','cust_street','cust_city','cust_state')
=======
	##Display format of fields
	list_display=('customer_id',)
>>>>>>> 167e14c3556efda588de90088769ec7042bc95f4

##This is used by admin site to modify the display of Accounts table    
class AAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display=('account_number','customer_id','ATM_PIN','amount','tax_exemption','date_account_created','service_tax_cut')
=======
	##Display format of fields
	list_display=('account_number',)
>>>>>>> 167e14c3556efda588de90088769ec7042bc95f4

##This is used by admin site to modify the display of Online_Transaction table    
class OTAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display=('transaction_id','account_number','amount_paid')
class TTAdmin(admin.ModelAdmin):
	list_display=('tax_type_id','tax_type_name')
     
=======
	##Display format of fields
	list_display=('transaction_id',)

##This is used by admin site to modify the display of Tax-Type table    
class TTAdmin(admin.ModelAdmin):
	##Display format of fields
	list_display=('tax_type_id',)

##All these classes need to be registred before usage
>>>>>>> 167e14c3556efda588de90088769ec7042bc95f4
admin.site.register(Tax_transaction,TaxAdmin)
admin.site.register(BackOffice_dummy,BOAdmin)
admin.site.register(Accounts_dummy,AAdmin)
admin.site.register(Online_Transaction_dummy,OTAdmin)
admin.site.register(Taxtype,TTAdmin)
