# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'message' not in request.session:
		request.session['message'] = ''
	return render(request, 'golds/index.html')

def farm(request):
	add = random.randrange(10,21)
	request.session['gold'] += add
	request.session['message'] += 'Earned ' + str(add) + ' golds from the farm' + datetime.now().strftime('%Y-%m-%d %I:%M %p') + '\n'
	request.session['split'] = request.session['message'].split('\n')
	return redirect('/')

def cave(request):
	add = random.randrange(5,11)
	request.session['gold'] += add
	request.session['message'] += 'Earned ' + str(add) + ' golds from the cave' + datetime.now().strftime('%Y-%m-%d %I:%M %p') + '\n'
	request.session['split'] = request.session['message'].split('\n')
	return redirect('/')

def house(request):
	add = random.randrange(2,6)
	request.session['gold'] += add
	request.session['message'] += 'Earned ' + str(add) + ' golds from the house' + datetime.now().strftime('%Y-%m-%d %I:%M %p') + '\n'
	request.session['split'] = request.session['message'].split('\n')
	return redirect('/')

def casino(request):
	add = random.randrange(-50,51)
	request.session['gold'] += add
	if add > 0:
		request.session['message'] += 'Earned ' + str(add) + ' golds from the casino' + datetime.now().strftime('%Y-%m-%d %I:%M %p') + '\n'
		request.session['split'] = request.session['message'].split('\n')
	else:
		request.session['message'] += 'Lost ' + str(abs(add)) + ' golds from the casino' + datetime.now().strftime('%Y-%m-%d %I:%M %p') + '\n'
		request.session['split'] = request.session['message'].split('\n')
	return redirect('/')