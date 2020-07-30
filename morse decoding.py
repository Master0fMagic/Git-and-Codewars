from morse3 import Morse as m

MORSE_CODE = { '.-':'A', '-...':'B', 
                    '-.-.':'C', '-..':'D', '.':'E', 
                    '..-.':'F', '--.':'G', '....':'H', 
                    '..':'I', '.---':'J', '-.-':'K', 
                    '.-..':'L', '--':'M', '-.':'N', 
                    '---':'O', '.--.':'P', '--.-':'Q', 
                    '.-.':'R', '...':'S', '-':'T', 
                    '..-':'U', '...-':'V', '.--':'W', 
                    '-..-':'X', '-.--':'Y', '--..':'Z', 
                    '.----':'1', '..---':'2', '...--':'3', 
                    '....-':'4', '.....':'5', '-....':'6', 
                    '--...':'7', '---..':'8', '----.':'9', 
                    '-----':'0', '--..--':', ', '.-.-.-':'.', 
                    '..--..':'?', '-..-.':'/', '-....-':'-', 
                    '-.--.':'(', '-.--.-':')', '...---...':'SOS',
                    } 

def decodeMorse(morse_code):
    #words=morse_code.strip().split("   ")
    words=[word.split(' ') for word in  morse_code.strip().split("   ")]
    result =""
    for word in words:
        for letter in word:
            result+=MORSE_CODE[letter]
        result+=" "
    return result.strip()

print(m("MORSE HAS BEEN DECODED").stringToMorse())
