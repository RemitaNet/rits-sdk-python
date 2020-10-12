from datetime import datetime


class Timestamp:

    def dateTimeObj(self, dateTimeObj):



        year = dateTimeObj.year
        month = dateTimeObj.month
        day = dateTimeObj.day
        hour = dateTimeObj.hour
        min = dateTimeObj.minute
        sec = dateTimeObj.second

        requestid = str(year) + '-' + str(month) + '-' + str(day) + 'T' + str(hour) + ':' + str(min) + ':' + str(
            sec) + '+000000'
        return requestid






