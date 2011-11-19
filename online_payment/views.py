##@author Shlok Chaurasia and Digvijay Singh
##This module contains all the backend logic happening in our Web Application
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from online_payment.models import Tax_transaction,BackOffice_dummy,Accounts_dummy,Online_Transaction_dummy,Taxtype
import datetime

##This method/view is called on the starting page of our Application
##@param request: This is the HTTP Request object,which is formed when we request for the starting page of our App.
##@return response:An HTTP Response Object,containing the name of the template which is to be rendered,and its context,which contains all the local variables of this function
def onli(request):
	##Get all objects from the table Taxtype in a dictionary,and send this to the rendering template
	tax_list = Taxtype.objects.all()
	return render_to_response('base.html',locals())

##This method/view is called when the customer enters his account number on the first page and requests for payment of a Tax Type.
##@param request: This is the HTTP Request object,which is formed when we request for the starting page of our App.
##@return response:An HTTP Response Object,containing the name of the template which is to be rendered,and its context,which contains all the local variables of this function
def detail(request):
	if 'accno' and 'type' in request.GET and request.GET['accno']:
		##Getting the Account number from the request.GET dictionary
	        q = request.GET['accno']
		##Getting the Tax type from the request.GET dictionary
		ttype=request.GET['type']
		##Getting the specific Tax type row corresponding to the tax type id.
		Type=Taxtype.objects.get(tax_type_id=ttype)
		try:
			##Getting the row from the Accounts dummy table with account number q
	        	custac = Accounts_dummy.objects.get(account_number=q)
			##Getting the row from the BackOffice dummy table with cust.customer id
			custinfo=BackOffice_dummy.objects.get(customer_id=custac.customer_id_id)
			if custinfo.customer_age>=60:
				custac.tax_exemption=True;
			else:
				custac.tax_exemption=False;
			##Logic for deducting Rs 100 from Customer's account every year
			now=datetime.datetime.now()
			account_created_on=custac.date_account_created;
			difference=((now-account_created_on).days)/365
			service_tax=100
			if custac.service_tax_cut!=difference:
				custac.amount=custac.amount-service_tax;
				custac.save()
				custac.service_tax_cut=difference
				custac.save()
				
		except:
			##Saving the error so that it can be showed in the rendered HTML page
			error="Invalid Account Number.It does Not Exists."
			return render_to_response('error.html',locals())
					
		return render_to_response('ttype1.html',locals())		
		#return render_to_response('ttype1.html',{'custac':ac , 'custinfo': cust})
    	#else:
        	#return HttpResponseRedirect('/onlinePayment/')


##This method/view is called when the customer enters the amount of Tax he wants to pay,and enters a payment portal.
##@param request: This is the HTTP Request object,which is formed when we request for the starting page of our App.
##@return response:An HTTP Response Object,containing the name of the template which is to be rendered,and its context,which contains all the local variables of this function

def confirm_payment(request):
	if 'amount' in request.GET and request.GET['amount']:
		##Getting the Amount from the request.GET dictionary
		a=request.GET['amount']
		##Getting the tax type id from the request.GET dictionary
		ttype=request.GET['taxtype']
		##Getting the Customer Name from the request.GET dictionary
		custname=request.GET['name']
		##Getting the Customer ID from the request.GET dictionary
		custid=request.GET['custid']
		##Getting the Account number from the request.GET dictionary
		accno=request.GET['accno']
		##Getting the Assesment year from the request.GET dictionary
		assyear=request.GET['ayear']
		return render_to_response('confirm.html',locals())
	else:
		return HttpResponse('Please enter Amount')
	
##This method/view is called when the customer enters his PIN on the payment portal.
##@param request: This is the HTTP Request object,which is formed when we request for the starting page of our App.
##@return response:An HTTP Response Object,containing the name of the template which is to be rendered,and its context,which contains all the local variables of this function
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
			##Creating a new Online Transaction Object/Row pertaining to the tax transaction just made
			p=Online_Transaction_dummy.objects.create(account_number_id=custac.account_number,amount_paid=amount)
			p.save()
			##Creating a new Tax transaction Object/Row pertaining to the tax transaction just made
			p1=Tax_transaction(customer_id_id=cid,account_number_id=accno,tax_type_id_id=ttid,transaction_id_id=p.transaction_id,date=now,amount_paid=amount,asses_year=assyear)
			p1.save()
			##Deducting appropriate money from the Customer Account
			custac.amount=custac.amount-float(amount)
			custac.save()
			return render_to_response('done.html',locals())
		else:
			##Saving the error so that it can be showed in the rendered HTML page

			error="Invalid PIN Entered.Try Again"
			return render_to_response('error.html',locals())
	else:
		return HttpResponse('Please enter Amount')


##This method/view is called when the customer wants to view all his Tax Transaction History
##@param request: This is the HTTP Request object,which is formed when we request for the starting page of our App.
##@return response:An HTTP Response Object,containing the name of the template which is to be rendered,and its context,which contains all the local variables of this function
def show(request):
		if 'accno' in request.GET and request.GET['accno']:
			##Getting the account object corresponding to the given account number in the request.GET dictionary
			try:
				account=Accounts_dummy.objects.get(account_number=request.GET['accno'])
			##Getting the Tax transaction object corresponding to the given account number
				alltax=Tax_transaction.objects.filter(account_number=account.account_number)
			except:
				error="Invalid Account Number.It Does not exists."
			return render_to_response('error.html',locals())
		else:
			return render_to_response('show.html')
		


















	
