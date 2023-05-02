import PyPDF2

# Define the variables you want to extract from the PDF file
name = ''
age = 0
address = ''

# Open the PDF file and extract the information you need
with open('example.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)
    text = page.extractText()
    # Use regular expressions to extract the information you need from the text
    # For example:
    # name = re.search(r'Name:\s*(.*)', text).group(1)
    # age = int(re.search(r'Age:\s*(\d+)', text).group(1))
    # address = re.search(r'Address:\s*(.*)', text).group(1)

# Create the HTML GUI using Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get the values submitted in the HTML form and update the variables
    name = request.form['name']
    age = int(request.form['age'])
    address = request.form['address']
    return render_template('result.html', name=name, age=age, address=address)

if __name__ == '__main__':
    app.run(debug=True)
