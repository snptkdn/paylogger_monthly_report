import requests
import create_amount_per_category
import create_amount_per_day

create_amount_per_day.create()
create_amount_per_category.create()

image_day = open('amount_per_day.png', 'rb')
image_caregory = open('amount_per_category.png', 'rb')

data = {'content': 'Here, Its Stats!'}
r = requests.post('https://discord.com/api/webhooks/1057715879074332803/otaAwjfRD4wdDPYHYq7r5XUQuYGX2KTz9JccFYnZ4iJ2YfKmSjFPslBORlM8T66W7XB1', json=data)

files = { 'param_name': ('amount_per_day.jpg', image_day, 'image/jpeg') }
data = {'another_key': 'another_value'}
r = requests.post('https://discord.com/api/webhooks/1057715879074332803/otaAwjfRD4wdDPYHYq7r5XUQuYGX2KTz9JccFYnZ4iJ2YfKmSjFPslBORlM8T66W7XB1', files=files, data=data)

files = { 'param_name': ('amount_per_category.jpg', image_caregory, 'image/jpeg') }
data = {'another_key': 'another_value'}
r = requests.post('https://discord.com/api/webhooks/1057715879074332803/otaAwjfRD4wdDPYHYq7r5XUQuYGX2KTz9JccFYnZ4iJ2YfKmSjFPslBORlM8T66W7XB1', files=files, data=data)
