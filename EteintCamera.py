import picamera

def EteintCamera()
  camera=picamera.Picamera()
  camera.stop_recording()
  return
