# contants, variables and code complexity

velocity = 61
car_local = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# -------------

car_high_speed_at_radar_1 = velocity > RADAR_1
car_at_radar_1 = car_local >= (LOCAL_1 - RADAR_RANGE) and \
    car_local <= (LOCAL_1 - RADAR_RANGE)

if car_high_speed_at_radar_1:
    print('High velocity.')

if car_at_radar_1:
    print('Car at Radar 1.')

if car_at_radar_1 and car_high_speed_at_radar_1:
    print('Ticketed car.')