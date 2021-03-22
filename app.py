# set FLASK_APP=app.py
# set FLASK_ENV=development
# python -m flask run --host=0.0.0.0

from flask import Flask
from flask import render_template
app = Flask(__name__)

from pynput.keyboard import Key, Controller
keyboard = Controller()

# import keyresponse
@app.route('/')
@app.route('/fnkey')
@app.route('/fnkey/<key>')
def fnkey(key=""):
    if key == "":
        pass
    elif key == "f1":
        keyboard.press(Key.f1)
    elif key == "f2":
        keyboard.press(Key.f2)
    elif key == "f3":
        keyboard.press(Key.f3)
    elif key == "f4":
        keyboard.press(Key.f4)
    elif key == "f5":
        keyboard.press(Key.f5)
    elif key == "f6":
        keyboard.press(Key.f6)
    elif key == "f7":
        keyboard.press(Key.f7)
    elif key == "f8":
        keyboard.press(Key.f8)
    elif key == "f9":
        keyboard.press(Key.f9)
    elif key == "f10":
        keyboard.press(Key.f10)
    elif key == "f11":
        keyboard.press(Key.f11)
    elif key == "f12":
        keyboard.press(Key.f12)
    elif key == "f13":
        keyboard.press(Key.f13)
    elif key == "f14":
        keyboard.press(Key.f14)
    elif key == "f15":
        keyboard.press(Key.f15)
    elif key == "f16":
        keyboard.press(Key.f16)
    elif key == "f17":
        keyboard.press(Key.f17)
    elif key == "f18":
        keyboard.press(Key.f18)
    elif key == "f19":
        keyboard.press(Key.f19)
    elif key == "f20":
        keyboard.press(Key.f20)
    elif key == "f21":
        keyboard.press(Key.f21)
    elif key == "f22":
        keyboard.press(Key.f22)
    elif key == "f23":
        keyboard.press(Key.f23)
    elif key == "f24":
        # max
        keyboard.press(Key.f24)
    return render_template('/fnkey/fnkey.html', name=key)


# import keyresponse
# https://www.autohotkey.com/docs/Hotkeys.htm
@app.route('/sckey')
@app.route('/sckey/<key>')
def sckey(key=""):
    if key == "":
        pass
    elif key[0] == "^":
        keyboard.press(Key.ctrl.value) #this would be for your key combination
        # keyboard.press(Key.cmd.value)
        keyboard.press(key[1]) # the letter
        keyboard.release(key[1])
        keyboard.release(Key.ctrl.value) #this would be for your key combination
        # keyboard.release(Key.cmd.value)
    # elif key == "^v":
    #     keyboard.press(Key.ctrl.value) #this would be for your key combination
    #     # keyboard.press(Key.cmd.value)
    #     keyboard.press('v')
    #     keyboard.release('v')
    #     keyboard.release(Key.ctrl.value) #this would be for your key combination
    #     # keyboard.release(Key.cmd.value)
    return render_template('/sckey/sckey.html', name=key)



# @app.route('/key/backspace')
# def backspace():
#     keyboard.press(Key.backspace)
#     return 'Hello, World!'

# if __name__ == 'main':
#     app.run(debug=True, host='0.0.0.0', port=8123)