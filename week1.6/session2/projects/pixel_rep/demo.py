def create_pixels(width, height, value=0, maximum=255):
        """
        Creates a new array of pixels, replacing any existing image data.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        pixels = [[value] * width for x in range(height)]
        return pixels

print(create_pixels(5, 5, value=10, maximum=255))