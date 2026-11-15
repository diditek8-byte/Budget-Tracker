"""
Track your expenses
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BudgetTracker(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))


        heading_label = toga.Label(
            "My Budget",
            style=toga.style.Pack(
            font_size=17,
            font_weight="bold",
            margin_top=5,
            margin_left=10,
           ),
        )

        subtitle_label = toga.Label(
            "Monthly Income",
            style=toga.style.Pack(
            font_size=14,
            margin=10,
           ),
        )

        income_label = toga.Label(
            "Total Income",
            style=toga.style.Pack(
                font_size=15,
                direction="column",
                padding_left=20,
                padding_top=15,
            ),
        )
        self.income_input = toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                font_size=13,
                direction="column",
                width=75,
                height=30,
                padding_left=35,
                padding_top=25,
            ),
        )

        enter_income = toga.Label(
            "Enter you income...",
            style=toga.style.Pack(
                font_size=12,
                padding_top=20,
                padding_left=20,
            )
        )

        income_box = toga.Box(
            style=toga.style.Pack(
                direction="column",
                background_color="beige",
                height=150,
                margin_top=30,
                padding=10,
              ),
            )
        income_box.add(income_label)
        income_box.add(self.income_input)
        income_box.add(enter_income)


        expense_title=toga.Label(
            "Expenses",
            style=toga.style.Pack(
                font_size=14,
                margin=10,
            )
        )

        main_box.add(heading_label)
        main_box.add(subtitle_label)
        main_box.add(income_box)
        main_box.add(expense_title)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    

def main():
    return BudgetTracker()
    
