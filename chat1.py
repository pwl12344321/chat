
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    sam_word_count = 0
    tom_word_count = 0
    sam_sticker_count = 0
    tom_sticker_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Sam':
            if s[2] == 'sticker':
                sam_sticker_count += 1
            else:
                for m in s[2:]:
                    sam_word_count += len(m)
        elif name == 'Tom':
            if s[2] == 'sticker':
                tom_sticker_count += 1
            else:
                for m in s[2:]:
                    tom_word_count += len(m)
    print('sam says', sam_word_count, 'and sticker count', sam_sticker_count)
    print('tom says', tom_word_count, 'and sticker count', tom_sticker_count)
        #print(s)


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
    lines = read_file('[line]Tom.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()