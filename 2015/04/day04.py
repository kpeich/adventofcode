import optparse
from hashlib import md5

data = 'iwrupvqb'
test1 = 'abcdef'
test2 = 'pqrstuv'

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

#    with open(options.filename) as f:
#        data = [line.strip() for line in f]

    if options.dbg:
        pass

    output = ''
    part1 = 0
    while output[:6] != '000000':
        part1 += 1
        string = f"{data}{part1}"
        output = md5(string.encode()).hexdigest()
        if output.startswith('00000'):
            print(f"hash: {part1} : {output}")
