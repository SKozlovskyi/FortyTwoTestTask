# -*- encoding: utf-8 -*-
from django.views.generic.base import TemplateView
from apps.hello.models import Person, RequestCollect


class MainPageView(TemplateView):

    template_name = "mainpage.html"

    def get_context_data(self, **kwargs):
        p = Person.objects.all()[0]
        rc = len(RequestCollect.objects.all())
        if rc > 10:
            request_list = RequestCollect.objects.all()[rc-10:rc+1]
        else:
            request_list = RequestCollect.objects.all()
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['title'] = 'Нello'
        context['firstname'] = p.first_name
        context['lastname'] = p.last_name
        context['birthdate'] = p.birth_date
        context['email'] = p.con_email
        context['jabber'] = p.con_jabbber
        context['skype'] = p.con_skype
        context['bio'] = p.bio
        context['other_contacts'] = p.con_other
        context['request_list'] = request_list[::-1]
        return context
