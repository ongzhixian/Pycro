################################################################################
# Modules and functions import statements
################################################################################

from helpers.app_runtime import api_stats

################################################################################
#
################################################################################

def get_api_stats(name):
    if name not in api_stats.keys():
        api_stats[name] = 0
    return api_stats[name]

def update_api_stats(name, count = 1):
    if name not in api_stats.keys():
        api_stats[name] = 0
    api_stats[name] = api_stats[name] + count