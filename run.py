import webbrowser
from app import app

if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=False)
    # app.run(debug=True) will cause the app to reload and relaunch every time changes are made
