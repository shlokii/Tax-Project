# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from online_payment.models import Tax_transaction,BackOffice_dummy,Accounts_dummy,Online_Transaction_dummy,Taxtype
import datetime


def onli(request):
	tax_list = Taxtype.objects.all()
	return render_to_response('base.html',locals())

def detail(request):
	if 'accno' and 'type' in request.GET and request.GET['accno']:
	        q = request.GET['accno']
		ttype=request.GET['type']
		Type=Taxtype.objects.get(tax_type_id=ttype)
	        custac = Accounts_dummy.objects.get(account_number=q)
		custinfo=BackOffice_dummy.objects.get(customer_id=custac.customer_id_id)
		return render_to_response('ttype1.html',locals())		
		#return render_to_response('ttype1.html',{'custac':ac , 'custinfo': cust})
    	else:
        	return HttpResponse('Please enter Valid accno')
def confirm_payment(request):
	if 'amount' in request.GET and request.GET['amount']:
		a=request.GET['amount']
		ttype=request.GET['taxtype']
		custname=request.GET['name']
		custid=request.GET['custid']
		accno=request.GET['accno']
		assyear=request.GET['ayear']
		return render_to_response('confirm.html',locals())
	else:
		return HttpResponse('Please enter Amount')
	
	
def onl_validatin(request):
	if 'amount' in request.GET and request.GET['amount']:
		cid=request.GET['id']
		ttid=request.GET['taxtype']
		a=request.GET['amount']
		custname=request.GET['name']
		accno=request.GET['accno']
		assyear=request.GET['ayear']
		amount=request.GET['amount']
		pin=request.GET['pin']
		custac = Accounts_dummy.objects.get(account_number=accno)
		#c=custac.
		#s=int(custac)==int(pin)
		#assert False
		now = datetime.datetime.now()
		if int(custac.ATM_PIN)==int(pin):
			p=Online_Transaction_dummy.objects.create(account_number_id=custac.account_number,amount_paid=amount)
			p.save()
			p1=Tax_transaction(customer_id_id=cid,account_number_id=accno,tax_type_id_id=ttid,transaction_id_id=p.transaction_id,date=now,amount_paid=amount,asses_year=assyear)
			p1.save()
			custac.amount=custac.amount-float(amount)
			custac.save()
			return render_to_response('done.html',locals())
		else:
			return render_to_response('confirm.html')
	else:
		return HttpResponse('Please enter Amount')




















	
