# Sunton_ESP32-8048S043


This project have not been touched ort updated in a while please check https://github.com/pixelwave/Sunton-ESP32-8048S043 for newer stuff.
or my other project https://github.com/zingo/CrazyCapyTime using this HW.



This project would be a good starting point if you want to use this devboard, just clone it
and rename it and do your own stuff.

Basic board setup and running using PlatformIO
this is based on the info found on
https://www.makerfabs.com/sunton-esp32-s3-4-3-inch-ips-with-touch.html

As it took a bit of effort to get a simple project up I thought I should
share the result so the it would be easier for other to get started.

There is basically nothing magic here just a PlatfornIO project ready to start
using based on the info and project found from a Sunton zip with a Arduino project

This will setup the Display with touch and run the LVGL demo project. As a graphic
backend it will use "GFX Library for Arduino" but it would be nice to test LovyanGFX
in the future and benchmark them.

Possible future improvemnets

 * Proper partition memory setup
 * SD Card setup
 * WIFI usage and setup, with WiFiManager?
 * BT setup
 * LittleFS setup
 * OTA
 
 But this will probably end up in other project, there is a lot of examples setting this up
 for ESP32 out there.

/ Zingo Andersen - CrazyCapy Developement director
