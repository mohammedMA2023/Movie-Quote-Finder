from itertools import product
from flask import *
temp = ""

def find(search,file):
    input_string = search
    res = ""
    # Split the input string into words
    words = input_string.split()

    # Generate variations by capitalizing or not capitalizing the first letter of each word
    case_variants = []

    for case_combination in product([True, False], repeat=len(words)):
        variant = ' '.join(
            [word.capitalize() if capitalize else word for word, capitalize in zip(words, case_combination)])
        case_variants.append(variant)
    print(case_variants)
    with open(file,"r") as file:
        for line in file:
                for variant in case_variants:
                    variant_2 = variant + " "
                    variant_3 = " " + variant
                    variant_4 = " " + variant + " "
                    print(f"V1, {variant}\n V2 {variant_2}, V3: {variant_3}\n V4: {variant_4}")
                    if variant in line or variant_2 in line or  variant_3 in line or variant_4 in line:

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