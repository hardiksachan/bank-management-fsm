import database
from app_gui import App

database.make_all_tables()
database.reset_withdrawals()

app = App()
app.state_Machine.initialize(app.main_menu)
