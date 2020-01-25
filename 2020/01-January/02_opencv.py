import cv2
import time

x, y = 200, 200
right, bottom = 300, 300
thickness = 2
dim = (416, 416)

# Let's look at a simple video option here first
# Open the videocapure socket
cap = cv2.VideoCapture(0)

while True:
	start_frame = time.time()

	# Pull an image from the open socket
	ret, img = cap.read()

# 	# Resize it
	start_resize = time.time()
# 	# img = cv2.resize(img, dim)  # Resize to the input dimension
	img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	end_resize = time.time()
	print(f"Speed of resize is: {end_resize - start_resize}")

	# Draw rectangle
	start_rect = time.time()
	cv2.rectangle(img, (x, y), (right, bottom), (125,255, 21), thickness=thickness)
	end_rect = time.time()
	print(f"Speed of drawing a rectangle is: {end_rect - start_rect}")

	# Show the image (requires keypress function to open)
	if cv2.waitKey(1) == ord('q'):
		break

	# Display image to user
	cv2.imshow('Lancaster AI Rocks', img)

	end_frame = time.time()
	print(f"Speed per frame is: {end_frame - start_frame}")



# Let's do just one image and read it from disk
# start_frame = time.time()
# img = cv2.imread("dog-cycle-car.png")

# img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# cv2.rectangle(img, (x, y), (right, bottom), (125,255, 21), thickness=thickness)

# cv2.imwrite('sample.jpg', img)
# end_frame = time.time()
# print(f"Speed is: {end_frame - start_frame}")

