from itertools import product
from flask import *
temp = ""

def find(search,file):
    res = ""
    input_string = search

    # Generate a list of tuples where each tuple contains a letter and its uppercase/lowercase representation.
    case_variants = [(c, c.upper()) if c.isalpha() else (c,) for c in input_string]

    # Generate all possible combinations of uppercase and lowercase for each letter.
    all_case_combinations = [''.join(combination) for combination in product(*case_variants)]


    with open(file,"r") as file:
        for line in file:
                for variant in all_case_combinations:

                    if  variant in line or " " + variant + " " in line or " " + variant in line or variant + " " in line:
                        res += line +"\n"

    return res
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if 'search' in request.form:
            print('yes')
            entered_value = request.form["quote"]
            script = request.form["file"]
            return render_template("result.html",res=find(entered_value,script))
        else:
            print("no")
            return 'Button was not clicked!'
    return render_template("quotes.html")

if __name__ == "__main__":
    app.run()