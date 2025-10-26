from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# HTML design using Flask's render_template_string
home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flask Student API</title>
  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      color: #333;
      text-align: center;
      padding: 50px;
    }
    h1 {
      color: #004aad;
      font-size: 2.5em;
    }
    .card {
      background: white;
      margin: 30px auto;
      padding: 20px;
      border-radius: 15px;
      width: 320px;
      box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    a {
      display: inline-block;
      margin-top: 20px;
      padding: 10px 20px;
      color: white;
      background: #004aad;
      border-radius: 8px;
      text-decoration: none;
      transition: 0.3s;
    }
    a:hover {
      background: #006eff;
    }
  </style>
</head>
<body>
  <h1>Welcome to My Flask API!</h1>
  <div class="card">
    <p>This API provides student information.</p>
    <p>Try clicking below to view a sample student record.</p>
    <a href="/student">View Student JSON</a>
  </div>
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
