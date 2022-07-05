phase-1
1. add 'rest_framework' to setting.py in INSTALLED_APPS
2. create api folder, inside it create urls.py and views.py
3. connect authproject urls.py with api/urls.y
4. create views to get hardcoded person data
5. run server using cmd 'python manage.py runserver' then you can get the the person data 

phase-2
1. create app using cmd 'python manage.py startapp base' 
2. add 'base' to setting.py in INSTALLED_APPS
3. create Person model to base/models.py
4. create serializers.py to api folder then create PersonSerializer to api/serializers.py
5. update views to fetch data from Person model using serializers
6. add your model to base/admin.py to see in admin dash board



![Screenshot 2022-07-05 at 10.30.52 AM](/Users/laxmikumaryadav/Desktop/Screenshot 2022-07-05 at 10.30.52 AM.png)

![Screenshot 2022-07-05 at 10.26.42 AM](/Users/laxmikumaryadav/Desktop/Screenshot 2022-07-05 at 10.26.42 AM.png)

![Screenshot 2022-07-05 at 10.26.57 AM](/Users/laxmikumaryadav/Desktop/Screenshot 2022-07-05 at 10.26.57 AM.png)

followed this youtube chanel
https://www.youtube.com/watch?v=cJveiktaOSQ&ab_channel=DennisIvy