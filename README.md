# Introduction
This project was implemented in Django and Python

This project visualizes the process of 'PTP Time Synchronization' in a Linux environment.

# Environment
Python version : 3.6.9

Django version : 2.0.13 

AWS console : Ubuntu Server 18.04 LTS


# Dockerfile
```
$ docker build -t <tag name> . 
```
After entering the docker build command, you can specify the name (tag) of the image to be created by entering the -t option.
Behind it **.** Is the Dockerfile and the path where the content is located.




# Precondition (When not using Docker)
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
nohup python manage.py runserver 0.0.0.0:8080 
```

Run it as a daemon using the **nohup** command.
Even if ssh, terminal connection is terminated, it runs without problem.


### Main Page

![Screenshot from 2020-08-12 13-58-32](https://user-images.githubusercontent.com/33818414/89976659-0089ce80-dca4-11ea-9ebb-395ca90e8c03.png)



### Show data page

![Screenshot from 2020-08-12 13-59-45](https://user-images.githubusercontent.com/33818414/89976729-30d16d00-dca4-11ea-89a0-fed68f169ba4.png)

- This is the screen after reading database.




### Normal Graph 


![Screenshot from 2020-08-12 14-01-07](https://user-images.githubusercontent.com/33818414/89976760-4b0b4b00-dca4-11ea-9a98-210411a0e88c.png)





### Zoom In/Out Graph 


![Screenshot from 2020-08-12 14-00-02](https://user-images.githubusercontent.com/33818414/89976787-624a3880-dca4-11ea-89b7-c3236d92b075.png)




