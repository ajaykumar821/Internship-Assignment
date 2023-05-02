from django import forms

class InvoiceForm(forms.Form):
    invoice_number = forms.CharField(max_length=50)
    invoice_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    seller_name = forms.CharField(max_length=100)
    seller_phone = forms.CharField(max_length=20)
    seller_address = forms.CharField(widget=forms.Textarea)
    
    buyer_name = forms.CharField(max_length=100)
    buyer_phone = forms.CharField(max_length=20)
    buyer_address = forms.CharField(widget=forms.Textarea)

    product = forms.CharField(max_length=100)
    quantity = forms.IntegerField(min_value=0)
    amount = forms.IntegerField(min_value=0)
    
    def calculate_total(self):
        total = 0
        for item in self.items.all():
            total += item.amount * item.quantity
        return total