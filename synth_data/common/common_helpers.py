def format_seconds(seconds: float) -> str:
    '''
    This function takes an argument, in seconds, and returns a formatted string representing that duration of time
    '''

    days = int(seconds / 86400)
    hours = int(seconds % 86400 / 3600)
    minutes = int(seconds % 86400 % 3600 / 60)
    seconds = int(seconds % 86400 % 3600 % 60)

    return f"{days} d {hours} h {minutes} m {seconds} s"
