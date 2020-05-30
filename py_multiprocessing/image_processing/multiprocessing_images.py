import time
from PIL import Image, ImageFilter
import concurrent.futures

images = [f"{i}.jpg" for i in range(1, 11)]


def process_images(image_name):
    print(f"Processing: {image_name}")

    size = (1200, 1200)

    img = Image.open(image_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)

    img.save(f"processed/{image_name}")

    print(f"{image_name} has been processed.")


start_time = time.perf_counter()

# doing in naive approach
# for img in images:
#     process_images(img)


# now lets do it in multiprocessing style

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(process_images, images)

    for res in results:
        print(res)

end_time = time.perf_counter()

print(f"Total time taken: {end_time - start_time}")