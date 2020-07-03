from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


class EntryForm(forms.Form):
    title = forms.CharField(label="New Entry")
    content = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, entry):
    e = util.get_entry(entry)
    if e is None:
        return render(
            request, "encyclopedia/error.html", {"error": f"{entry} not found"}
        )

    return render(request, "encyclopedia/entry.html", {"entry": e, "name": entry})


def new(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            e = util.get_entry(title)
            if e is None:
                util.save_entry(title, content)
            else:
                return render(
                    request,
                    "encyclopedia/error.html",
                    {"error": f"Encyclopedia entry {title} already exists"},
                )

            # validate validate validate
            return HttpResponseRedirect(title)

    return render(request, "encyclopedia/new.html", {"form": EntryForm()})
