from itertools import product
from flask import *

def find(search, file):
    input_string = search
    res = ""

    words = input_string.split()
    case_variants = []
    for case_combination in product([True, False], repeat=len(words)):
        variant = ' '.join(
            [word.capitalize() if capitalize else word for word, capitalize in zip(words, case_combination)])
        case_variants.append(variant)

    # Generate variations where individual words are fully capitalized
    word_capitalization_variants = []
    for word_combination in product([True, False], repeat=len(words)):
        variant = ' '.join([word.upper() if caps else word for word, caps in zip(words, word_combination)])
        word_capitalization_variants.append(variant)

    # Combine both sets of variations
    all_variants = case_variants + word_capitalization_variants

    for variant in all_variants:
        print(variant)
        for line in file:
            if variant in line:
                print(f"Found: {variant} in line: {line}")

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