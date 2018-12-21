# Assignment 1
# Rutvik Patel
# ID: 1530012
# CMPUT 274 Fall 2018
#
# This program works hand in hand with the other files in the huffman directory
# in order to correctly compress a file using a huffman tree, use the pickle
# module to compress and write the huffman tree, and send it to the user who
# wishes to uncompress later. Then, the file that is passed is uploaded to a
# web server at the web address localhost:8000 and it is there where the file
# is then decompressed.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# importing the necessary modules
import bitio
import huffman
import pickle
import sys

# control the debugging output that is output to the command line...
# set debug to: 0 for no debugging, 1 for light debugging, and 2 for
# verbose debugging.
debug = 0

# control the pickle module to check if you are compressing the file
# correctly, set to True in order to correctly run the program.
pkl = True


def read_tree(tree_stream):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # This function reads a description of a Huffman tree from the given
    # compressed tree stream, and use the pickle module to construct the
    # tree object. Then, it returns the root node of the tree itself.

    # Args:
    #  tree_stream: The compressed stream o read the tree from.

    # Returns:
    # A Huffman tree root constructed according to the given description.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # unpickle the tree from the tree stream
    unpkltree = pickle.load(tree_stream)

    # return the root node of the tree
    return(unpkltree.root)


def decode_byte(tree, bitreader):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # This function reads bits from the bit reader and traverses the given tree
    # from the root to a leaf. Once a leaf is reached, bits are no longer read
    # and the value of that leaf is returned.

    # Args:
    #  bitreader: An instance of bitio.BitReader to read the tree from.
    #  tree: A Huffman tree.

    # Returns:
    #  Next byte of the compressed bit stream.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # setting the starting point of the node to be
    # equal to the tree.root (return value from the read_tree function)
    node = tree

    # while the class is still a TreeBranch...
    while isinstance(node, huffman.TreeBranch):
        # the action of reading can fail, so we
        # need to catch the exception.
        try:
            bit = bitreader.readbit()

            if bit == 0:
                # go left
                node = node.left

            elif bit == 1:
                # go right
                node = node.right

        # break the while loop if we reach the end
        # or anything goes wrong
        except:
            break

    # the byte is then the value of that node
    byte = node.value

    # return that byte
    return node.value


def decompress(compressed, uncompressed):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # First, read a Huffman tree from the 'tree_stream' using your
    # read_tree function. Then use that tree to decode the rest of the
    # stream and write the resulting symbols to the 'uncompressed'
    # stream.

    # Args:
    #  compressed: A file stream from which compressed input is read.
    #  uncompressed: A writable file stream to which the uncompressed
    #      output is written.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # unpickling the tree from the compressed file stream
    unpkltree = read_tree(compressed)

    # creating BitReader and BitWriter objects
    bitread = bitio.BitReader(compressed)
    bitwriter = bitio.BitWriter(uncompressed)

    while True:
        try:
            nextbyte = decode_byte(unpkltree, bitread)

            # use bitwriter to write indiviual bits to a file
            bitwriter.writebits(nextbyte, 8)
        except:
            break

    # flushing the bit writer object
    bitwriter.flush()

    pass


def write_tree(tree, tree_stream):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # Write the given Huffman tree to the given tree_stream
    # using the pickle module.

    # Args:
    #  tree: A Huffman tree.
    #  tree_stream: The binary file to write the tree to.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # pickle the tree, and write to the specified tree_stream
    pickle.dump(tree, tree_stream)

    pass


def check_mode(uncompressed, compressed):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # This function checks if the file is actually readable or not, if not it
    # terminates the program.
    # Args:
    #    uncompressed: A file stream from which you can read the input.
    #    compressed: A file stream that will receive the tree description
    #                and the coded input data.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # error handling depending on the mode

    # if not in reading bits mode...
    if uncompressed.mode != 'rb':
        print('Error in reading file...')
        sys.exit(-1)

    # if not in writing bits mode...
    if compressed.mode != 'wb':
        print('Error in writing to file...')
        sys.exit(-1)

    pass


def compress(tree, uncompressed, compressed):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # This function writes the given tree to the stream 'compressed' using the
    # write_tree function. Then use the same tree to encode the data
    # from the input stream 'uncompressed' and write it to 'compressed'.
    # If there are any partially-written bytes remaining at the end,
    # write 0 bits to form a complete byte.

    # Flush the bitwriter after writing the entire compressed file.

    # Args:
    #    tree: A Huffman tree.
    #    uncompressed: A file stream from which you can read the input.
    #    compressed: A file stream that will receive the tree description
    #                and the coded input data.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # checking if the file is readable or not before we compress
    check_mode(uncompressed, compressed)

    # writing the created tree to the tree file stream
    if pkl:
        write_tree(tree, compressed)

    # optional debugging output
    if debug >= 1:
        print('The tree is: ', tree)
        print()
        print('The root is: ', tree.root)
        print()

    # mapping the bytes to bit sequences to a dictionary
    bit2bytemap = huffman.make_encoding_table(tree.root)

    # optional debugging output
    if debug >= 1:
        print('The encoding table is: ', bit2bytemap)
        print()

    # creating bit reader object
    bitread = bitio.BitReader(uncompressed)

    # creating bit writer object
    bitwrite = bitio.BitWriter(compressed)

    # We don't know how many bytes there are, need to break
    # this loop once we reach end of file
    while True:
        # read each byte from the uncompressed file, encode it using the tree
        # io can fail... must cover it safely.
        try:
            byte = bitread.readbits(8)
            if debug > 1:
                print('The byte read is: ', byte)
                print('The character is: ', chr(byte))

            # find the corresponding bit sequence in our dictionary
            # and write to the compressed file stream
            if byte in bit2bytemap:
                # go through the bit sequence that corresponds
                # to the bits read in
                for i in range(len(bit2bytemap[byte])):

                    if debug > 1:
                        print(bit2bytemap[byte][i])

                    # If bit read is a True (1) or False (0)...
                    if bit2bytemap[byte][i] is True:
                        bitwrite.writebit(True)

                    elif bit2bytemap[byte][i] is False:
                        bitwrite.writebit(False)

        # If no more bits to read, break out of the while loop
        except EOFError:
            break

    # when writing to a disk, the OS 'buffers' the writing of the
    # bit for performance reasons, because there is buffering, when
    # you are done writing you have to tell the system that you are
    # done with writing. You need to flush and close...
    flushIt(bitwrite, compressed)
    pass


def flushIt(bitwrite, compressed):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # When writing to a disk, the OS 'buffers' the writing of the
    # bit for performance reasons, because there is buffering, when
    # we are done writing this function tells the system that we are
    # done with writing, and therfore we flush and close...

    # Args:
    #    bitwrite: the bitwriter object
    #    compressed: the compressed file stream
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # flush the object
    bitwrite.flush()
    # flush the file, since the object talks to the file
    compressed.flush()
    # close the file
    compressed.close()

    pass
