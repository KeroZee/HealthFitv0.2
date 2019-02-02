from Scripts import app, db

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.debug = True
    app.run()

