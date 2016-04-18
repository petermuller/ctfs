
def make_dict():
	morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.', 
		'D': '-..',    'E': '.',      'F': '..-.',
		'G': '--.',    'H': '....',   'I': '..',
		'J': '.---',   'K': '-.-',    'L': '.-..',
		'M': '--',     'N': '-.',     'O': '---',
		'P': '.--.',   'Q': '--.-',   'R': '.-.',
		'S': '...',    'T': '-',      'U': '..-',
		'V': '...-',   'W': '.--',    'X': '-..-',
		'Y': '-.--',   'Z': '--..',
		
		'0': '-----',  '1': '.----',  '2': '..---',
		'3': '...--',  '4': '....-',  '5': '.....',
		'6': '-....',  '7': '--...',  '8': '---..',
		'9': '----.' 
	}
	morse_dict.update(dict((morse_dict[i], i) for i in morse_dict))
	return morse_dict

def code(string, d):
	newstr = ""
	for token in string.split():
		newstr += d[token.upper()] + ' '
	return newstr

def main():
	d = make_dict()
	while True:
		string = raw_input("(De)Code me: ")
		print(code(string,d))
		print

if __name__ == "__main__":
	main()
