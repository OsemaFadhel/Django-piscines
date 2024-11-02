import os
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from .forms import InputForm
##learn logging


# Create your views here.

def my_form(request):
	history = []

	# Read the existing history from the log file, if it exists
	if os.path.exists(settings.LOG_FILE_PATH):
		with open(settings.LOG_FILE_PATH, 'r') as log_file:
			for line in log_file:
				timestamp, text = line.strip().split(" - ", 1)
				history.append({'timestamp': timestamp, 'text': text})

	# Handle form submission
	if request.method == 'POST':
		form = InputForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text_input']
			timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
			entry = f"{timestamp} - {text}"

			# Append the new entry to the log file
			with open(settings.LOG_FILE_PATH, 'a') as log_file:
				log_file.write(entry + '\n')

			# Add the new entry to the in-memory history list
			history.append({'timestamp': timestamp, 'text': text})

	else:
		form = InputForm()

	return render(request, 'ex02/my_form.html', {'form': form, 'history': history})
