import gpxpy
import gpxpy.gpx
import time


class GPSStats(object):
    def __init__(self, gpx_file):
        self.gpx = gpxpy.parse(open(gpx_file, 'r'))
        self.__minutes_duration = None
        self.__seconds_duration = None
        for track in self.gpx.tracks:

            last_point_time = None
            added_in_sec = 0
            self.set_minutes_duration(track)
            self.set_seconds_duration(track)
            for segment in track.segments:

                for point in segment.points:
                    minutes_added = 0
                    seconds_added = 0

                    if last_point_time:
                        diff = point.time - last_point_time
                        diff_m_s = divmod(diff.days * 86400 + diff.seconds, 60)
                        if diff_m_s[0] >= 1:
                            minutes_added = diff_m_s[0]
                        if diff_m_s[1] >= 15:
                            seconds_added = diff_m_s[1]
                        if point.time > last_point_time:
                            last_point_time = point.time
                    else:
                        last_point_time = point.time

                    added_in_sec += ( minutes_added * 60 ) + seconds_added
            seconds_overall_without_added = self.get_overall_seconds_duration() - added_in_sec
            print time.strftime('%H:%M:%S', time.gmtime(self.get_overall_seconds_duration()))
            print time.strftime('%H:%M:%S', time.gmtime(seconds_overall_without_added))
            length_2d = self.gpx.length_2d()/1000
            time_normal = self.get_minutes_duration() + ( 0.01 * self.get_seconds_duration() )
            # time_diff = seconds_overall_without_added + ( 0.01 * self.get_seconds_duration() )
            avg = ( length_2d /
                time_normal
                ) * 60
            print "avg - normal: ", avg

            # avg = ( length_2d /
                # seconds_overall_without_added
                # ) * 60
            # print "avg - normal: ", avg

    def set_minutes_duration(self, track):
        self.__minutes_duration = track.get_duration()/60

    def set_seconds_duration(self, track):
        self.__seconds_duration = (
            (track.get_duration()/60)*60 - track.get_duration())

    def get_minutes_duration(self):
        return self.__minutes_duration

    def get_seconds_duration(self):
        return self.__seconds_duration

    def get_overall_seconds_duration(self):
        return self.get_minutes_duration() * 60 + self.get_seconds_duration()


# gpsstat1 = GPSStats('20151105_073311.gpx')
# print gpsstat1.get_overall_seconds_duration()

gpsstat2 = GPSStats('20151112_054455.gpx')
print gpsstat2.get_overall_seconds_duration()
