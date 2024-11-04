from django.shortcuts import render

# Create your views here.
def generate_shades(color, count):
	"""Generate a list of shades for a given color."""
	shades = []
	step = 255 // (count + 1)
	for i in range(1, count + 1):
		if color == 'noir':
			shades.append(f'rgb({step * i}, {step * i}, {step * i})')  # Shades of gray
		elif color == 'rouge':
			shades.append(f'rgb({step * i}, 0, 0)')  # Shades of red
		elif color == 'bleu':
			shades.append(f'rgb(0, 0, {step * i})')  # Shades of blue
		elif color == 'vert':
			shades.append(f'rgb(0, {step * i}, 0)')  # Shades of green
	return shades



def index(request):
	colors = {
		'noir': generate_shades('noir', 50),
		'rouge': generate_shades('rouge', 50),
		'bleu': generate_shades('bleu', 50),
		'vert': generate_shades('vert', 50),
	}
	zipped_colors = zip(colors['noir'], colors['rouge'], colors['bleu'], colors['vert'])
	return render(request, 'index.html', {'zipped_colors': zipped_colors})
