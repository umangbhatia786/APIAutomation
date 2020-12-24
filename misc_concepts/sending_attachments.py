import requests

base_url = 'https://petstore.swagger.io/v2'
resource = '/pet/9843217/uploadImage'

api_url = f'{base_url}{resource}'

input_file = {'file': open(r"C:\Users\Umang Bhatia\Pictures\BAJAJ FINANCE Trend.PNG", 'rb')}

upload_pet_img_res = requests.post(
    url= api_url,
    files= input_file,
    allow_redirects= False,
    timeout= 4
)

print(upload_pet_img_res.status_code)
print(upload_pet_img_res.text)