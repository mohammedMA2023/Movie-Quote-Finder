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

    with open(file,'r') as f:
        for line in f:

            for variant in all_variants:
                variant_2 = variant + " "
                variant_3 = " " + variant
                variant_4 = " " + variant + " "

                if variant in line or variant_2 in line or variant_3 in line or variant_4 in line or variant in line.lower() or variant_2 in line.lower() or variant_3 in line.lower() or variant_4 in line.lower() or variant in line.upper() or variant_2 in line.upper() or variant_3 in line.upper() or variant_4 in line.upper() or variant in line.title() or variant_2 in line.title() or variant_3 in line.title() or variant_4 in line.title() or variant in line.capitalize() or variant_2 in line.capitalize() or variant_3 in line.capitalize() or variant_4 in line.capitalize():
                    res += line + "\n"
    return res if res else  "Not Found"

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if 'search' in request.form:

            entered_value = request.form["quote"]
            script = request.form["file"]
            return render_template("result.html",res=find(entered_value,script))
        else:
            print("no")
            return 'Button was not clicked!'
    return render_template("quotes.html")

if __name__ == "__main__":
    app.run(host="192.168.0.203",port=443)