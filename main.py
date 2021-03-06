from lib.Corrector import Corrector
from test import Tester

from optparse import OptionParser


CORPUS = "corpus.txt"


def main():
    options = read_commands()
    corrector = Corrector(options.corpus)
    
    if options.test:
        Tester(corrector, options.verbose).run()
        exit(0)
    
    elif not options.input:
        options.input = input("[*]: ")

    corrected_text = corrector.correct(options.input, True)

    if options.output:
        output = open(options.output, 'w')
        output.write(corrected_text)
        output.close()
    else:
        print("[+]:", corrected_text)


def read_commands():
    parser = OptionParser("%prog -f <input_file>")
    parser.add_option("-f", dest="input", help="File to correct")
    parser.add_option("-o", dest="output", help="File to save the corrections")
    parser.add_option("-c", dest="corpus", help="Corpus in a txt file")
    parser.add_option("-t", action="store_true", default=False, dest="test", help="Run tests")
    parser.add_option("-v", action="store_true", default=False, dest="verbose", help="Make the output verbose")

    (options, args) = parser.parse_args()

    with open(options.corpus or CORPUS) as corpus:
        options.corpus = corpus.read()

    if options.input:
        with open(options.input) as f:
            options.input = f.read()

    return options


if __name__ == "__main__":
    main()
