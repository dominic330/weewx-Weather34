# Troubleshooting Guide

* Before sumitting a new issue, please look through the open and closed issue logs to see if there is previous history of the problem you encountered.
* When submitting an issue it will help us to deal with your problem more quickly if you can supply the following information and run the listed procedures: -
        
    1. Are your WeeWX installation and webserver on the same machine?
    
    2. cd to your w34hicharts/scripts folder and run **cat plots_config.js**
    
    3. run **cat /var/log/syslog | grep weewx**
    
    4. check your webserver error log
  
    5. cd to your webserver /weewx folder and run **ls -l weather34**
    
    6. cd to your /weather34 folder and run **ls -lR w34highcharts**
    
    7. run **ls -l /home/weewx/bin** (or **ls -l /usr/share/weewx** or **ls -l /Users/Shared/weewx/bin/** depending on your WeeWX setup)
    
    8. and finally cd to your /skins folder and run **ls -lR w34Highcharts-day**
        
    There is no need to save the various outputs to a file, just cut and paste each one in to seperate issue log comment windows indicating the type of output. 
        
