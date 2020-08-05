# Introduction
This project was implemented in Django and Python

This project visualizes the process of 'PTP Time Synchronization' in a Linux environment.

# Environment
Python version : 3.6.9

Django version : 2.0.13 


# Precondition
You must install the virtual environment first, and then run the program.

The process of installing the virtual environment is as follows:


```
$ mkdir djangoproject
$ cd djangoproject
```

When creating a virtual environment named **'myvenv'**, execute the following command.

```
$ python3 -m venv myvenv
$ source myvenv/bin/activate 
```

If the (myvenv) prefix is prefixed to the console prompt, you can see that the virtual environment has started.
And then, Install **Django** 

```
(myvenv) ~$ pip install django~=2.0.0
```


# Configuration
## Run server, execute the following command.
```sh
python manage.py runserver
```


![Screenshot from 2020-08-04 19-19-18](https://user-images.githubusercontent.com/33818414/89283036-6f08d400-d687-11ea-94d8-607c9316a095.png)

- Default port number : 8000




![Screenshot from 2020-08-04 16-18-15](https://user-images.githubusercontent.com/33818414/89283130-98296480-d687-11ea-92e9-5e831f12e479.png)

- This is the main screen.




![Screenshot from 2020-08-04 16-18-53](https://user-images.githubusercontent.com/33818414/89283226-c27b2200-d687-11ea-931b-639393e2a436.png)

- This is the screen after reading the csv file.




![Screenshot from 2020-08-04 16-19-01](https://user-images.githubusercontent.com/33818414/89283275-d9ba0f80-d687-11ea-84f9-06ca2d4745a3.png)

- This is the screen result of the showdata page.
- Data is output 10 per field.




# Graph 1


![Peek 2020-08-04 16-26](https://user-images.githubusercontent.com/33818414/89283392-0bcb7180-d688-11ea-9c16-f9d0292dfe26.gif)





# Graph 2


![Peek 2020-08-04 16-25](https://user-images.githubusercontent.com/33818414/89283379-079f5400-d688-11ea-9d73-d7aa773780ce.gif)






