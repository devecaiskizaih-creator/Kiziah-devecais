from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# HTML Template with a better design
home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flask Student API</title>
  <style>
    body {
      font-family: 'Poppins', Arial, sans-serif;
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      color: #333;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .container {
      background: #fff;
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      text-align: center;
      max-width: 400px;
    }
    h1 {
      color: #004aad;
      font-size: 2em;
      margin-bottom: 10px;
    }
    p {
      font-size: 1.1em;
      color: #555;
      margin-bottom: 20px;
    }
    a {
      text-decoration: none;
      background: #004aad;
      color: white;
      padding: 10px 20px;
      border-radius: 8px;
      transition: 0.3s;
    }
    a:hover {
      background: #007bff;
    }
    footer {
      position: fixed;
      bottom: 10px;
      font-size: 0.9em;
      color: #222;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to My Flask API</h1>
    <p>This is an enhanced version with a clean and modern design.</p>
    <a href="/student">View Student JSON</a>
  </div>
  <footer>© 2025 Flask Student API | Designed by You</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_page)

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == '__main__':
    app.run(debug=True)
