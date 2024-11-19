from flask import Flask, render_template, request, redirect, url_for

fake_db = [
    {
        'id': 1,
        'title': 'Помити посуд',
        'completed': False,
    },
    {
        'id': 2,
        'title': 'Зробити домашнє завдання',
        'completed': True,
    },
    {
        'id': 3,
        'title': 'Погладити кота',
        'completed': False,
    },
    {
        'id': 4,
        'title': 'Вийти на прогулянку',
        'completed': True,
    },
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html", todo_list=fake_db)


@app.route("/add", methods=["POST"])
def create_todo():
    title = request.form.get("title", "")
    fake_db.append({
        'id': get_last_todo_id(),
        'title': title,
        'completed': False,
    })
    return redirect(url_for("home"))


def get_last_todo_id():
    if len(fake_db) > 0:
        return max(todo["id"] for todo in fake_db) + 1
    else:
        return 1


if __name__ == "__main__":
    app.run()