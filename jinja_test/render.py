from jinja2 import Environment, FileSystemLoader

# 1. Load the templates folder
env = Environment(loader=FileSystemLoader("templates"))

# 2. Load hello.html
template = env.get_template("hello.html")

# 3. Render with data
output = template.render(name="Jagapathi")

# 4. Save the result in an HTML file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(output)

print("Rendered HTML saved to output.html")
