var pathweewx = '/weewx/'             //Path from web server home location to weewx directory
var pathpws   = '/weewx/weather34/'               //Path from web server home location to weather34 directory
var pathweewxbin = '/usr/share/weewx'  //Physical path to weewx include files for wee_report_w34 if DEB installed WeeWX
var realtimefile =  pathpws   + "w34realtime.txt";    //Location of real-time data from web server
var pathjsonfiles = pathpws + "w34highcharts/json/";                    //Location weewx report output json files from home location of weewx. DO NOT CHANGE UNLESS YOU CHANGE SKIN DIRECTORY.

var dayplotsurl =   pathpws + "w34highcharts/getDayChart.php"; //Location of day reports php file from home location of pws.
var pathjsondayfiles = "json_day/";                         //Location day report output json files from home location of where wee_report_34 run. DO NOT CHANGE UNLESS YOU CHANGE SKIN DIRECTORY.
var weereportcmd = "./wee_reports_w34";                     //Command to run wee_report_34. DO NOT CHANGE.

var autoupdateinterval = 60; //This is seconds
var realtimeinterval = 10;  //This is seconds
var hide_zero_wind_barb = false; //Hide or display Zero Barb

//[0] array offset(s) to wanted real-time data(s)(can be empty),[1] array offset(s) to data's real-time units(can be empty),[2] array of unit convert function(s)(can be empty), [3] plot type, [4] plot X resolution, [5] delta value
// The (can be empty) entries then must have a plot_type that is another plot type entry with fill in values this is how to display a different plot_type when using real-time data.
var realtimeplot = {
    temperatureplot:[[2,4],[14,14],['convert_temp','convert_temp'],['temperatureplot'],[150]],
    tempallplot:[[2,4,3],[14,14,-1],['convert_temp','convert_temp',null],['tempallplot'], [150]],
    winddirplot:[[7],[13],['convert_wind'],['winddirplot'], [150]],
    windplot:[[6],[13],['convert_wind'],['windplot'],[150]],
    windallplot:[[5,40,46],[13,13,-1],['convert_wind','convert_wind',null],['windallplot'],[150]],
    barometerplot:[[10],[15],['convert_pressure'],['barometerplot'],[150]],
    rainplot:[[47,8],[16,16],['convert_rain','convert_rain'],['rainplot'],[50],[]],
    windroseplot:[[6,11],[13,-1],['convert_wind', null],['windroseplot'],[150]]
};