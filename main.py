n_days = int(input())
n_hour = n_days * 60
n_second = n_days * 60 * 60
v_hour = 38241                            # Miles per hour.
v_second = v_hour / 3600                  # Miles per second.
length = v_second*n_second                # In miles.

rd_wv_spd_second = 299_792_458            # In meters per second.
rd_wv_spd_hour = rd_wv_spd_second * 3600  # In meters per hour
cmmnctn_dl = n_hour / rd_wv_spd_hour
print(f'in miles: {length}, \n'
      f'in kilometers: {length * 1.609_344}, \n'
      f'in astronomical units: {length*1.609_344*149_597_870.7}, \n'
      f'delay: {cmmnctn_dl}')