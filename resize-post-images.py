from wand.image import Image

from os import walk
from os.path import join, splitext

(dirpath, _, filenames) = next(walk("_img/posts"))
(target_dirpath, _, target_filenames) = next(walk("assets/img/posts"))

for image_file_name in filenames:
    image_file = join(dirpath, image_file_name)
    (image_file_name_alone, _) = splitext(image_file_name)

    if (image_file_name in target_filenames): continue

    with Image(filename=image_file) as img:
        print('Generating image for', image_file_name)

        widths = [
                (230, '_placehold'), 
                (535, '_thumb'), 
                (535*2, '_thumb@2x'),
                (575, '_xs'),
                (767, '_sm'),
                (991, '_md'),
                (1999, '_lg'),
                (1920, '')
                ]

        for (width, suffix) in widths:
            with img.clone() as image_clone:
                print('\t-> Generating size', width)

                image_clone.transform(resize=str(width)+'x')
                image_clone.save(filename=join(target_dirpath, image_file_name_alone+suffix+'.jpg'))

