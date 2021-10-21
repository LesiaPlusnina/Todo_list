
def deleteCompleted(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
