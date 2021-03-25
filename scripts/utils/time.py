import re
from datetime import datetime
import sys
import logging

time_patterns_set = {
    "%Y-%m-%d", "%Y-%m-%dT%H:%M", \
        "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", \
            "%Y-%m-%dT%H:%M:%z"
}

r_time_pattern = r'[yyyy]-[mm]-[dd]T[HH]:[MM]:[SS][+/-][HHMM]'
r_time_patterns = [re.sub(r'%Y', '[yyyy]', 
                          re.sub(r'%m', '[mm]', re.sub(
                             r'%d', '[dd]', re.sub(
                                 r'%H', '[HH]', re.sub(
                                    r'%M', '[MM]', re.sub(
                                        r'%S', '[SS]', re.sub(
                                            r'%z', '[+-][HHMM]', x
                                        )
                                    ) 
                                 )
                             ) 
                          )
                        )
                    )
                for x in time_patterns_set]
# datetime.strptime("2012-11-01T04:16:13+0400", "%Y-%m-%dT%H:%M:%S%z")
# 2012-11-01 04:16:13+04:00


def validate_date(date, param_name):
    for pattern in time_patterns_set:
        try:
            valid_date = datetime.strptime(date, pattern)
            return valid_date
        except ValueError:
            pass 
    else:
        logging.error(f'No time pattern matched for {param_name}.' + \
                      'Use -h flag to see the whole pattern')
        sys.exit()