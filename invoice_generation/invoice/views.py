from django.shortcuts import render
from .forms import InvoiceForm
from .utils import generate_pdf


def generate_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            context = {
                'form': form.cleaned_data,
            }
            pdf = generate_pdf('invoice/invoice_template.html', context)
            return pdf
    else:
        form = InvoiceForm()
    context = {
        'form': form,
    }
    return render(request, 'invoice/invoice_form.html', context)
