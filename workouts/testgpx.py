import gpxpy
import gpxpy.gpx
gpx_file = open('20151105_073311.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    print "TRACK!!"
    print track.get_duration()/60 , "minutes", (track.get_duration()/60)*60 - track.get_duration()
    help(track)
    for segment in track.segments:
        print "SEGMENT!!"
        # for point in segment.points:
            # print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

#for waypoint in gpx.waypoints:
#    print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude)
#
#for route in gpx.routes:
#    print 'Route:'
#    for point in route:
#        print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)
#
## There are many more utility methods and functions:
## You can manipulate/add/remove tracks, segments, points, waypoints and routes and
## get the GPX XML file from the resulting object:
#
#print 'GPX:', gpx.to_xml()
