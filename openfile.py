import webbrowser#pip install webbrowser
import os

def open_webfunc(name, path):
    query = query.replace('open ','').strip().lower()
    print(query)
    if query == name:
        webbrowser.open_new_tab(path)