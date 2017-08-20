# picoCTF 2017 : meta-find-me-70

**Category:** Forensics
**Points:** 70
**Solves:** 
**Description:** Find the location of the flag in the image: image.jpg. Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!

HINTS
How can images store location data? Perhaps search for GPS info on photos.


## Write-up

Running the image through http://www.verexif.com/en/index.php gives us 

```
Date/Time :2016/02/10 11:55:56
Resolution : 500 x 500
Jpeg process : Progressive
GPS Latitude :? 7º 0' 0"
GPS Longitude :? 100º 0' 0"
Comment : "Your flag is flag_2_meta_4_me_<lat>_<lon>_1c84.
Now find the GPS coordinates of this image! (Degrees only please)"
```

Following the instructions, the flag is: ```flag_2_meta_4_me_7_100_1c84```

## Other write-ups and resources

* none yet
