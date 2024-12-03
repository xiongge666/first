import pyotp

key = '6SD6S2WLRA4K7P7IXFDWUX2XDQINUWKW'
totp = pyotp.TOTP(key)
print(totp.now())