# Drone-Reconnaissance
Trying to recreate the functionality of the Ring Drone using my Tello drone and Python

Main Idea:

Make a mobile app, when I click 'Activate Security Mode':
  When:
    Ring doorbell detects motion
  Do:
    send request to NGROK URL through IFTTT
    Ngrok sends this to localhost http server
    Activate Reconnaissance:
      Auto switch to drone WiFi
      Take off, fly drone around predefined loop sending video feed to mobile app
      Land drone, reconnect to WiFi
      NGROK reconnects, ready another request
      
Could this be the most productive way I have ever procrastinated? 
Yes.
