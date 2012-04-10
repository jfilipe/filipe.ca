import sys
import os

from flask import Flask, render_template
from flaskext.flatpages import FlatPages
from flask_frozen import Freezer

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


def by_date(works):
    return sorted(works, reverse=True, key=lambda p: p.meta['work_date'])


@app.route("/")
def index():
    return render_template('index.html', pages=by_date(pages))


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'work_detail.html')
    return render_template(template, page=page, pages=by_date(pages))


@app.url_defaults
def inject_version_number(endpoint, values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            version_number = int(os.stat(file_path).st_mtime)
            values.setdefault('_v', version_number)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8000)
