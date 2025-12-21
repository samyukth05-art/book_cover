# Ex.05 Book Front Cover Page Design
# Date:05.12.25
# AIM:
To design a book front cover page using HTML and CSS.

# DESIGN STEPS:
## Step 1:
Create a Django Admin project.

## Step 2:
Create an app in the Django interface.

## Step 3:
Create a folder named 'static' in the app folder.

## Step 4:
Create a new HTML file in the static folder.

## Step 5:
Write the HTML code with relevant CSS properties.

## Step 6:
Choose the appropriate style and color scheme.

## Step 7:
Insert the images in their appropriate places.

## Step 8:
Publish the website in the LocalHost.

# PROGRAM:
views.py
```
from django.shortcuts import render

def book_func(request):
    return render(request, 'bookcover.html')

```
urls.py
```
from django.contrib import admin
from django.urls import path
from bookapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_func),
]
```
bookcover.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Cover</title>
<style>
    #cover{
    background-image:url("{% static 'bookcover.jpg' %}") ;
    height: 700px;
    width:450px;
    position: relative;
    margin:50px auto;
    }
    #border{
    top:20px;
    bottom: 20px;
    left:20px;
    right:20px;
    border:4px solid black;
    position:absolute;
    }
    #cover h1{
        text-align: center;
        font-style: oblique;
        color: white;
    }
    #cover img{
        position:absolute;
        bottom:50px;
        right:20px;
        height: 150px;
        width: 150px;
        border-radius: 20px;
    }
    #cover h4{
        position:absolute;
        right:50px;
        bottom: 0px;
        color: aliceblue;

    }
    #cover h3{
        text-align: center;
        font-style: oblique;
    }
    
</style>
</head>
<body>
    <div id="cover">
        <div id="border">
            <h1>THE GUIDE</h1>
            <h3 color="white">"Nothing in this world can be hidden"</h3>
            <hr color="black" width="100%" size="4">
            <img src="{% static 'author.jpg' %}">
            <h4>R.K.Narayan</h4>
        </div>
    </div>
</body>
```

# OUTPUT:
![alt text](<Screenshot 2025-12-15 135607.png>)

# RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
