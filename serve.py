"""Local dev server with live reload.

Serves the site at http://127.0.0.1:8000 and auto-refreshes the browser
whenever a source file changes.

Usage:
    python serve.py

Requires:  pip install livereload
"""
from livereload import Server

server = Server()

# Watch everything that affects the page; a change to any of these
# triggers an automatic browser reload.
server.watch("index.html")
server.watch("site.webmanifest")
server.watch("assets/")
server.watch("fonts/")

server.serve(root=".", host="127.0.0.1", port=8000, open_url_delay=1)
