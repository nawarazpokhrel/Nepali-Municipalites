# Nepali Municipalities
[![Downloads](https://static.pepy.tech/personalized-badge/nepali-municipality?period=total&units=international_system&left_color=black&right_color=yellowgreen&left_text=Downloads)](https://pepy.tech/project/nepali-municipality)


This is a simple and small python package contributed by me to get all list of municipalities of Nepal based on given districts of Nepal on latest version now you can autocomplete other info when municipalities name is given.

# Contents
Installation
Use the package manager pip to install nepal-municipalities.


To Autocomplete all info based on municipalities name provided
for example if you provide municipalities names then rest of district and province will be autocompleted.

```python
from nepali_municipalities import NepalMunicipality

print(NepalMunicipality().all_data_info('Kathmandu'))
[{'province': 'Province 3', 'country': 'Nepal', 'id': 311, 'district': 'Kathmandu', 'name': 'Kathmandu'}]
```

**If No matching municipalities are supplied The Exception is thrown as below**
``` python
No matching info for provided municipalities try changing spelling or try another name.
```



**To get list of all districts of Nepal**

```python
from nepali_municipalities import NepalMunicipality

print(NepalMunicipality().all_districts())
# ['Bhojpur', 'Dhankuta', 'Ilam', 'Jhapa', ......]

```

To get list of all municipalities of Nepal based on District provided.

```python
from nepali_municipalities import NepalMunicipality

print(NepalMunicipality('Kathmandu').all_municipalities())
# ['Kathmandu', 'Kageshwori Manohara', 'Kirtipur', 'Gokarneshwor', 'Chandragiri', 'Tokha', 'Tarkeshwor', 'Dakchinkali', 'Nagarjun', 'Budhanilkantha', 'Shankharapur']

print(NepalMunicipality('Kaski').all_municipalities())
```


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#Update on new version
Autocomplete 
This version has major update as you can autocomplete all remaining fields when municipalities name is provided.
you can now use [Nepali Municipalities](https://nepali-municipalities.herokuapp.com/api/docs/) API too.


## License
[MIT](https://choosealicense.com/licenses/mit/)
