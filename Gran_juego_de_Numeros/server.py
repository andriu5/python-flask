import random
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)

app.secret_key = "codingDojo!"

@app.route('/')
def great_number_game():
    guess_number = random.randrange(1,101)
    if 'num' not in session:
        session['num']=guess_number
        #session['num']=22
    return render_template("index.html", num=session['num'])

@app.route("/check", methods=["POST"] )
def check_input_value():
    messages = [{"invalid_input":"Please provide a number between 1 and 100!"}]
    input_value = request.form.get('input_guess', type=int)
    print("El tipo de la entrada es: ", type(input_value))
    print("El valor de la entrada es: ", input_value)
    if input_value != None:
        if input_value > 0 and input_value <= 100:
            random_guess = session['num']
            print("El numero es:", random_guess)
            box_color = ""
            box_text = ""
            reset_button = ""
            box_text2=""
            
            if input_value == random_guess:
                box_color = "green"
                box_text = "You've Guessed the number!"
                return render_template("index.html",input_value =input_value, box_color=box_color, box_guess=box_text, reset_button=reset_button)
            if input_value > random_guess:
                box_color = "red"
                box_text = "your guess is to high! Try again!"
                return render_template("index.html",box_color=box_color, box_guess=box_text, reset_button=reset_button)
            if input_value < random_guess:
                box_color = "blue"
                box_text = "your guess is to low! Try again!"
                return render_template("index.html",box_color=box_color, box_guess=box_text)
        else:
            # session['messages'] = messages
            return render_template("index.html", messages=messages)
            #return redirect(url_for('great_number_game', messages=messages))
    else:
        #return redirect(url_for('great_number_game'))
        #return redirect('/')
        return render_template("index.html", messages=messages)

@app.route('/reset_session', methods=['POST'])
def reset():
    print("El numero es:", session['num'])
    #session.pop ('num')          # borra una clave específica
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)