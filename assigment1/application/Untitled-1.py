@app.route("/get_todos")
def get_todos():
    instructors = []
    for instr in db.instructor.find().sort("ins_name", -1):
        instr["_id"] = str(instr["_id"])
        # instr["date_created"] = instr["date_created"].strftime("%b %d %Y %H:%M:%S")
        instructors.append(instr)

    return render_template("view_todos.html", instructors = instructors)
     {% for instr in instructors %}
        
        <div class="card p-1 m-3">
            <div class="card-body">
                <p class="card-text">{{ instr.ins_id }}</p>
                <p class="card-text text-muted">{{ instr.ins_name }}</p>
                <a href="{{ url_for('update_todo', id = todo._id) }}" class="btn btn-info btn-sm">Update</a>
                <a href="{{ url_for('delete_todo', id = todo._id) }}" class="btn btn-outline-danger btn-sm">Delete</a>
            </div>
        </div>
    {% endfor %}