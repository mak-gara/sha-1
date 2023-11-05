class SHA1:

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
