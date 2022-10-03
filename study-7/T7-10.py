import time


class Time:
    def __init__(self):
        current_time = time.time()
        total_seconds = int(current_time)
        total_minutes = total_seconds // 60
        total_hours = total_minutes // 60

        self.__hour = total_hours % 24
        self.__minute = total_minutes % 60
        self.__second = total_seconds % 60

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def set_time(self, current_time):
        total_seconds = int(current_time)
        total_minutes = total_seconds // 60
        total_hours = total_minutes // 60

        self.__hour = total_hours % 24
        self.__minute = total_minutes % 60
        self.__second = total_seconds % 60


def main():
    timer = Time()
    print("Current time is {0}:{1}:{2}".format(timer.get_hour(),
                                               timer.get_minute(),
                                               timer.get_second()))
    time0 = eval(input("Enter the elapsed time:"))
    timer.set_time(time0)
    print("The hour:minute:second for the elapsed time is {0}:{1}:{2}".format(timer.get_hour(),
                                                                              timer.get_minute(),
                                                                              timer.get_second()))


main()
