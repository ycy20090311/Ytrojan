import thirdhand.Strings as i18n
from thirdhand.Strings import gp
import thirdhand.Core as core
class Main:
    
    LANGUAGE = "zh_CN"
    
    def run(self):
        # Output the logo first.
        print(i18n.LOGO_STR)
        self.mainloop()
        
    def mainloop(self):
        while True:
            # The mainloop
            cmd = input(gp(i18n.MAIN_PROMPT))
            self.doCommand(cmd)
    
    def doCommand(self, cmd_str):
        cmd = cmd_str.split()
        if cmd[0] == 'help':
            self.showHelp()
        elif cmd[0] == 'create':
            core.create_command(self.LANGUAGE, cmd)
        elif cmd[0] == 'connect':
            core.connect_command(self.LANGUAGE, cmd)
        elif cmd[0] == 'exit':
            exit(0)
        else:
            print(i18n.STRINGS[self.LANGUAGE]["str_command_not_found"] % ('Third-Hand', cmd[0]))
    
    def showHelp(self):
        print("help\t%s" % i18n.STRINGS[self.LANGUAGE]['str_help_for_help'])
        print("create [%s] [%s]\t%s" % (
            i18n.STRINGS[self.LANGUAGE]['str_word_mode'],
            i18n.STRINGS[self.LANGUAGE]['str_word_path'],
            i18n.STRINGS[self.LANGUAGE]['str_help_for_create']
        ))
        print("connect [%s]\t%s" % (
            i18n.STRINGS[self.LANGUAGE]['str_word_mode'],
            i18n.STRINGS[self.LANGUAGE]['str_help_for_connect']
        ))
        print("exit\t%s" % i18n.STRINGS[self.LANGUAGE]["str_help_for_exit"])
        print("\n\n%s" % i18n.STRINGS[self.LANGUAGE]["str_mode_description"])
        print()
