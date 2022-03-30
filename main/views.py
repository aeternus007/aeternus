from django.shortcuts import render, HttpResponse

def index(response):
  return(HttpResponse("<h1>This works!!</h1>"))
  