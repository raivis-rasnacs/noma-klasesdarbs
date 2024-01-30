from __init__ import create_app

app = create_app()

if __name__ == "__main__":
    if app.config["FLASK_ENV"] == "development":
        app.run(debug=True)