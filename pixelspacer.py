# create a funtion that inputs an image and outputs an image that is 3x the size of the input image with a 1 pixel border of transparency around each input pixel

from PIL import Image, ImageOps


def pixelspacer(input_path):
    # Open the input image
    image = Image.open(input_path)

    # Calculate the new size with 3 times the width and height
    new_width = image.width * 3
    new_height = image.height * 3

    # Create a new transparent image with the new size
    new_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    # Create a border around each pixel with transparency
    border_width = 1

    for y in range(image.height):
        for x in range(image.width):
            # Get the pixel value from the original image
            original_pixel = image.getpixel((x, y))

            # Calculate the position in the new image
            new_x = x * 3 + border_width
            new_y = y * 3 + border_width

            # Set the pixel value in the new image
            for i in range(3):
                for j in range(3):
                    # If it's the center pixel, use the original pixel value
                    if i == 1 and j == 1:
                        new_image.putpixel((new_x + i, new_y + j), original_pixel)
                    else:
                        if new_x + i < new_width and new_y + j < new_height:
                            new_image.putpixel((new_x + i, new_y + j), (0, 0, 0, 0))

    # Return the resulting image
    return new_image


input_image_path = "input/image.png"
output_image = pixelspacer(input_image_path)
output_image.save("output/image.png")
