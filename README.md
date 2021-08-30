# Nepali Municipalities
[![Downloads](https://static.pepy.tech/personalized-badge/nepali-municipality?period=total&units=international_system&left_color=black&right_color=yellowgreen&left_text=Downloads)](https://pepy.tech/project/nepali-municipality)


This is a simple and small python package contributed by me to get all list of municipalities of Nepal based on given districts of Nepal.
# Contents
Installation
Use the package manager pip to install nepal-municipalities.

To get list of all districts of Nepal

```python
from src.nepali_municipalities import NepalMunicipality

print(NepalMunicipality().all_districts())
# ['Bhojpur', 'Dhankuta', 'Ilam', 'Jhapa', ......]

```

To get list of all municipalities of Nepal

```python
from src.nepali_municipalities import NepalMunicipality

print(NepalMunicipality('Kathmandu').all_municipalities())
# ['Kathmandu', 'Kageshwori Manohara', 'Kirtipur', 'Gokarneshwor', 'Chandragiri', 'Tokha', 'Tarkeshwor', 'Dakchinkali', 'Nagarjun', 'Budhanilkantha', 'Shankharapur']

print(NepalMunicipality('Kaski').all_municipalities())
```


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
