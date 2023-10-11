import cv2
import numpy as np

# Open the video source
cap = cv2.VideoCapture("dog.mp4")

# Read the first frame
_, frame = cap.read()

# Create a video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame.shape[1], frame.shape[0]))

while(1):
    # Read the next frame
    _, frame = cap.read()
    
    # Break the loop when the video ends
    if frame is None:
        break
    
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensitivity = 15
    lowe_white = np.array([0, 0, 250 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])
    
    # Create a mask to distinguish white objects
    mask = cv2.inRange(hsv, lowe_white, upper_white)
    
    # Generate the processed frame using the mask
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Write the processed frame
    out.write(res)
    
    # Show the frame
    cv2.imshow("frame", frame)
    #cv2.imshow("Mask", mask)
    cv2.imshow("result", res)
    
    # Break the loop when 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the video writer
out.release()

# Close the windows
cv2.destroyAllWindows()
