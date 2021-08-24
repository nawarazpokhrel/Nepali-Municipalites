# Nepali Municipalities

This is a simple and small python package contributed by me to get all list of municipalities of Nepal based on given districts of Nepal.
# Contents
Installation
Use the package manager pip to install nepal-municipalities.

To get list of all districts of Nepal

```python
from src.nepali_municipalities import NepalMunicipality

NepalMunicipality().all_districts()
# ['Bhojpur', 'Dhankuta', 'Ilam', 'Jhapa', 'Khotang', 'Morang', 
# 'Okhaldhunga', 'Panchthar', 'Sankhuwasabha', 'Solukhumbu', 
# 'Sunsari', 'TapleJung', 'Terhathum', 'Udayapur', 'Bara', 
# 'Dhanusha', 'Mahottari', 'Parsa', 'Rautahat', 'Saptari', 'Sarlahi', 'Siraha', 'Bhaktapur', 'Chitwan', 'Dhading', 'Dolakha', 'Kavrepalanchowk', 'Kathmandu', 'Lalitpur', 'Makwanpur', 'Nuwakot', 'Ramechhap', 
# 'Rasuwa', 'Sindhuli', 'Sindhupalchowk', 'Baglung', 'Gorkha', 
# 'Kaski', 'Lamjung', 'Manang', 'Mustang', 'Myagdi', 
# 'Nawalparasi (State 4)', 'Parbat', 'Syangja', 'Tanahun', 
# 'Arghakhanchi', 'Banke', 'Bardiya', 'Dang', 'Gulmi', 
# 'Kapilvastu', 'Nawalparasi West', 'Palpa', 'Pyuthan', 'Rolpa', 
# 'Rukum (State 5)', 'Rupandehi', 'Dailekh', 'Dolpa', 'Humla', 
# 'Jajarkot', 'Jumla', 'Kalikot', 'Mugu', 'Western Rukum', 'Salyan', 
# 'Surkhet', 'Aachham', 'Baitadi', 'Bajhang', 'Bajura', 'Dadeldhura', 
# 'Darchula', 'Doti', 'Kailali', 'Kanchanpur']

```

To get list of all municipalities of Nepal

```python
from src.nepali_municipalities import NepalMunicipality

NepalMunicipality('Kathmandu').all_municipalities()
# ['Kathmandu', 'Kageshwori Manohara', 'Kirtipur', 'Gokarneshwor', 'Chandragiri', 'Tokha', 'Tarkeshwor', 'Dakchinkali', 'Nagarjun', 'Budhanilkantha', 'Shankharapur']

```


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



I