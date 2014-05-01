from django.shortcuts import render
from models import Portfolio
from django.utils.html import escape



def portfolio_base(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolio': portfolio})