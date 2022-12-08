# Drowsyness_detection

It is Iot project using Rasberry pi that alerts the driver when he/she is closes their eye.

# used
  1. Tensorflow
  2. OpenCV
  3. Rasberry Pi
  4. Dlib
  
# process
  1. A python script running in Laptop is made as Server waiting for request.
  2. Camera is connected to Rasberry pi and made it client.
  3. each frame is send to the server.
  4. each frame is processed, checks if driver is drowssy or not and signal is sent back to client.
  5. Client receives the signal and makes alaram based on signal.
  
  
for demo purpose Youtube link https://youtu.be/IXXP6BruV34
