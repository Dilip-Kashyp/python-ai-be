from app import ai_server

app = ai_server()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
