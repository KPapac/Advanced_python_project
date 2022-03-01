import random 

class Rotor():
    def __init__(self, seed):
        # A list of the capital letters of the latin alphabet (eg, [A, B, C, ..., Z])
        self.input_letters = [chr(x) for x in range(65,91)]
        # The seed ensures that each rotor will have a random intermal wiring, which will be identical for each 
        # corresponding rotor across enigma machines
        self.seed = seed
        random.seed(self.seed)
        self.make_the_wiring()
        
    def make_the_wiring(self):
        # The list of new random output letters
        self.output_letters = random.sample(self.input_letters, 26)
        self.wiring_dict = {self.input_letters[i]: self.output_letters[i] for i in range(0,26)}
        
    def rottor_encrypt_the_letter(self, message):
        '''Takes an input message, makes all letters uppercase and removes whitespace. Return the message encrypted.'''
        cryptograph = []
        for letter in message.upper().replace(" ", ""):
            cryptograph.append(self.wiring_dict[letter])
        return "".join(cryptograph)

    def rottor_decrypt_the_letter(self, message):
        '''Return the message decrypted.'''
        decrypt = []
        for letter in message.upper().replace(" ", ""):
            index_in_input = self.output_letters.index(letter)
            decrypt.append(self.input_letters[index_in_input])
        return "".join(decrypt)
            
        
class Reflector(Rotor):
    def __init__(self, seed):
        Rotor.__init__(self, seed)
        self.make_the_wiring()
    
    def make_the_wiring(self):
        self.part1_of_pairs = random.sample(self.input_letters, 13)
        self.part2_of_pairs = [x for x in self.input_letters if x not in self.part1_of_pairs]
        self.wiring_dict = {self.part1_of_pairs[i]: self.part2_of_pairs[i] for i in range(0,12)}
        
    # def reflector_change_the_letter(self, message):
    #     '''Takes an input message, makes all letters uppercase and removes whitespace. Return the message cryptographed.'''
    #     cryptograph = []
    #     for letter in message.upper().replace(" ", ""):
    #         if letter in list(self.wiring_dict.keys()):
    #             cryptograph.append(self.wiring_dict[letter])
    #         else: 
    #             # cryptograph.append(self.wiring_dict.keys()[self.wiring_dict.values().index(letter)])
    #             print(self.wiring_dict.keys()[self.wiring_dict.values().index(letter)])

    #         # cryptograph.append(self.wiring_dict[letter])
    #     return "".join(cryptograph)





#test code
# for rotors
# decrypts = ["ZIRRCYWC", "UDHHRSTR", "GFKKWCOW", "YLWWMSJM", "TPQQXJFX"]
# for i, decrypt in zip(range(0,5), decrypts):
#     rotor = Rotor(i)
#     print(rotor.wiring_dict)
#     print(rotor.rottor_encrypt_the_letter("Hello bro"))
#     print(rotor.rottor_decrypt_the_letter(decrypts[i]))


# for reflectors
# refl = Reflector(1)
# print(refl.part1_of_pairs)
# print(refl.part2_of_pairs)
# print(refl.wiring_dict)
# print(refl.rottor_change_the_letter("Hello bro"))