import thirdhand.Strings as i18n

def create_command(lang, args):
    if len(args) < 3:
        print(i18n.STRINGS[lang]['str_arg_not_enough'] % ('create', 3, len(args)))
        return
    with open(args[2], "w+") as file:
        if args[1] == '1':
            my_addr = input(i18n.STRINGS[lang]['str_input_host_addr'])
            my_port = input(i18n.STRINGS[lang]['str_input_host_port'])
            file.write(i18n.CODE_SLICE_2 % (my_addr, my_port))
        elif args[1] == '2':
            your_port = input(i18n.STRINGS[lang]['str_input_others_port'])
            file.write(i18n.CODE_SLICE_3 % i18n.STRINGS[lang]['str_input_others_port'])
        else:
            print(i18n.STRINGS[lang]['str_arg_not_found'] % ('create', args[1]))

def connect_command(lang, args):
    if len(args) < 2:
        print(i18n.STRINGS[lang]['str_arg_not_enough'] % ('connect', 2, len(args)))
        return
    if args[1] == '1':
        exec(i18n.CODE_SLICE_0 % (input(i18n.STRINGS[lang]['str_input_host_port']), i18n.STRINGS[lang]['str_listening']))
    elif args[1] == '2':
        exec(i18n.CODE_SLICE_1 % (input(i18n.STRINGS[lang]['str_input_others_addr'], i18n.STRINGS[lang]['str_input_others_port'])))
    else:
        print(i18n.STRINGS[lang]['str_arg_not_found'] % ('connect', args[1]))
    
