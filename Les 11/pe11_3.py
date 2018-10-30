def encrypt(typed_input):
    orderd_plus = [ord(char) + 300 for char in input_user]
    char = [chr(i) for i in orderd_plus]
    line = ''.join(char)
    print(line)

naam = input("Uw naam: ")
beginstation = input("Uw beginstation: ")
eindstation = input( "Uw eindstation: ")
input_user = (f'{naam} {beginstation} {eindstation}')
encrypt(input_user)