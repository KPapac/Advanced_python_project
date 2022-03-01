class Plugboard():
    def __init__(self, dict_of_connections):
        self.dict_of_connections = {k.upper():v.upper() for k,v in dict_of_connections.items()}

    def plugboard_encrypt_the_letters(self, message):
        '''Takes as input a dictionary of letters to connect and swaps the connected letters with each other. 
        Letters without connections do not change. E.g. A connection between "w" and "h" is made, so if the 
        message "HELLOWORLD" passes though the plugboard, it will come out as "WELLOHORLD".'''
        cryptograph = []
        for letter in message.upper().replace(" ", ""):
            if letter in self.dict_of_connections.keys():
                cryptograph.append(self.dict_of_connections[letter])
            elif letter in self.dict_of_connections.values():
                cryptograph.append(list(self.dict_of_connections.keys())[(list(self.dict_of_connections.values()).index(letter))])
            else:
                cryptograph.append(letter)
        return "".join(cryptograph)


#test code
connections_to_make = {"W": "H", "A": "B", "o": "e" }
plug = Plugboard(connections_to_make)
# t = plug.plugboard_encrypt_the_letters("Hello world")
# print(t)
assert connections_to_make == {"W": "H", "A": "B", "o": "e" }
assert plug.plugboard_encrypt_the_letters("Hello world") == "WOLLEHERLD"