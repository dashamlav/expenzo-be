from rest_framework.throttling import UserRateThrottle


class DownloadCsvThrottle(UserRateThrottle):
    rate = '4/minute'