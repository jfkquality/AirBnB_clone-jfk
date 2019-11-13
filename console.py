#!/user/bin/python3
# Command interpreter for AirBnB project
import cmd, sys, gc
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not name:
            print("** class name missing **")
            return
        try:
            self.name = eval(name)()
        except NameError:
        # if not name in eval(name).__name__:
        # if not isinstance(name, BaseModel):
            print("** class doesn't exist **")
            return
        # self.name = eval(name)()
        print(self.name)
        my_model = self.name
        print(my_model.id)
        # print(my_model.created_at)
        # my_model.name = "Holberton"
        # my_model.my_number = 89
        # my_model.save()

    def do_show(self, name, id):
        """Prints the string representation of an instance based on the class name and id"""
        if not name:
            print("** class name missing **")
        if not id:
            print("** instance id missing **")

    def do_destroy(self, name, id):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not name:
            print("** class name missing **")
        if not id:
            print("** instance id missing **")
        if not attr_name:
            print("** attribute name missing **")
        if not attr_val:
            print("** value missing **")

    def do_all(self, name=None):
        """Prints all string representation of all instances based or not on the class name"""
        for obj in gc.get_objects():
            if isinstance(obj, name):
                print(obj)
        # pass

    def do_update(self, name, id, attr_name, attr_val):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        if not name:
            print("** class name missing **")
        if not id:
            print("** instance id missing **")


    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Press Ctrl-d to exit the program """
        print()
        return True

    def emptyline(self):
        """Do nothing when user enters nothing and presses Enter.
        Default is to repeat last command entered.
        """
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF: Press Ctrl-d to exit the program")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
