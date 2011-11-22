from django import forms

class ContactForm(forms.Form):
	customer_id=forms.IntegerField(primary_key=True)
	customer_name=forms.CharField(max_length=50)
	customer_age=forms.IntegerField()
	cust_street=forms.CharField(max_length=50)
	cust_city=forms.CharField(max_length=150)#to be added by digi
	cust_state=forms.CharField(max_length=150)
