from website import create_app

app = create_app()
app.secret_key = app.config['SECRET KEY']

if __name__ == '__main__':
    app.run(debug=True)

