from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask basics", "completed": False},
    {"id": 2, "title": "Create a to-do form", "completed": False},
]

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head><title>Mini To-Do App</title></head>
  <body>
    <h1>My To-Do List</h1>
    <form action="/add" method="post">
      <input type="text" name="title" placeholder="New task">
      <button type="submit">Add</button>
    </form>
    <ul>
      {% for task in tasks %}
      <li>{{ task.title }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})
    return redirect(url_for("index"))


# TODO: add a route to mark tasks as complete


if __name__ == "__main__":
    app.run(debug=True)
