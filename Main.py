
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = TextInput(
            text="0",
            font_size=40,
            readonly=True,
            halign="right",
            size_hint=(1, 0.25)
        )

        main.add_widget(self.display)

        buttons = [
            ["AC", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "00", "="]
        ]

        grid = GridLayout(
            cols=4,
            spacing=8
        )

        for row in buttons:
            for symbol in row:
                btn = Button(
                    text=symbol,
                    font_size=28
                )
                btn.bind(on_press=self.on_button_click)
                grid.add_widget(btn)

        main.add_widget(grid)
        return main

    def on_button_click(self, instance):
        value = instance.text

        if value == "AC":
            self.expression = ""

        elif value == "⌫":
            self.expression = self.expression[:-1]

        elif value == "=":
            try:
                result = eval(
                    self.expression,
                    {"__builtins__": {}},
                    {}
                )
                self.expression = str(result)
            except Exception:
                self.expression = "Error"

        elif value == "%":
            try:
                self.expression = str(
                    float(self.expression) / 100
                )
            except Exception:
                self.expression = "Error"

        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += value

        self.display.text = self.expression or "0"


if __name__ == "__main__":
    CalculatorApp().run()

