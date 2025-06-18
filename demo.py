from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<html>
    <head>
        <title>Calculator</title>
    </head>
    <body>
        <h2>Calculator</h2>
        <form method="POST">
            <input type="text" name="num1">
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="text" name="num2">
            <input type="submit" value="=">
        </form>
        <h3>Result: {{ result }}</h3>
    </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = 0  # default result
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        # No input validation or conversion
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
