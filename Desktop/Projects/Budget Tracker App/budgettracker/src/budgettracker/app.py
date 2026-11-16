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
                margin_left=20,
                margin_top=15,
            ),
        )
        self.income_input = toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                font_size=13,
                direction="column",
                width=75,
                height=30,
                margin_left=35,
                margin_top=25,
            ),
        )

        enter_income = toga.Label(
            "Enter you income...",
            style=toga.style.Pack(
                font_size=12,
                margin_top=20,
                margin_left=20,
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
                font_size=16,
                margin_top=6,
                text_align="center",
            ),
        )

        rent_label=toga.Label(
            "Rent",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
            ),
        )

        rent_input=toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                height=30,
                margin_left=25,
                margin_top=25,
                font_size=13,
            ),
        )

        rent_box= toga.Box(
            style=toga.style.Pack(
                direction="column",
                background_color="beige",
                height=150,
                width=120,
                margin=10,
                flex=1,
            ),
        )

        rent_box.add(rent_label)
        rent_box.add(rent_input)

        electricity_label=toga.Label(
            "Electricity",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
            ),
        )

        electricity_input=toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_left=25,
                margin_top=25,
            ),
        )

        electricity_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="beige",
                flex=1,
            ),
        )

        electricity_box.add(electricity_label)
        electricity_box.add(electricity_input)

        gas_label=toga.Label(
            "Gas",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center"
            ),
        )

        gas_input=toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_left=25,
                margin_top=25,
            ),
        )

        gas_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="beige",
                flex=1,
            ),
        )

        gas_box.add(gas_label)
        gas_box.add(gas_input)

        water_label=toga.Label(
            "Water",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
            ),
        )

        water_input=toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin=25,
            ),
        )

        water_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="beige",
                flex=1,
            ),
        )

        water_box.add(water_label)
        water_box.add(water_input)


        expense_container = toga.Box(
            style=toga.style.Pack(
                direction="row",
            ),
        )
        
        expense_container.add(rent_box)
        expense_container.add(electricity_box)
        expense_container.add(gas_box)
        expense_container.add(water_box)


        internet_label=toga.Label(
            "Internet",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
            ),
        )

        internet_input=toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                font_size=13,
                width=75,
                margin=25,
            ),
        )

        internet_box=toga.Box(
            style=toga.style.Pack(
                background_color="beige",
                width=120,
                height=150,
                direction="column",
                margin=10,
                flex=1,
            ),
        )
        
        internet_box.add(internet_label)
        internet_box.add(internet_input)

        grocery_label=toga.Label(
            "Groceries",
            style=toga.style.Pack(
                font_size=15,
                text_align="center",
                margin_top=15,
            ),
        )

        grocery_input = toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                font_size=13,
                width=75,
                margin=25,
            ),
        )

        grocery_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="beige",
                flex=1,
            ),
        )

        grocery_box.add(grocery_label)
        grocery_box.add(grocery_input)

        credit_label = toga.Label(
            "Credit",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
            ),
        )

        credit_input = toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin=25,
            ),
        )

        credit_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                background_color="beige",
                flex=1,
                direction="column",
                margin=10,
            ),
        )

        credit_box.add(credit_label)
        credit_box.add(credit_input)

        commuting_label = toga.Label(
            "Commuting",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                margin_left=10,
            ),
        )

        commuting_input = toga.TextInput(
            value="$0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin=25,
            ),
        )

        commuting_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                background_color="beige",
                flex=1,
                margin=10,
            ),
        )

        commuting_box.add(commuting_label)
        commuting_box.add(commuting_input)

        
        expense_container2 = toga.Box(
            style=toga.style.Pack(
                direction="row",
            )
        )

        expense_container2.add(internet_box)
        expense_container2.add(grocery_box)
        expense_container2.add(credit_box)
        expense_container2.add(commuting_box)

        expense_widget = toga.Box(
            style=toga.style.Pack(
                direction="column",
                alignment="center",
            ),
        )

        expense_widget.add(expense_container)
        expense_widget.add(expense_container2)

        category_button = toga.Button(
            "+",
            style=toga.style.Pack(
                text_align="center",
                margin=10,
                font_size=14,
                background_color="beige",
            ),
        )

        category_label = toga.Label(
            "Add Category",
            style=toga.style.Pack(
            font_size=15,
            text_align="center",
            margin=5,
            ),
        )

        category_box = toga.Box(
            style=toga.style.Pack(
                margin_top=25,
                background_color="beige",
                direction="column",
                height=100,
            ),
        )

        category_box.add(category_button)
        category_box.add(category_label)


        save_button = toga.Button(
            "Save Budget",
            style=toga.style.Pack(
                font_size=15,
                margin=10
            ),
        )
        
        main_box.add(heading_label)
        main_box.add(subtitle_label)
        main_box.add(income_box)
        main_box.add(expense_title)
        main_box.add(expense_widget)
        main_box.add(category_box)
        main_box.add(save_button)
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    

def main():
    return BudgetTracker()
    
