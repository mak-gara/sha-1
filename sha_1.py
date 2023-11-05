import struct


class SHA1:
    """
    Performs hashing using the SHA-1 algorithm.
    """

    def __init__(self, input_message: str) -> None:
        self.input_message = bytes(input_message, "utf-8")
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    @staticmethod
    def rotate(n, b):
        """
        Method for cyclic left shift.
        The number n is shifted by b positions to the left, and the result
        of this operation is combined with a bitwise OR with a shift of
        n by 32 - b positions to the right. Finally, the result is combined
        with a 32-bit mask, where all bits are set to 1, ensuring
        that the result remains within the 32-bit number.

        :param n: 32-bit number for a cyclic shift.
        :param b: Number indicating the number of positions by which the number should be shifted.
        :return: Shifted number.
        """

        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

    def pad_with_zeros(self) -> bytes:
        """
        Pads the input message with zeros so that padded_data has 512 bits.

        :return: A sequence of bytes representing the input_message padded with zeros.
        """

        padding = b"\x80" + b"\x00" * (63 - (len(self.input_message) + 8) % 64)
        padded_data = self.input_message + padding + struct.pack(">Q", 8 * len(self.input_message))
        return padded_data

    def split_blocks(self) -> list[bytes]:
        """
        Splits the padded data into blocks of 64 bytes each.

        :return: A list of byte blocks where each block is 64 bytes long, obtained from the padded data.
        """

        return [
            self.padded_data[i: i + 64] for i in range(0, len(self.padded_data), 64)
        ]

    def expand_block(self, block: bytes) -> list[int]:
        """
        Expands a 512-bit block into an 80-word message schedule.

        :param block: A 512-bit block of data to be expanded.
        :return: An expanded 80-word message schedule derived from the input block.
        """
        w = list(struct.unpack(">16L", block)) + [0] * 64
        for i in range(16, 80):
            w[i] = self.rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        return w

    def hash(self) -> str:
        """
        Generates SHA-1 hash for the provided data.

        The hash() method implements the Secure Hash Algorithm 1 (SHA-1) logic for
        generating a hashed output from the given data. It follows the SHA-1 hashing
        process by first padding the input data, splitting it into blocks, and
        applying the defined operations on these blocks iteratively. The algorithm
        iterates through each block, expanding it, and updating the state variables
        according to the SHA-1 specifications.

        :return: hash for input message.
        """

        self.padded_data = self.pad_with_zeros()
        self.blocks = self.split_blocks()

        for block in self.blocks:
            expanded_block = self.expand_block(block)
            a, b, c, d, e = self.h

            for i in range(80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                a, b, c, d, e = (
                    self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xFFFFFFFF,
                    a,
                    self.rotate(b, 30),
                    c,
                    d,
                )

            self.h = (
                self.h[0] + a & 0xFFFFFFFF,
                self.h[1] + b & 0xFFFFFFFF,
                self.h[2] + c & 0xFFFFFFFF,
                self.h[3] + d & 0xFFFFFFFF,
                self.h[4] + e & 0xFFFFFFFF,
            )

        return ("{:08x}" * 5).format(*self.h)
