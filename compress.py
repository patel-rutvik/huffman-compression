import huffman
import sys
import util


def run_compressor (filename):
    # opening file to read
    with open(filename, 'rb') as uncompressed:
        # makefreqtable reads the whole file
        freqs = huffman.make_freq_table(uncompressed)
        tree = huffman.make_tree(freqs)
        # reinitializing the file 'editing cursor' back to
        # the start of the file
        uncompressed.seek(0)
        with open(filename+'.huf', 'wb') as compressed:
            # adding tree_stream as a parameter...????????
                util.compress(tree, uncompressed, compressed)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <file1> <file2> ...".format(sys.argv[0]))
    else:
        for filename in sys.argv[1:]:
            print ("Compressing '{0}' to '{0}.huf'".format(filename))
            run_compressor(filename)
