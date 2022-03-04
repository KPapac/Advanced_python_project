import plugboard, rotors

plugboard = plugboard.Plugboard({"W": "H", "A": "B", "o": "e" })
    
# Set up the enigma parts
rotor1 = rotors.Rotor(3)
rotor2 = rotors.Rotor(5)
ref = rotors.Reflector(1)

message = "Hello world"
# message = "UYCCFQFKCI"

def enigma_encrypt(message):
    ''''''
    # Encrypt a message
    encrypt = []
    for letter in message:
        plug_in = plugboard.plugboard_encrypt_the_letters(letter)
        out1 = rotor1.rottor_encrypt_the_letter(plug_in)
        out2 = rotor2.rottor_encrypt_the_letter(out1)
        out_ref = ref.reflector_change_the_letter(out2)
        out3 = rotor2.rottor_decrypt_the_letter(out_ref)
        out4 = rotor1.rottor_decrypt_the_letter(out3)
        plug_out = plugboard.plugboard_encrypt_the_letters(out4)
        encrypt.append(plug_out)

        print(letter, plug_in, out1, out2, out_ref, out3, out4, plug_out)
    return "".join(encrypt)

print(enigma_encrypt(message))