from django.conf.urls.defaults import patterns, include, url
from online_payment.views import onli,detail,confirm_payment,onl_validatin,show
from piston.resource import Resource
from api.handlers import TaxHandler,DateHandler
from piston.doc import documentation_view 

tax_handler = Resource(TaxHandler)
date_handler= Resource(DateHandler)

urlpatterns = patterns('',
   url(r'^account_number/(?P<account_number>\d+)/$', tax_handler),
   url(r'^customer_id/(?P<customer_id>\d+)/$', tax_handler),
   url(r'^transaction_id/(?P<transaction_id>\d+)/$', tax_handler),		
   url(r'^date/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',date_handler),
   (r'^$', documentation_view),
   (r'^show/$', documentation_view),    
)


