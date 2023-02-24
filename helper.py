################################################################################
#
# Helper
#
################################################################################

import os, datetime


#===============================================================================
# Logging func
#-------------------------------------------------------------------------------

def logger(message, level='DEBUG', func=__name__, file='default', stdout=False):
    if file == 'default':
        file = os.path.splitext(os.path.realpath(__file__))[0] + '.log'
    if stdout:
        print(message)

    log = (
        f'{datetime.datetime.now().astimezone(datetime.timezone.utc):%m-%d-%Y @ %H:%M:%S.%f} | '
        f'{level:^10} | '
        f'{func:^30} | '
        f'{message}'
    )
    with open(file, 'a') as logger:
        logger.write(log + '\n')