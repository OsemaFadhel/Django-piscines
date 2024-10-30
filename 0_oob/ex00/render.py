import sys, os, re

settings_module = __import__('settings')

# checking if file ends with .template and if it exists
def check_file(file):
	if not file.endswith('.template'):
		raise Exception("File must end with .template")
	if not os.path.exists(file):
		raise Exception("File does not exist")

def replacer(content):
	for key in dir(settings_module):
		if not key.startswith('__'):
			value = getattr(settings_module, key)
			content = content.replace(f'{{{{ {key} }}}}', str(value))
	return content

def run(template):
	with open(template, 'r') as f:
		content = f.read()

	rendered_content = replacer(content)
	output_file = template.replace('.template', '.html')
	with open(output_file, 'w') as f:
		f.write(rendered_content)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: python render.py <file.template>")
		sys.exit(1)
	template = sys.argv[1]
	try:
		check_file(template)
		run(template)
	except Exception as e:
		print(e)
		sys.exit(1)
