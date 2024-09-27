# Thermal Human Detection from UAV > 2023-08-24 2:49pm
https://universe.roboflow.com/thermal-disasters-project/thermal-human-detection-from-uav

Provided by a Roboflow user
License: CC BY 4.0

### The dataset for a conferance paper.
This dataset contains 654 selected images, from 2 datasets.
The related datasets and the image number obtained from them is:

 1. **HIT-UAV Dataset:**
Link: [HIT-UAV Dataset Link (YOLO Format)](https://www.kaggle.com/datasets/pandrii000/hituav-a-highaltitude-infrared-thermal-dataset)
selected image count: 465 images

2. **NII-CU Dataset**
Link: [NII-CU Dataset Link](https://www.nii-cu-multispectral.org)
selected image count: 189 images



The images are selected only if they are regarded as related to UAV Thermal Human Detection for Disaster Management task.
In the task, it is assumed that the themal human detection will be used in night scenarios. Hence, the images are eliminated where humans are not have higher contrast than the background (the ground is hot due to the sunlight in day scenarios).
We eliminated the mis-labeled images we have noticed.
Also, to obtain diversity among images, we tried to eliminate most of the images that are close to each other.










Related citations

	Suo, J., Wang, T., Zhang, X., Chen, H., Zhou, W., & Shi, W. (2023, April 20). HIT-UAV: A high-altitude infrared thermal dataset for Unmanned Aerial Vehicle-based object detection. Scientific Data; Nature Portfolio. https://doi.org/10.1038/s41597-023-02066-6


	Speth, S., Gonçalves, A., Rigault, B., Suzuki, S., Bouazizi, M., Matsuo, Y. & Prendinger, H. (2022) Deep Learning with RGB and Thermal Images onboard a Drone for Monitoring Operations. Journal of Field Robotics, 1- 29. https://doi.org/10.1002/rob.22082