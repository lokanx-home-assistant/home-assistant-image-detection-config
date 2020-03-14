#!/usr/bin/env python3.6

directory = data.get('directory')
directory2 = None
append_today_subdirectory = data.get('append_today_subdirectory')
logger.debug("Append Today Subdirectory: {}".format(append_today_subdirectory))
if (append_today_subdirectory):
    originalDirectory = directory
    now = datetime.datetime.now()
    year = "{}".format(now.year)
    month = "{}".format(now.month)
    if (now.month < 10):
        month = "0{}".format(now.month)
    day = "{}".format(now.day)
    if (now.day < 10):
        day = "0{}".format(now.day)
    directory = originalDirectory + "/" + year + month + day
    tomorrow = now + datetime.timedelta(days=1)
    year2 = "{}".format(tomorrow.year)
    month2 = "{}".format(tomorrow.month)
    if (tomorrow.month < 10):
        month2 = "0{}".format(tomorrow.month)
    day2 = "{}".format(tomorrow.day)
    if (tomorrow.day < 10):
        day2 = "0{}".format(tomorrow.day)
    directory2 = originalDirectory + "/" + year2 + month2 + day2
    
logger.debug("About to create directory: {}".format(directory))
if not os.path.exists(directory):
    os.makedirs(directory)
    logger.info("Directory created: {}".format(directory))
if not directory2 is None:
    if not os.path.exists(directory2):
        os.makedirs(directory2)
        logger.info("Directory created: {}".format(directory2))