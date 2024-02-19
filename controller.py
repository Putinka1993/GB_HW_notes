import user
import model
import view
class Control:

    def __init__(self):
        self.command = user.Input_user_command()
        self.get_command = model.My_function()
    def enter_command(self):

        while self.command.return_command() != "stop":
            match self.command.return_command():
                case 'date':
                    self.get_command.date_function()
                case 'show':
                    self.get_command.show_function()
                case 'show_all':
                    self.get_command.show_all_function()
                case 'add':
                    self.get_command.add_function()
                case 'edit':
                    self.get_command.edit_function()
                case 'delete':
                    self.get_command.delete_function()
                case _:
                    start = view.Show_information(f"Неверная команда, попробуйте заново !")
                    return start.show_point()

