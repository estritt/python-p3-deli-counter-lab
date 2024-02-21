katz_deli = []

def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        in_line = ""
        for i in range(len(katz_deli)):
            in_line += f' {i+1}. {katz_deli[i]}'
        print(f'The line is currently:{in_line}')


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli.pop(0)}.')