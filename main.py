# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    ##print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#nome = str(input('digite seu nome:')).strip()
#if nome == 'gustavo':
    #print('que nome lindo você tem!')# esse comando só vai acontecer se o nome for gustavo
#else:
    #print('Bom dia, {}'.format(nome))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {:.1f}'.format(m))
if m >= 7.0:
    print('APROVADO')
else:
    print('REPROVADO')
