May  7 22:39:33 wxpi4b systemd[1]: Started LSB: weewx weather system.
May  7 22:39:33 wxpi4b weewx[1976] INFO user.sdr: driver version is 0.77
May  7 22:39:33 wxpi4b weewx[1976] INFO user.sdr: sensor map is {'outTemp': 'temperature.71.FOWH65BPacket', 'windSpeed': 'wind_speed.71.FOWH65BPacket', 'UV': 'uv_index.71.FOWH65BPacket', 'light': 'light.71.FOWH65BPacket', 'outBatteryStatus': 'battery.71.FOWH65BPacket', 'outHumidity': 'humidity.71.FOWH65BPacket', 'windDir': 'wind_dir.71.FOWH65BPacket', 'windGust': 'wind_gust.71.FOWH65BPacket', 'rain_total': 'rain_total.71.FOWH65BPacket', 'inTemp': 'temperature.233.FOWH32BPacket', 'inHumidity': 'humidity.233.FOWH32BPacket', 'barometer': 'pressure.233.FOWH32BPacket', 'inTempBatteryStatus': 'battery.233.FOWH32BPacket'}
May  7 22:39:33 wxpi4b weewx[1976] INFO user.sdr: deltas is {'rain': 'rain_total', 'strikes': 'strikes_total'}
May  7 22:39:33 wxpi4b weewx[1976] INFO user.sdr: startup process 'rtl_433 -f 868M -s 1024k -M utc -F json -R 78'
May  7 22:39:33 wxpi4b weewx[1976] DEBUG user.sdr: start async reader for stdout-thread
May  7 22:39:33 wxpi4b weewx[1976] DEBUG user.sdr: start async reader for stderr-thread
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdTimeSynch
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdTimeSynch
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service user.filepile.FilePile
May  7 22:39:33 wxpi4b weewx[1976] INFO user.filepile: Using /home/pi/pmdata.txt with the 'METRICWX' unit system
May  7 22:39:33 wxpi4b weewx[1976] INFO user.filepile: Label map is {'pm2_5': 'pm2_5', 'pm10_0': 'pm10_0'}
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service user.filepile.FilePile
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdConvert
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: StdConvert target unit is 0x11
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdConvert
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdCalibrate
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdCalibrate
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdQC
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdQC
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.wxservices.StdWXCalculate
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.wxservices: The following values will be calculated: pressure=prefer_hardware, altimeter=prefer_hardware, appTemp=prefer_hardware, barometer=prefer_hardware, beaufort=prefer_hardware, cloudbase=prefer_hardware, dewpoint=prefer_hardware, ET=prefer_hardware, heatindex=prefer_hardware, humidex=prefer_hardware, inDewpoint=prefer_hardware, maxSolarRad=prefer_hardware, rainRate=prefer_hardware, windchill=prefer_hardware, windrun=prefer_hardware
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.wxservices: The following algorithms will be used for calculations: altimeter=aaASOS, maxSolarRad=RS
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.wxservices.StdWXCalculate
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service user.weather34.Weather34RealTime
May  7 22:39:33 wxpi4b /weewxd: w34rt: service version is 0.0.5
May  7 22:39:33 wxpi4b /weewxd: w34rt: output goes to /var/www/html/weewx/weather34/w34realtime.txt
May  7 22:39:33 wxpi4b /weewxd: w34rt: 'None' values will be displayed as NULL
May  7 22:39:33 wxpi4b /weewxd: w34rt: units will be displayed as METRICWX
May  7 22:39:33 wxpi4b /weewxd: w34rt: zambretti forecast: False
May  7 22:39:33 wxpi4b /weewxd: w34rt: Failed to open config file or create dictionary: /var/www/html/weewx/weather34/settings1.php, Error: name 'reduce' is not defined
May  7 22:39:33 wxpi4b /weewxd: w34rt: Weather34 RetainLoopValues in cache is: True
May  7 22:39:33 wxpi4b /weewxd: w34rt: binding is loop
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service user.weather34.Weather34RealTime
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdArchive
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: Archive will use data binding wx_binding
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: Record generation will be attempted in 'hardware'
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: Using archive interval of 300 seconds (specified in weewx configuration)
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Use LOOP data in hi/low calculations: 1
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdArchive
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdStationRegistry
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: StationRegistry: Station will be registered.
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdStationRegistry
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdWunderground
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: Wunderground: Posting not enabled.
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdWunderground
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdPWSweather
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: PWSWeather: Data for station ISTEEPLE2 will be posted
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdPWSweather
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdCWOP
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: CWOP: Posting not enabled.
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdCWOP
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdWOW
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: WOW: Data for station 64226802 will be posted
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdWOW
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.restx.StdAWEKAS
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.restx: AWEKAS: Posting not enabled.
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.restx.StdAWEKAS
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdPrint
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdPrint
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Loading service weewx.engine.StdReport
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Finished loading service weewx.engine.StdReport
May  7 22:39:33 wxpi4b weewx[1976] INFO __main__: Starting up weewx version 4.0.0
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.engine: Station does not support reading the time
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: Using binding 'wx_binding' to database 'weewx.sdb'
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.manager: Starting backfill of daily summaries
May  7 22:39:33 wxpi4b weewx[1976] INFO weewx.engine: Starting main packet loop.
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:39:33 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:39:36 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:39:39 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:39:42 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:39:45 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:39:48 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:39:45", "model" : "Fine Offset WH65B", "id" : 71, "temperature_C" : 14.900, "humidity" : 73, "wind_dir_deg" : 84, "wind_speed_ms" : 0.064, "gust_speed_ms" : 0.510, "rainfall_mm" : 1238.504, "uv" : 1, "uvi" : 0, "light_lux" : 0.000, "battery" : "OK", "mic" : "CRC"}\n']
May  7 22:39:48 wxpi4b weewx[1976] DEBUG user.sdr: packet={'outTemp': 14.9, 'windSpeed': 0.064, 'UV': 0.0, 'light': 0.0, 'outBatteryStatus': 0, 'outHumidity': 73.0, 'windDir': 84.0, 'windGust': 0.51, 'rain_total': 1238.504, 'dateTime': 1588887585, 'usUnits': 17}
May  7 22:39:51 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:39:56 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:39:53", "model" : "Fineoffset-WH32B", "id" : 233, "temperature_C" : 20.200, "humidity" : 55, "pressure_hPa" : 1013.100, "battery" : "LOW", "mic" : "CHECKSUM"}\n']
May  7 22:39:56 wxpi4b weewx[1976] DEBUG user.sdr: packet={'inTemp': 20.2, 'inHumidity': 55.0, 'barometer': 1013.1, 'inTempBatteryStatus': 1, 'dateTime': 1588887593, 'usUnits': 16}
May  7 22:39:59 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:04 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:40:01", "model" : "Fine Offset WH65B", "id" : 71, "temperature_C" : 14.900, "humidity" : 73, "wind_dir_deg" : 84, "wind_speed_ms" : 0.191, "gust_speed_ms" : 0.510, "rainfall_mm" : 1238.504, "uv" : 2, "uvi" : 0, "light_lux" : 0.000, "battery" : "OK", "mic" : "CRC"}\n']
May  7 22:40:04 wxpi4b weewx[1976] DEBUG user.sdr: packet={'outTemp': 14.9, 'windSpeed': 0.191, 'UV': 0.0, 'light': 0.0, 'outBatteryStatus': 0, 'outHumidity': 73.0, 'windDir': 84.0, 'windGust': 0.51, 'rain_total': 1238.504, 'dateTime': 1588887601, 'usUnits': 17}
May  7 22:40:07 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:10 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:13 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:16 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:20 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:40:17", "model" : "Fine Offset WH65B", "id" : 71, "temperature_C" : 14.900, "humidity" : 73, "wind_dir_deg" : 340, "wind_speed_ms" : 0.382, "gust_speed_ms" : 1.020, "rainfall_mm" : 1238.504, "uv" : 2, "uvi" : 0, "light_lux" : 0.000, "battery" : "OK", "mic" : "CRC"}\n']
May  7 22:40:20 wxpi4b weewx[1976] DEBUG user.sdr: packet={'outTemp': 14.9, 'windSpeed': 0.382, 'UV': 0.0, 'light': 0.0, 'outBatteryStatus': 0, 'outHumidity': 73.0, 'windDir': 340.0, 'windGust': 1.02, 'rain_total': 1238.504, 'dateTime': 1588887617, 'usUnits': 17}
May  7 22:40:20 wxpi4b weewx[1976] INFO weewx.manager: Added record 2020-05-07 22:40:00 BST (1588887600) to database 'weewx.sdb'
May  7 22:40:20 wxpi4b weewx[1976] INFO weewx.manager: Added record 2020-05-07 22:40:00 BST (1588887600) to daily summary in 'weewx.sdb'
May  7 22:40:20 wxpi4b weewx[1976] DEBUG weewx.reportengine: Running reports for latest time in the database.
May  7 22:40:20 wxpi4b weewx[1976] DEBUG weewx.reportengine: Running report 'SeasonsReport'
May  7 22:40:20 wxpi4b weewx[1976] DEBUG weewx.reportengine: Found configuration file /home/weewx/skins/Seasons/skin.conf for report 'SeasonsReport'
May  7 22:40:20 wxpi4b weewx[1976] DEBUG weewx.cheetahgenerator: Using search list ['weewx.cheetahgenerator.Almanac', 'weewx.cheetahgenerator.Station', 'weewx.cheetahgenerator.Current', 'weewx.cheetahgenerator.Stats', 'weewx.cheetahgenerator.UnitInfo', 'weewx.cheetahgenerator.Extras']
May  7 22:40:20 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:40:21 wxpi4b weewx[1976] INFO weewx.restx: StationRegistry: Published record 2020-05-07 22:40:00 BST (1588887600)
May  7 22:40:21 wxpi4b weewx[1976] INFO weewx.restx: PWSWeather: Published record 2020-05-07 22:40:00 BST (1588887600)
May  7 22:40:22 wxpi4b weewx[1976] INFO weewx.cheetahgenerator: Generated 8 files for report SeasonsReport in 1.90 seconds
May  7 22:40:22 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:40:23 wxpi4b weewx[1976] INFO weewx.imagegenerator: Generated 15 images for report SeasonsReport in 0.60 seconds
May  7 22:40:23 wxpi4b weewx[1976] INFO weewx.reportengine: Copied 5 files to /var/www/html/weewx
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Report 'SmartphoneReport' not enabled. Skipping.
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Report 'MobileReport' not enabled. Skipping.
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Report 'StandardReport' not enabled. Skipping.
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Report 'FTP' not enabled. Skipping.
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Report 'RSYNC' not enabled. Skipping.
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Running report 'Weather34Report'
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Found configuration file /home/weewx/skins/Weather34/skin.conf for report 'Weather34Report'
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.cheetahgenerator: Using search list ['weewx.cheetahgenerator.Almanac', 'weewx.cheetahgenerator.Station', 'weewx.cheetahgenerator.Current', 'weewx.cheetahgenerator.Stats', 'weewx.cheetahgenerator.UnitInfo', 'weewx.cheetahgenerator.Extras', 'user.stats.MyStats', 'user.lastrain.lastRainTags']
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:40:23 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:23 wxpi4b weewx[1976] INFO weewx.cheetahgenerator: Generated 2 files for report Weather34Report in 0.53 seconds
May  7 22:40:23 wxpi4b weewx[1976] INFO weewx.reportengine: Copied 0 files to /var/www/html/weewx/weather34/
May  7 22:40:23 wxpi4b weewx[1976] DEBUG weewx.reportengine: Running report 'w34Highcharts'
May  7 22:40:24 wxpi4b weewx[1976] DEBUG weewx.reportengine: Found configuration file /home/weewx/skins/w34Highcharts/skin.conf for report 'w34Highcharts'
May  7 22:40:24 wxpi4b weewx[1976] DEBUG weewx.cheetahgenerator: Using search list ['weewx.cheetahgenerator.Almanac', 'weewx.cheetahgenerator.Station', 'weewx.cheetahgenerator.Current', 'weewx.cheetahgenerator.Stats', 'weewx.cheetahgenerator.UnitInfo', 'weewx.cheetahgenerator.Extras', 'user.w34highchartsSearchX.w34highcharts_temp_week', 'user.w34highchartsSearchX.w34highcharts_bar_rain_week', 'user.w34highchartsSearchX.w34highcharts_wind_week', 'user.w34highchartsSearchX.w34highcharts_solar_week', 'user.w34highchartsSearchX.w34highcharts_indoor_derived_week', 'user.w34highchartsSearchX.w34highcharts_wind_rose_week', 'user.w34highchartsSearchX.w34highchartsYear']
May  7 22:40:24 wxpi4b weewx[1976] DEBUG weewx.manager: Daily summary version is 2.0
May  7 22:40:24 wxpi4b weewx[1976] DEBUG weewx.cheetahgenerator: Skip 'year.json': last_mod=1588887031.162923 age=593.4508907794952 stale=600
May  7 22:40:24 wxpi4b weewx[1976] INFO weewx.cheetahgenerator: Generated 6 files for report w34Highcharts in 0.60 seconds
May  7 22:40:24 wxpi4b weewx[1976] INFO weewx.reportengine: Copied 0 files to /var/www/html/weewx/weather34/w34highcharts
May  7 22:40:26 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:28 wxpi4b systemd[1]: Started Session c4361 of user pi.
May  7 22:40:28 wxpi4b systemd[1]: session-c4361.scope: Succeeded.
May  7 22:40:29 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:30 wxpi4b weewx[1976] DEBUG weewx.restx: WOW: Failed upload attempt 1: timed out
May  7 22:40:32 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:36 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:40:33", "model" : "Fine Offset WH65B", "id" : 71, "temperature_C" : 14.900, "humidity" : 73, "wind_dir_deg" : 75, "wind_speed_ms" : 1.084, "gust_speed_ms" : 1.530, "rainfall_mm" : 1238.504, "uv" : 2, "uvi" : 0, "light_lux" : 0.000, "battery" : "OK", "mic" : "CRC"}\n']
May  7 22:40:36 wxpi4b weewx[1976] DEBUG user.sdr: packet={'outTemp': 14.9, 'windSpeed': 1.084, 'UV': 0.0, 'light': 0.0, 'outBatteryStatus': 0, 'outHumidity': 73.0, 'windDir': 75.0, 'windGust': 1.53, 'rain_total': 1238.504, 'dateTime': 1588887633, 'usUnits': 17}
May  7 22:40:39 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:42 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:45 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:45 wxpi4b weewx[1976] DEBUG weewx.restx: WOW: Failed upload attempt 2: timed out
May  7 22:40:48 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:40:51 wxpi4b weewx[1976] ERROR weewx.restx: WOW: Bad login; waiting 60.0 minutes then retrying
May  7 22:40:52 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:40:49", "model" : "Fine Offset WH65B", "id" : 71, "temperature_C" : 14.900, "humidity" : 73, "wind_dir_deg" : 67, "wind_speed_ms" : 0.510, "gust_speed_ms" : 0.510, "rainfall_mm" : 1238.504, "uv" : 2, "uvi" : 0, "light_lux" : 0.000, "battery" : "OK", "mic" : "CRC"}\n']
May  7 22:40:52 wxpi4b weewx[1976] DEBUG user.sdr: packet={'outTemp': 14.9, 'windSpeed': 0.51, 'UV': 0.0, 'light': 0.0, 'outBatteryStatus': 0, 'outHumidity': 73.0, 'windDir': 67.0, 'windGust': 0.51, 'rain_total': 1238.504, 'dateTime': 1588887649, 'usUnits': 17}
May  7 22:40:56 wxpi4b weewx[1976] DEBUG user.sdr: lines=['{"time" : "2020-05-07 21:40:53", "model" : "Fineoffset-WH32B", "id" : 233, "temperature_C" : 20.200, "humidity" : 55, "pressure_hPa" : 1012.900, "battery" : "LOW", "mic" : "CHECKSUM"}\n']
May  7 22:40:56 wxpi4b weewx[1976] DEBUG user.sdr: packet={'inTemp': 20.2, 'inHumidity': 55.0, 'barometer': 1012.9, 'inTempBatteryStatus': 1, 'dateTime': 1588887653, 'usUnits': 16}
May  7 22:40:59 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
May  7 22:41:02 wxpi4b weewx[1976] DEBUG user.sdr: lines=[]
