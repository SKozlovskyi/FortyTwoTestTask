__author__ = 'sergey'

from apps.hello.models import RequestCollect


class MiddlewareRC(object):

    if not RequestCollect.objects.all():
        current_req = RequestCollect(r_path='NULL', r_read_id=0)
    else:
        current_req = RequestCollect.objects.get(pk=len(RequestCollect.objects.all()))
    last_read_req_id = current_req.r_read_id

    def process_request(self, request):
        req_ = RequestCollect.objects.create(r_path=request.path,
                                             r_method = request.method,
                                             r_read_id=MiddlewareRC.last_read_req_id)
        MiddlewareRC.current_req = req_
        return None

    def process_template_response(self, request, response):
        if request.path == '/':
            count_of_unread_req = MiddlewareRC.current_req.pk - MiddlewareRC.last_read_req_id - 1
            new_title = str(count_of_unread_req)+' new requests '+response.context_data['title']
            if count_of_unread_req != 0:
                response.context_data['title'] = new_title
            MiddlewareRC.last_read_req_id = MiddlewareRC.current_req.pk
        return response
