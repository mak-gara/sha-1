import struct


class SHA1:

    def __init__(self, input_message: str) -> None:
        self.input_message = bytes(input_message, "utf-8")

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
