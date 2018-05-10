import base64
cipher = 'N9aqFjeqE6oryUioNwGp2aLwMoXRBLIcH4eAYuWlO39BXbKDOK6ph2VpoL+e67CA43l+cytz51cZmCRX53kdShO9bCDgw3MsNY72DhAj4xU='
# old = 'me";s:5:"1dmin";'
# new = 'me";s:5:"admin";'

cipher = base64.b64decode(cipher)
cipher = cipher[:9] +  chr(ord(cipher[9]) ^ ord('1') ^ ord('a')) + cipher[10:]

print(base64.b64encode(cipher))