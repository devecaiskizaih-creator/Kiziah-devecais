from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# HTML page with form and modern design
home_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Student Info Form | Flask API</title>
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      color: #333;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .card {
      background: white;
      padding: 40px;
      border-radius: 15px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
      width: 350px;
      text-align: center;
    }
    h1 {
      color: #004aad;
      margin-bottom: 20px;
    }
    input[type="text"], input[type="number"] {
      width: 90%;
      padding: 10px;
      margin: 8px 0;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 1em;
    }
    button {
      background: #004aad;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 1em;
      transition: 0.3s;
      margin-top: 10px;
    }
    button:hover {
      background: #007bff;
    }
    footer {
      position: fixed;
      bottom: 10px;
      font-size: 0.9em;
      color: #222;
      text-align: center;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Student Info Form</h1>
    <form action="/student" method="POST">
      <input type="text" name="name" placeholder="Enter Name" required><br>
      <input type="number" name="grade" placeholder="Enter Grade" required><br>
      <input type="text" name="section" placeholder="Enter Section" required><br>
      <button type="submit">Submit</button>
    </form>
  </div>
  <footer>© 2025 Flask Student API | Designed by You</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_page)

@app.route('/student', methods=['GET', 'POST'])
def get_student():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        grade = request.form.get('grade')
        section = request.form.get('section')

        # Return as JSON
        return jsonify({
            "name": name,
            "grade": grade,
            "section": section
        })
    else:
        # Default sample data for GET requests
        return jsonify({
            "name": "Your Name",
            "grade": 10,
            "section": "Zechariah"
        })

if __name__ == '__main__':
    app.run(debug=True)
