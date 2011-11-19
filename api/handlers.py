##@author Digvijay Singh
##This module is used for generating the API for our app.
from piston.handler import BaseHandler
from online_payment.models import Tax_transaction
from piston.doc import generate_doc
import datetime

##Handling the request for APIs
class TaxHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Tax_transaction   

   def read(self, request, account_number=0,customer_id=0,transaction_id=0,year=1111):
       if account_number:
            setquer=Tax_transaction.objects.filter(account_number=account_number)
	    return setquer
       if customer_id:
            setquer=Tax_transaction.objects.filter(customer_id=customer_id)
	    return setquer		
       if transaction_id:
            setquer=Tax_transaction.objects.filter(transaction_id=transaction_id)
	    return setquer
       else:
            return Tax_transaction.objects.all()

##Handling the request for APIs
class DateHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Tax_transaction   

   def read(self, request,year=1111,month=11,day=11):
       if year and month and day:
	    date1=datetime.date(int(year),int(month),int(day))
            setquer=Tax_transaction.objects.filter(date=date1)
	    return setquer			    
       else:
            return Tax_transaction.objects.all()

doc = generate_doc(TaxHandler)

print doc.name 
#print doc.model

methods = doc.get_methods()

for method in methods:
   print method.name # -> 'read'
   print method.signature # -> 'read(post_slug=<optional>)'

   sig = ''

   for argn, argdef in method.iter_args():
      sig += argn

      if argdef:
         sig += "=%s" % argdef

      sig += ', '

   sig = sig.rstrip(",")

   print sig # -> 'read(repo_slug=None)'
