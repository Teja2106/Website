from django.shortcuts import render
from django.views import View

class HomePage(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
            return render(request, self.template_name)

class Page2(View):
      template_name = "apt_booking.html"

      def get(self, request, *args, **kwargs):
            return render(request, self.template_name)