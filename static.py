def time_am_or_pm(time):
    if time >= 12:
        if time >= 13:
            value_str = str(time)
            vales_1 = int(value_str[:2]) - 12
            data = str(vales_1) + value_str[-3:]
            return data, "PM"
        else:
            result = str(time) + " " + "PM"
            return result
    else:
        result = str(time) + " " + "AM"
        return result
