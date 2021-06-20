from django.db.models.query_utils import PathInfo
from django.shortcuts import render,HttpResponse
from django.views.generic import  View

from pdfGeneration.models import SupportTicket


# Create your views here.
#pdf genarator start from here
from pdf.utils import render_to_pdf
from django.template.loader import get_template

class GenerateInvoice(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            order_db = SupportTicket.objects.get(id = pk)     #you can filter using order_id as well
            
        except:
            return HttpResponse("505 Not Found")
        data = {
            'order_id': order_db.user.pk,
            'user_email': order_db.email,
            'date': str(order_db.created),
            # 'name': order_db.user,
            'order': order_db,
            'amount': order_db.assigned_to,
        }
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

        # force download
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Invoice_%s.pdf" %(data['order_id'])
        #     content = "inline; filename='%s'" %(filename)
        #     #download = request.GET.get("download")
        #     #if download:
        #     content = "attachment; filename=%s" %(filename)
        #     response['Content-Disposition'] = content
        #     return response
        # return HttpResponse("Not found")