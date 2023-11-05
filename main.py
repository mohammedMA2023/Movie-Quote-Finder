from flask import *
def find(search,file):
    res = ""
    while True:
        search_2 = " " + search + " "
        search_3 = " " + search
        search_4 = search + " "
        print(f"{search.upper()} , {search.lower()} , {search.title()} , {search.capitalize()}")
        with open(file,"r") as file:
            for line in file:

                if search in line or search_2 in line or search_3 in line or search_4 in line or search.title() in line or search.upper() in line or search.capitalize() in line or search_2.title() in line or search_2.upper() in line or search_2.capitalize() in line or search_3.title() in line or search_3.upper() in line or search_3.capitalize() in line or search_4.title() in line or search_4.upper() in line or search_4.capitalize() in line:
                    res += line +"\n"
            break
    return res
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if 'search' in request.form:
            print('yes')
            entered_value = request.form["quote"]
            script = request.form["file"]
            return f"{find(entered_value,script)}"
        else:
            print("no")
            return 'Button was not clicked!'
    return render_template("quotes.html")

if __name__ == '__main__':
    app.run()

