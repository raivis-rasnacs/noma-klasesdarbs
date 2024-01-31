from __init__ import create_app

app = create_app()

from views.produkti_views import (
    produkti
)

# all routes
app.add_url_rule('/', view_func=produkti)

if __name__ == "__main__":
    if app.config["FLASK_ENV"] == "development":
        app.run(debug=True)