from django.conf.urls import patterns, include, url
from online_payment.views import onli,detail,confirm_payment,onl_validatin
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tax.views.home', name='home'),
    # url(r'^tax/', include('tax.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^onlinePayment/$', onli),
    (r'^onlinePayment/homePage/$', detail),
    (r'^homePage2/$', confirm_payment),
     (r'^homePage3/$', onl_validatin),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
