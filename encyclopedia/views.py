from django.shortcuts import render

from . import util


"""
list_entries():
Returns a list of all names of encyclopedia entries.

save_entry(title, content):
Saves an encyclopedia entry, given its title and Markdown
content. If an existing entry with the same title already exists,
it is replaced.

get_entry(title):
Retrieves an encyclopedia entry by its title. If no such
entry exists, the function returns None.
"""


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, entry):
    e = util.get_entry(entry)
    print(e)
    if e is None:
        return render(request, "encyclopedia/error.html", {"entry": entry})

    return render(request, "encyclopedia/entry.html", {"entry": e, "name": entry})
