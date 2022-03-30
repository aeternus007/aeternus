from django.shortcuts import render, HttpResponse

def home(response):
  return(HttpResponse("<h1>This works!!</h1>"))
  