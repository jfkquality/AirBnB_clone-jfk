#!/user/bin/python3
# Command interpreter for AirBnB project
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
