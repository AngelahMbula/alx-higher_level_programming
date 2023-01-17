#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me,server responds with mesage you got me.
curl -sX PUT -L -H "Origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
