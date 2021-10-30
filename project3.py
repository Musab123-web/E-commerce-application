{% load static %}
{% block title %}
Your Shopping Cart
{% endblock %}
 
 
{% block content %}
&lt;div class="container"&gt;
&lt;div class="row" style="margin-top: 6%"&gt;
&lt;h2&gt;Your Shopping Cart
&lt;span class="badge pull-right"&gt;
{% with totail_items=cart|length %}
{% if cart|length &gt; 0 %}
My Shopping Order:
&lt;a href="{% url "cart:cart_detail" %}" style="color: green"&gt;
{{ totail_items }} item {{ totail_items|pluralize }}, P{{ cart.get_total_price }}
&lt;/a&gt;
{% else %}
Your cart is empty.
{% endif %}
{% endwith %}
&lt;/span&gt;
&lt;/h2&gt;
&lt;table class="table table-striped table-hover"&gt;
&lt;thead style="background-color: navajowhite"&gt;
&lt;tr&gt;
&lt;th&gt;Image&lt;/th&gt;
&lt;th&gt;Product&lt;/th&gt;
&lt;th&gt;Quantity&lt;/th&gt;
&lt;th&gt;Remove&lt;/th&gt;
&lt;th&gt;Unit Price&lt;/th&gt;
&lt;th&gt;Price&lt;/th&gt;
&lt;/tr&gt;
&lt;/thead&gt;
&lt;tbody&gt;
{% for item in cart %}
{% with product=item.product %}
&lt;tr&gt;
&lt;td&gt;
&lt;a href="{{ product.get__absolute_url }}"&gt;
&lt;img src="{% if product.image %} {{ product.image.url }} {% else %} {% static 'img/default.jpg' %} {% endif %}" alt="..." style="height: 130px; width: auto"&gt;
&lt;/a&gt;
&lt;/td&gt;
&lt;td&gt;{{ product.name }}&lt;/td&gt;
&lt;td&gt;
&lt;form action="{% url "cart:cart_add" product.id %}" method="post"&gt;
{% csrf_token %}
{{ item.update_quantity_form.quantity }}
{{ item.update_quantity_form.update }}
&lt;input type="submit" value="Update" class="btn btn-warning" &gt;
&lt;/form&gt;
&lt;/td&gt;
&lt;td&gt;
&lt;a style="color: red" href="{% url "cart:cart_remove" product.id %}"&gt;Remove&lt;/a&gt;
&lt;/td&gt;
&lt;td&gt;P{{ item.price }}&lt;/td&gt;
&lt;td&gt;P{{ item.total_price }}&lt;/td&gt;
&lt;/tr&gt;
{% endwith %}
{% endfor %}
&lt;tr style="background-color: navajowhite"&gt;
&lt;td&gt;&lt;b&gt;Total&lt;/b&gt;&lt;/td&gt;
&lt;td colspan="4"&gt;&lt;/td&gt;
&lt;td colspan="num"&gt;&lt;b&gt;P{{ cart.get_total_price }}&lt;/b&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/tbody&gt;
&lt;/table&gt;
&lt;p class="text-right"&gt;
&lt;a href="{% url "shop:product_list" %}" class="btn btn-default"&gt;Continue Shopping&lt;/a&gt;
&lt;a href="{% url "orders:order_create" %}" class="btn btn-warning"&gt;Checkout&lt;/a&gt;
&lt;/p&gt;
&lt;/div&gt;
&lt;/div&gt;
{% endblock %}

{% extends 'shop/base.html' %}
{% load static %}
{% block title %}
Your Shopping Cart| Checkout
{% endblock %}

{% block content %}
&lt;div class="container"&gt;
&lt;div class="row" style="margin-top: 6%"&gt;
&lt;div class="col-md-8"&gt;
&lt;h4 class="page-header"&gt;Checkout&lt;/h4&gt;
&lt;form action="." method="post"&gt;
{% csrf_token %}
{{ form.as_p }}&lt;br&gt;
&lt;input type="submit" class="btn btn-primary" value="Submit order"&gt;
&lt;/form&gt;
&lt;/div&gt;
&lt;div class="col-md-4"&gt;
&lt;div class="page-header"&gt;
Your Order
&lt;/div&gt;
&lt;ul class="list-group"&gt;
{% for item in cart %}
&lt;li class="list-group-item"&gt;
{{ item.quantity }}x {{ item.product.name }}
&lt;span&gt; P{{ item.total_price }}&lt;/span&gt;
&lt;/li&gt;
{% endfor %}

&lt;li class="list-group-item active"&gt;Total Cost: P{{ cart.get_total_price }}&lt;/li&gt;
&lt;/ul&gt;

&lt;/div&gt;
&lt;/div&gt;
&lt;/div&gt;
{% endblock %}

{% load static %}
&lt;nav class="navbar navbar-default navbar-fixed-top" role="navigation" style="margin-bottom: 0px; background-color: darkblue;"&gt;
&lt;!-- Brand and toggle get grouped for better mobile display --&gt;
&lt;div class="container-fluid"&gt;
&lt;div class="navbar-header"&gt;

&lt;a class="navbar-brand" href="{% url 'shop:product_list' %}" style="color: whitesmoke"&gt;EVANZ WEBSITE BUSINESS&lt;/a&gt;
&lt;/div&gt;

&lt;!-- Collect the nav links, forms, and other content for toggling --&gt;
&lt;div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"&gt;

&lt;ul class="nav navbar-nav navbar-right"&gt;
&lt;li class="dropdown"&gt;
{% if request.user.is_authenticated %}
&lt;a href="#" class="dropdown-toggle" data-toggle="dropdown" style="color: #ffffff"&gt;{{ request.user.username }}&lt;b class="caret"&gt;&lt;/b&gt;&lt;/a&gt;

{% endif %}
&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;&lt;!-- /.navbar-collapse --&gt;
&lt;/div&gt;
&lt;/nav&gt;

&lt;!DOCTYPE html&gt;
{% load static %}
&lt;html lang="en"&gt;
&lt;head&gt;
&lt;meta charset="UTF-8"&gt;
&lt;title&gt;{% block title %}On-line Shop{% endblock %}&lt;/title&gt;
&lt;link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"&gt;
 
&lt;/head&gt;
&lt;body style="background-color: navajowhite"&gt;
{% include 'shop/navbar.html' %}
 
&lt;div class="container"&gt;
&lt;div class="row" style="margin-top: 6%"&gt;
&lt;button class="btn btn-danger pull-right"&gt;
{% with totail_items=cart|length %}
{% if cart|length &gt; 0 %}
My Shopping Order:
&lt;a href="{% url "cart:cart_detail" %}" style="color: white"&gt;
{{ totail_items }} item {{ totail_items|pluralize }}, P{{ cart.get_total_price }}
&lt;/a&gt;
{% else %}
Your cart is empty.
{% endif %}
{% endwith %}
&lt;/button&gt;
&lt;/div&gt;
&lt;/div&gt;
{% block content %}
 
 
{% endblock %}
 
&lt;script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
