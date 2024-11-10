from kivy.config import Config 

Config.set('graphics', 'resizable', False)

from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.gridlayout import GridLayout

from kivymd.app import MDApp

from kivymd.uix.button import MDRaisedButton

from kivymd.uix.textfield import MDTextField

from kivy.metrics import dp

from kivy.uix.button import Button

from kivy.base import runTouchApp

from pprint import pprint 

from kivy.core.window import Window 

Window.size = (290, 250)

KV = '''

<CalculatorApp>:

    orientation: 'vertical'

    MDTextField:
        id: input_field
        hint_text: "Insira um número"
        helper_text_mode: "on_focus"
        input_filter: "float"
        text_color: "black"


    GridLayout:
        cols: 4
        spacing: dp(10)
    
        MDRaisedButton:

            text: "1"
            id: btn
            md_bg_color: "#edfff3"
            text_color: "black"
            on_press: app.on_number_press(1)

        MDRaisedButton:

            text: "2"
            md_bg_color: "#dcffe7"
            text_color: "black"
            on_press: app.on_number_press(2)

        MDRaisedButton:

            text: "3"
            md_bg_color: "#caffdb"
            text_color: "black"
            on_press: app.on_number_press(3)

        MDRaisedButton:

            text: "+"
            md_bg_color: "#b9ffcf"
            text_color: "black"
            on_press: app.on_operator_press("+")

        MDRaisedButton:

            text: "4"
            md_bg_color: "#ffebe8"
            text_color: "black"                       
            on_press: app.on_number_press(4)

        MDRaisedButton:

            text: "5"
            md_bg_color: "#ffd7d0"
            text_color: "black"
            on_press: app.on_number_press(5)

        MDRaisedButton:

            text: "6"
            md_bg_color: "#ffc3b9"
            text_color: "black"           
            on_press: app.on_number_press(6)

        MDRaisedButton:

            text: "-"
            md_bg_color: "#ffafa2"
            text_color: "black"
            on_press: app.on_operator_press("-")

        MDRaisedButton:

            text: "7"
            md_bg_color: "#feffd5"
            text_color: "black"           
            on_press: app.on_number_press(7)

        MDRaisedButton:

            text: "8"
            md_bg_color: "#fdffb3"
            text_color: "black"
            on_press: app.on_number_press(8)

        MDRaisedButton:

            text: "9"
            md_bg_color: "#fcff90"
            text_color: "black"           
            on_press: app.on_number_press(9)

        MDRaisedButton:

            text: "*"
            md_bg_color: "#fbff6e"
            text_color: "black"
            on_press: app.on_operator_press("*")

        MDRaisedButton:

            text: "C"
            md_bg_color: "#dfdff4"
            text_color: "black"
            on_press: app.clear_input()

        MDRaisedButton:

            text: "0"
            md_bg_color: "#d1d1ea"
            text_color: "black"
            on_press: app.on_number_press(0)

        MDRaisedButton:

            text: "="
            md_bg_color: "#c2c2df"
            text_color: "black"
            on_press: app.calculate_result()

        MDRaisedButton:

            text: "/"
            md_bg_color: "#b3b4d5"
            text_color: "black"
            on_press: app.on_operator_press("/")

'''

class CalculatorApp(BoxLayout):

    def on_number_press(self, number):

        current_text = self.ids.input_field.text
        new_text = f"{current_text}{number}"
        self.ids.input_field.text = new_text

    def on_operator_press(self, operator):

        current_text = self.ids.input_field.text
        new_text = f"{current_text} {operator}"
        self.ids.input_field.text = new_text

    def clear_input(self):

        self.ids.input_field.text = ""

    def calculate_result(self):

        try:

            result = eval(self.ids.input_field.text)

            self.ids.input_field.text = str(result)

        except Exception as e:

            self.ids.input_field.text = e

class CalculatorMDApp(MDApp):

    def build(self):

        return CalculatorApp()

    def on_number_press(self, number):

        self.root.on_number_press(number)

    def on_operator_press(self, operator):

        self.root.on_operator_press(operator)

    def clear_input(self):

        self.root.clear_input()

    def calculate_result(self):

        self.root.calculate_result()

if __name__ == '__main__':
    Builder.load_string(KV)

    CalculatorMDApp().run()