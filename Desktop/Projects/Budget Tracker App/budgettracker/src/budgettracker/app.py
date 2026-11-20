"""
Track your expenses
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import json


class BudgetTracker(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        main_box.style.background_color = "#775e54"
    
        heading_label = toga.Label(
            "My Budget",
            style=toga.style.Pack(
            font_size=25,
            font_weight="bold",
            margin_top=5,
            margin_left=10,
            color="#e6b3b8",
            text_align="center",
           ),
        )

        subtitle_label = toga.Label(
            "Monthly Income",
            style=toga.style.Pack(
            font_size=16,
            margin=10,
            text_align="center",
           ),
        )

        income_label = toga.Label(
            "Total Income",
            style=toga.style.Pack(
                font_size=15,
                direction="column",
                margin_left=20,
                margin_top=15,
                text_align="center",
            ),
        )
        self.income_input = toga.NumberInput(
            value=0.00,
            style=toga.style.Pack(
                font_size=13,
                direction="column",
                alignment="center",
                width=100,
                height=30,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency =toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        income_line = toga.Box(
            direction=ROW
        )

        income_line.add(self.currency)
        income_line.add(self.income_input)
        

        enter_income = toga.Label(
            "Enter you income...",
            style=toga.style.Pack(
                font_size=12,
                margin_top=20,
                margin_left=20,
                color="#b15b64",
                text_align="center",
            )
        )

        income_box = toga.Box(
            style=toga.style.Pack(
                direction="column",
                background_color="#f3eeec",
                color="#b15b64",
                height=150,
                margin_top=30,
                padding=10,
                alignment="center",
              ),
            )
        income_box.add(subtitle_label)
        income_box.add(income_label)
        income_box.add(income_line)
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
                color="#b15b64",
            ),
        )

        self.rent_input=toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                width=75,
                height=30,
                margin_left=5,
                margin_top=25,
                font_size=13,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            )
        )

        rent_line = toga.Box(
            style=toga.style.Pack(
                direction="row"
            )
        )

        rent_line.add(self.currency)
        rent_line.add(self.rent_input)

        rent_box= toga.Box(
            style=toga.style.Pack(
                direction="column",
                background_color="#f3eeec",
                height=150,
                width=120,
                margin=10,
                flex=1,
            ),
        )

        rent_box.add(rent_label)
        rent_box.add(rent_line)

        electricity_label=toga.Label(
            "Electricity",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
                color="#b15b64",
            ),
        )

        self.electricity_input=toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_left=5,
                margin_top=25,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            )
        )

        electricity_line = toga.Box(
            direction=ROW
        )

        electricity_line.add(self.currency)
        electricity_line.add(self.electricity_input)


        electricity_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="#f3eeec",
                flex=1,
                color="#b15b64"
            ),
        )

        electricity_box.add(electricity_label)
        electricity_box.add(electricity_line)
        

        gas_label=toga.Label(
            "Gas",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
                color="#b15b64",
            ),
        )

        self.gas_input=toga.NumberInput(
            value="0.00",
            step=10,
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_left=5,
                margin_top=25,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            )
        )

        gas_line = toga.Box(
            direction=ROW
        )

        gas_line.add(self.currency)
        gas_line.add(self.gas_input)

        gas_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="#f3eeec",
                flex=1,
                color="#b15b64"
            ),
        )

        gas_box.add(gas_label)
        gas_box.add(gas_line)
       

        water_label=toga.Label(
            "Water",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
                color="#b15b64",
            ),
        )

        self.water_input=toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        water_line = toga.Box(
            direction=ROW
        )

        water_line.add(self.currency)
        water_line.add(self.water_input)

        water_box=toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="#f3eeec",
                flex=1,
                color="#b15b64",
            ),
        )

        water_box.add(water_label)
        water_box.add(water_line)
        

        self.expense_container = toga.Box(
            style=toga.style.Pack(
                direction="row",
            ),
        )
        
        self.expense_container.add(rent_box)
        self.expense_container.add(electricity_box)
        self.expense_container.add(gas_box)
        self.expense_container.add(water_box)


        internet_label=toga.Label(
            "Internet",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
                color="#b15b64",
            ),
        )

        self.internet_input=toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                font_size=13,
                width=75,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        internet_line = toga.Box(
            direction=ROW
        )

        internet_line.add(self.currency)
        internet_line.add(self.internet_input)

        internet_box=toga.Box(
            style=toga.style.Pack(
                background_color="#f3eeec",
                width=120,
                height=150,
                direction="column",
                margin=10,
                flex=1,
            ),
        )
        
        internet_box.add(internet_label)
        internet_box.add(internet_line)
        

        grocery_label=toga.Label(
            "Groceries",
            style=toga.style.Pack(
                font_size=15,
                text_align="center",
                margin_top=15,
                color="#b15b64",
            ),
        )

        self.grocery_input = toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                font_size=13,
                width=75,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        grocery_line = toga.Box(
            direction=ROW
        )

        grocery_line.add(self.currency)
        grocery_line.add(self.grocery_input)

        grocery_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                margin=10,
                background_color="#f3eeec",
                flex=1,
            ),
        )

        grocery_box.add(grocery_label)
        grocery_box.add(grocery_line)
        

        credit_label = toga.Label(
            "Credit",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                text_align="center",
                color="#b15b64",
            ),
        )

        self.credit_input = toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency= toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        credit_line = toga.Box(
            direction=ROW
        )

        credit_line.add(self.currency)
        credit_line.add(self.credit_input)

        credit_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                background_color="#f3eeec",
                flex=1,
                direction="column",
                margin=10,
            ),
        )

        credit_box.add(credit_label)
        credit_box.add(credit_line)


        commuting_label = toga.Label(
            "Commuting",
            style=toga.style.Pack(
                font_size=15,
                margin_top=15,
                margin_left=10,
                color="#b15b64",
            ),
        )

        self.commuting_input = toga.NumberInput(
            value=0.00,
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_top=25,
                margin_left=5,
            ),
        )

        self.currency =toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_top=27,
                margin_left=10,
            ),
        )

        commuting_line = toga.Box(
            direction=ROW
        )

        commuting_line.add(self.currency)
        commuting_line.add(self.commuting_input)

        commuting_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                background_color="#f3eeec",
                flex=1,
                margin=10,
            ),
        )

        commuting_box.add(commuting_label)
        commuting_box.add(commuting_line)

        
        self.expense_container2 = toga.Box(
            style=toga.style.Pack(
                direction="row",
            )
        )

        self.expense_container2.add(internet_box)
        self.expense_container2.add(grocery_box)
        self.expense_container2.add(credit_box)
        self.expense_container2.add(commuting_box)

        self.expense_widget = toga.Box(
            style=toga.style.Pack(
                direction="column",
                alignment="center",
            ),
        )

        self.expense_widget.add(self.expense_container)
        self.expense_widget.add(self.expense_container2)

        self.expense_container3 = toga.Box(
            style=toga.style.Pack(
                direction="column",
                alignment="center",
                margin_right=420,
            )
        )

        category_button = toga.Button(
            "+",
            on_press=self.add_category,
            style=toga.style.Pack(
                text_align="center",
                margin=10,
                font_size=20,
                background_color="#f3eeec",
            ),
        )

        category_label = toga.Label(
            "Add Category",
            style=toga.style.Pack(
            font_size=15,
            text_align="center",
            margin=5,
            color="#b15b64",
            ),
        )

        category_box = toga.Box(
            style=toga.style.Pack(
                margin_top=25,
                background_color="#f3eeec",
                direction="column",
                height=100,
            ),
        )

        category_box.add(category_button)
        category_box.add(category_label)


        save_button = toga.Button(
            "Save Budget",
            on_press=self.save_budget,
            style=toga.style.Pack(
                font_size=15,
                margin=10,
                background_color="#f3eeec",
            ),
        )

        overview_label = toga.Label(
            "Overview",
            style=toga.style.Pack(
                margin_left=10,
                font_size=23,
                color="#e6b3b8",
                margin_top=20,
            ),
        )

        earned_label = toga.Label(
            "Earned:",
            style=toga.style.Pack(
                font_size=17,
                gap=10,
                margin_top=7,
            ),
        )

        self.earned_currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=17,
                margin_left=3,
                margin_top=5,
            )
        )

        self.earned_input = toga.TextInput(
            value="0.00",
            readonly=True,
            style=toga.style.Pack(
                width=75,
                margin_top=5,
                font_size=13,
            ),
        )

        spent_label = toga.Label(
            "Spent:",
            style=toga.style.Pack(
                font_size=17,
                margin_top=5,
                gap=10,

            ),
        )

        self.spent_currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=17,
                margin_left=3,
                margin_top=5,
            )
        )

        self.spent_input = toga.TextInput(
            value="0.00",
            readonly=True,
            style=toga.style.Pack(
                width=75,
                margin_top=5,
                font_size=13,
                
            ),
        )

        remaining_label = toga.Label(
            "Remaining:",
            style=toga.style.Pack(
                font_size=17,
                margin_top=5,
                gap=10,
                
            ),
        )

        self.remaining_currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=17,
                margin_left=3,
                margin_top=5,
            )
        )

        self.remaining_input = toga.TextInput(
            value="0.00",
            readonly=True,
            style=toga.style.Pack(
                width=75,
                margin_top=5,
                font_size=13,
                margin_left=3,
            ),
        )

        overview_box = toga.Box(
            style=toga.style.Pack(
                direction="row",
                width=500,
                margin_left=20,
                margin_top=15,
                gap=15,
                margin_bottom=10,
            ),
        )

        overview_box.add(earned_label)
        overview_box.add(self.earned_currency)
        overview_box.add(self.earned_input)
        overview_box.add(spent_label)
        overview_box.add(self.spent_currency)
        overview_box.add(self.spent_input)
        overview_box.add(remaining_label)
        overview_box.add(self.remaining_currency)
        overview_box.add(self.remaining_input)


        main_box.add(heading_label)
        main_box.add(subtitle_label)
        main_box.add(income_box)
        main_box.add(expense_title)
        main_box.add(self.expense_widget)
        main_box.add(category_box)
        main_box.add(save_button)
        main_box.add(overview_label)
        main_box.add(overview_box)

        

        self.main_window = toga.MainWindow(title=self.formal_name)

        self.main_window.show()

        scroll_content = toga.Box(
            direction=COLUMN,
        )
                
        scroll = toga.ScrollContainer(
            horizontal=False,
        )
        
        scroll.content = scroll_content
        scroll.content = main_box
        self.main_window.content = scroll


        self.load_budget()


    custom_dict = {}
    budget_dict = {}

    
    def add_category(self, widget):
        self.add_expense_label = toga.TextInput(
            placeholder="Expense",
            style=toga.style.Pack(
                font_size=14,
                margin_top=15,
                margin_left=10,
                width=100,
            ),
        )
        self.add_expense_input = toga.NumberInput(
            value="0.00",
            style=toga.style.Pack(
                width=75,
                font_size=13,
                margin_top=25,
                margin_left=5,
            ),
        )
        self.currency = toga.Label(
            "$",
            style=toga.style.Pack(
                font_size=16,
                margin_left=10,
                margin_top=27,
            )
        )
        add_expense_line = toga.Box(
                direction=ROW
        )
        add_expense_line.add(self.currency)
        add_expense_line.add(self.add_expense_input)
        self.add_expense_box = toga.Box(
            style=toga.style.Pack(
                width=120,
                height=150,
                direction="column",
                background_color="#f3eeec",
                flex=1,
                margin=10,
            )
        )
        self.add_expense_box.add(self.add_expense_label)
        self.add_expense_box.add(add_expense_line)
    
        self.expense_container3 = toga.Box(
            style=toga.style.Pack(
                direction="column",
                alignment="center",
                margin_right=420,
            )
        )
    
        self.expense_container3.add(self.add_expense_box)
        self.expense_widget.add(self.expense_container3)


    def save_budget(self, widget):
        data_file = self.paths.data / "data.json"
        
        self.budget_dict = {
            "income": str(self.income_input.value),
            "electricity": str(self.electricity_input.value),
            "rent": str(self.rent_input.value),
            "gas": str(self.gas_input.value),
            "water": str(self.water_input.value),
            "internet": str(self.internet_input.value),
            "grocery": str(self.grocery_input.value),
            "credit": str(self.credit_input.value),
            "commuting": str(self.commuting_input.value),
        }

        self.expense = self.add_expense_label.value
        self.value = str(self.add_expense_input.value)
        print("Input type:", type(self.value))
        self.custom_dict[self.expense] = str(self.value)
        
        data = {
            "budget": self.budget_dict,
            "custom": self.custom_dict,
        }
        

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

        with open(data_file, "r") as file:
            data = json.load(file)
    
        self.earned_input.value = str(self.budget_dict["income"])

        total_budget = float(self.budget_dict["rent"]) + float(self.budget_dict["electricity"]) + float(self.budget_dict["gas"]) + float(self.budget_dict["water"]) + float(self.budget_dict["internet"]) + float(self.budget_dict["grocery"]) + float(self.budget_dict["credit"]) + float(self.budget_dict["commuting"])

        self.spent_input.value = total_budget

        remaining = float(self.budget_dict["income"]) - total_budget
        self.remaining_input.value = remaining

       
        with open(data_file, "w") as file:
          json.dump(data, file, indent=4)
          




    def load_budget(self):
        data_file = self.paths.data / "data.json"
        
        with open(data_file, "r") as file:
            data = json.load(file)
            self.budget_dict = data["budget"]
            self.custom_dict = data["custom"]
        if self.budget_dict:
          self.income_input.value = self.budget_dict["income"]
          self.rent_input.value = self.budget_dict["rent"]
          self.electricity_input.value = self.budget_dict["electricity"]
          self.gas_input.value = self.budget_dict["gas"]
          self.water_input.value = self.budget_dict["water"]
          self.internet_input.value = self.budget_dict["internet"]
          self.grocery_input.value = self.budget_dict["grocery"]
          self.credit_input.value = self.budget_dict["credit"]
          self.commuting_input.value = self.budget_dict["commuting"]
          self.earned_input.value = self.budget_dict["income"]

          total_budget = float(self.budget_dict["rent"]) + float(self.budget_dict["electricity"]) + float(self.budget_dict["gas"]) + float(self.budget_dict["water"]) + float(self.budget_dict["internet"]) + float(self.budget_dict["grocery"]) + float(self.budget_dict["credit"]) + float(self.budget_dict["commuting"])
          self.spent_input.value = total_budget

          remaining = float(self.budget_dict["income"]) - total_budget
          self.remaining_input.value = remaining


        if self.custom_dict:
            for expense, value in self.custom_dict.items():
                self.saved_expense_label = toga.Label(
                    "",
                    style=toga.style.Pack(
                        font_size=15,
                        margin_top=15,
                        text_align="center",
                        color="#b15b64",
                        width=100,
                    )
                )
                self.saved_expense_input = toga.NumberInput(
                    readonly=True,
                    style=toga.style.Pack(
                        width=75,
                        font_size=13,
                        margin_top=25,
                        margin_left=5,
                    )
                )
                self.currency = toga.Label(
                    "$",
                    style=toga.style.Pack(
                        font_size=16,
                        margin_left=10,
                        margin_top=27,
                    )
                )
                self.added_line_box = toga.Box(
                    direction=ROW
                )
                self.added_line_box.add(self.currency)
                self.added_line_box.add(self.saved_expense_input)

                self.saved_box = toga.Box(
                    style=toga.style.Pack(
                        width=120,
                        height=150,
                        direction="column",
                        background_color="#f3eeec",
                        flex=1,
                        margin=10
                    )
                )
                self.saved_box.add(self.saved_expense_label)
                self.saved_box.add(self.added_line_box)

                self.expense_container3.add(self.saved_box)
                self.expense_widget.add(self.expense_container3)

            
                self.saved_expense_label.text = expense
                self.saved_expense_input.value = float(value)

                total_budget = total_budget + float(self.custom_dict[expense])
                self.spent_input.value = total_budget

                remaining = remaining - float(self.custom_dict[expense])
                self.remaining_input.value = remaining

            



def main():
    return BudgetTracker()
    
