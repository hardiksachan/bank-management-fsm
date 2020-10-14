import database
from app import App

database.make_all_tables()
database.reset_withdrawals()

app = App()
app.screen_manager.initialize(app.main_menu)
