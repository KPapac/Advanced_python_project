# Enigma Machine

This is an attempt to simulate the enigma machine in python.

### Installation:

`pip3 install uu-enigma-kostas`

### Usage:
In the python interpreter type:

`from enigma_kostas.enigma_run import enigma_encrypt`

`enigma_encrypt("Hello World", "453")`

to create an enigma machine with rotors IV, V and III in this specific order and encrypt the message "Hello World". The encrypted message returned would be 'WTSSPHPYSI' in this case.
To decrypt you must specify the order of the specific rotors used to encypt the original message. In this example it was "453", so we would type in the python interpreter:

`enigma_encrypt("WTSSPHPYSI", "453")`

and the output will be 'HELLOWORLD'

### Uninstall:
`pip3 uninstall uu-enigma-kostas`

## General Information
This project was inspired from [this youtube video](https://www.youtube.com/watch?v=ybkkiGtJmkM).

### Parts of the machine modeled:
#### Plugboard
The plugboard is a part of the enigma that connects a pair of letters of our choice in order a letter with its pair. The plugboard currently is fixed with the creation of an enigma machine, but could be made to be set by the user in the future.

#### Rotors
Each time `enigma_encrypt()` is run an enigma machine is created and every time the same five rotors occur. This means that rotor "1" will always have the same "internal circuit" that connects input and output letters for encryption. The same is true for the rest of the rotors. The rotors are passed in the `enigma_encrypt()` in order, so first, second and the third rotor. In the above example, the "453" string means that rotor 4 is first, the rotor 5 is second and rotor 3 is third. Each rotor has a notch which allows for its rotation depending on the position of the notch of the previous rotor. The first rotor always rotates, thus shifting the output values of the dictionary that models the circuit once each time.

#### Reflector
The reflector is a part of the machine that connects letters A to Z in pairs. It receives the output of the last rotor, changes it and then passes it back to that same rotor.


#### The circuit
To summarise, a letter can be modified 7 to 9 times, depending on whether the letter is modified by the plugboard or not. User input passes through these components in this order:

1. Plugboard
2. Rotor 1
3. Rotor 2
4. Rotor 3
5. Reflector
6. Rotor 3
7. Rotor 2
8. Rotor 1
9. Plugboard

### What does not work yet:

1. Rotors do not rotate, as I have not figured out how to decrypt the messages when this feature is on. This means that an input like "HHH" will be encrypted into "TTT" a given settings of rotors and plugboard. Ideally the same letter should not appear consecutively.
2. There is no script for calling the program directly from the command line for now.
