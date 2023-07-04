from Engine import searchObject
from reader import load_images

def main():
    images = load_images.getImages
    expected = searchObject.searchObject.compare(images.images, images.expected)


if __name__ == '__main__':
    main()