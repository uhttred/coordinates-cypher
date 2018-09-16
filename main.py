import sys

OP_ENCODE = '-e'
OP_DECODE = '-d'
EX_ENCODE = '.nje'
EX_DECODE = '.njd'

labels = {
	'space': '\'',
	'colon': ':',
	'void' : ''
}

box = {
	0: {
		' ' : 1,
		'(' : 2,
		')' : 3,
		'[' : 4,
		']' : 5,
		'{' : 6,
		'}' : 7,
		'\n': 8,
		'0' : 9
	}, 
	1: {
		'.' : 1,
		',' : 2,
		'-' : 3,
		'?' : 4,
		'!' : 5,
		'\'': 6,
		'"' : 7,
		'@' : 8,
		'\\': 9,
		'/' : 10,
		':' : 11,
		'_' : 12,
		';' : 13,
		'+' : 14,
		'*' : 15,
		'=' : 16,
		'%' : 17,
		'&' : 18,
		'<' : 19,
		'>' : 20,
		'$' : 21,
		'#' : 22,
		'^' : 23,
		'~' : 24,
		'|' : 25,
		'1' : 26
	},
	2: {
		'a': 1,
		'b': 2,
		'c': 3,
		'2': 4,
		chr(225): 5,
		chr(224): 6,
		chr(226): 7,
		chr(227): 8,
		chr(231): 9
	},
	3: {
		'd': 1,
		'e': 2,
		'f': 3,
		'3': 4,
		chr(233): 5,
		chr(234): 6
	},
	4: {
		'g': 1,
		'h': 2,
		'i': 3,
		'4': 4,
		chr(237): 5
	},
	5: {
		'j': 1,
		'k': 2,
		'l': 3,
		'5': 4
	},
	6: {
		'm': 1,
		'n': 2,
		'o': 3,
		'6': 4,
		chr(243): 5,
		chr(245): 6
	},
	7: {
		'p': 1,
		'q': 2,
		'r': 3,
		's': 4,
		'7': 5
	},
	8: {
		't': 1,
		'u': 2,
		'v': 3,
		'8': 4,
		chr(250): 5
	},
	9: {
		'w': 1,
		'x': 2,
		'y': 3,
		'z': 4,
		'9': 5
	}
}

def mask(char):
	is_upper = char.isupper()
	char = char.lower()
	for k, v in box.items():
		for c, r in v.items():
			if char == c:
				return str(k)*r + labels.get('colon') if is_upper else str(k)*r 

def unmask(m):
	is_upper = True if m[-1] == labels.get('colon') else False 
	mask_target = len(m) - 1 if is_upper else len(m)
	mask_candiadtes = box.get(int(m[0]))
	for k, v in mask_candiadtes.items():
		if mask_target == v:
			return k.upper() if is_upper else k

def encode(s):
	return labels.get('space').join([mask(char) for char in s])

def decode(s):
	return labels.get('void').join([unmask(char) for char in s.split(labels.get('space'))])

def main():

	if len(sys.argv) < 2:
		exit()

	operation = sys.argv[1]
	file_name = sys.argv[2]

	temp = file_name.find('.') 
	hide_ext = True if temp != -1 else False
	output_name = file_name[:temp] if hide_ext else file_name

	fr = open(file_name, 'r') 

	if operation == OP_DECODE:
		txt = fr.read()
		fw  = open(output_name + EX_DECODE, 'w')
		s = decode(txt[:-2])
		fw.write(s)

	elif operation == OP_ENCODE:
		lines = fr.readlines()
		fw    = open(output_name + EX_ENCODE, 'w') 
		for line in lines:
			s = encode(line)
			fw.write(s + labels.get('space'))

	else:
		exit()

	fr.close()
	fw.close()
	
if __name__ == '__main__':
	main()

















