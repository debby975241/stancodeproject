"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

Give some images of a same place.
And this will show a image that has no pedestrian in it(help you remove the pedestrian in the picture).
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = math.sqrt((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0                 # to count the total number of red in every pixel
    green = 0               # to count the total number of green in every pixel
    blue = 0                # to count the total number of blue in every pixel
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    rgb = [red//len(pixels), green//len(pixels), blue//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    minimum_dist = 255      # assign it with the longest distance it could be
    avg_rgb = get_average(pixels)
    best_pixel = pixels[0]  # compare the pixels with the first in the list of pixels one by one to assign the best one
    for pixel in pixels:
        distance = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])
        if distance < minimum_dist:
            minimum_dist = distance
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixel = []                          # the pixel in the same position of every image
            for i in range(len(images)):
                pixel.append(images[i].get_pixel(x, y))
            best_pixel = get_best_pixel(pixel)
            each_pixel = result.get_pixel(x, y)  # get each pixel in result
            each_pixel.red = best_pixel.red
            each_pixel.green = best_pixel.green
            each_pixel.blue = best_pixel.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
