# python-earth-view

[Google Earth View](https://earthview.withgoogle.com/) is a gallery of at least 2,604 visually appealing satellite images. Each has a resolution of 1800x1200, making them suitable wallpapers or placeholder images. For example, there's a [Chrome extension](https://chrome.google.com/webstore/detail/earth-view-from-google-ea/bhloflhklmhfpedakmangadcdofhnnoh) that displays a new Earth View image each time you open a new tab, and a [GNOME extension](https://github.com/neffo/earth-view-wallpaper-gnome-extension) that regularly sets the wallpaper to a new Earth View image.

I wrote this package to make it a little bit easier to hit the ground running with Earth View images.
It provides a command-line tool and Python API that make it easy to download images and access their metadata.

## How to use

### In Python

```python
from earth_view import EarthViewImage
```
By default, initializing an EarthViewImage will download a random image:

```python
>>> my_image = EarthViewImage()
>>> print(my_image.geocode("establishment"])
Volcán Isluga National Park
```
If you want, you can request a specific image ID:

```python
# id parameter can be int or str
specific_image = EarthViewImage(1004)
```

Save it for later:

```python
# if you don't specify path, default is your current working directory
EarthViewImage().save(path="/home/user/Desktop")
```

### Command-line

The `earth-view` command makes it easy to download a new Earth View image.

```sh
# download a random image to the current directory
earth-view 

# download a specific image to your Downloads folder, overwriting if file exists
earth-view ~/Downloads --id 1004 --overwrite
```

## A word of warning

This package entirely relies on a free service hosted by Google.
At any time, Google may decide to end the service.
Enjoy it while it's here.

## Contributing

Feel free to file an issue, submit a pull request, or reach out to me directly.
I'd love to hear from you.

## License

This code is licensed under GPLv3 or any later version. See LICENSE.md for more information.
