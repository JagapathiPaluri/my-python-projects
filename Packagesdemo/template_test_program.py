from jinja2 import Template, FileSystemLoader, Environment

# Loading a template from a file (template.html)
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.html')

# Rendering the template with data
output = template.render(name='Alice')

# Output the rendered template
print(output)