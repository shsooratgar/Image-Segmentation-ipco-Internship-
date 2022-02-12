# Image-Segmentation

This is my internship project at ipco company implementing an image segmentation system
The Three main methods of image segmentation are implemented

### Thresholding
This method which comes in two parts for grayscale image thresholding and color image thresholding is mostly used to detect objects from background 

In this method a threshold (global or local/adaptive) is calculated and is used to group pixels

![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Codes/Wallpapers_full_marlin.jpg)

raw adaptive thresholding :
![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Results/3866313f-9dc3-48da-b289-8dcce88f708d.jfif)

after optimization :
![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Results/a6526306-77cf-4ca0-afe5-7676cb453253.jfif)

### Edge Detection
Edge detection is mostly used to detect edges of an object between other objects

The key idea is to use first or second derivatives of a line of pixels to detect places where the 
light intensity changes

two algorithms of sobel and canny are  implemented (both use first derivative)

![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Codes/%DB%B2%DB%B0%DB%B2%DB%B0%DB%B0%DB%B6%DB%B1%DB%B7_%DB%B1%DB%B7%DB%B3%DB%B4%DB%B0%DB%B0.png)
![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Results/ee2eb400-d072-4f1c-ba9d-5ad890d5547b.jfif)

 
### Hough Transformation
hough transformation is method to detect straight lines and some other shapes in an image.

This method uses the output of an edge detector algorithm (previos part) as input

![alt text](https://github.com/shsooratgar/Image-Segmentation-ipco-Internship-/blob/main/Results/8ecabcd2-9b18-43c2-9dc1-aa54508cd1d7.jfif)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
