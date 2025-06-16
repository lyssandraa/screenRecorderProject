import pyautogui, cv2, numpy as np

# Set size of video; below is full HD
resolution = (1920, 1080)

# Choose video compression format (codec)
# XVID is a common format for .avi files
codec = cv2.VideoWriter_fourcc(*"XVID")

#Set name of the output video file
filename = "Recording.avi"

# Set frame rate (fps = frame per second)
# Higher fps gives smoother video 
fps = 60.0

# Create a video writer object (out) that will save 
# fraames to Recording.avi using the specified settings
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Preview live window
# Create an empty window, named Live
# WINDOW_NORMAL means window can be resized
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize window to 480x270 pixels 
cv2.resizeWindow("Live", 480, 270)

while True:

    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR to RGB (cv uses BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Display the recording screen
    cv2.imshow("Live", frame)

    # Stop recording when "x" pressed
    if cv2.waitKey(1) == ord("x"):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()