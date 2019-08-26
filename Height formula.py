#print ("hello world");
#payload = {
#	"first_name": "Drake",
#	"last_name": "Gang",
#	"email": "drakegang@gmail.com",
#	"mmt": "70",
#	"user_height": "76",
#	"pin_number": "456789"
#}

#r = requests.post('http://localhost:3003/hey', json=payload)
#print(r)
#print(r.text)

print('enter your height in feet first and then add your inches after:')
x = int(input('Please enter your height in feet: '))
y = int(input('Please enter your remainding height in inches:  '))

standing_height = (((x*12)+ y) / 4) + 9
sitting_height = (((x*12) + y )/2) + 8
height = ((x*12) + y )

print('height in inches: ', height , 'standing height: ', standing_height, 'Sitting height: ', sitting_height)