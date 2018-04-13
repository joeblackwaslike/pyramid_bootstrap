# pyramid_bootstrap
[![Build Status](https://travis-ci.org/joeblackwaslike/pyramid_bootstrap.svg?branch=master)](https://travis-ci.org/joeblackwaslike/pyramid_bootstrap) [![Github Repo](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/joeblackwaslike/pyramid_bootstrap) [![Pypi Version](https://img.shields.io/pypi/v/pyramid_bootstrap.svg)](https://pypi.python.org/pypi/pyramid_bootstrap) [![Pypi License](https://img.shields.io/pypi/l/pyramid_bootstrap.svg)](https://pypi.python.org/pypi/pyramid_bootstrap) [![Pypi Wheel](https://img.shields.io/pypi/wheel/pyramid_bootstrap.svg)](https://pypi.python.org/pypi/pyramid_bootstrap) [![Pypi Versions](https://img.shields.io/pypi/pyversions/pyramid_bootstrap.svg)](https://pypi.python.org/pypi/pyramid_bootstrap)


## Maintainer
Joe Black | <me@joeblack.nyc> | [github](https://github.com/joeblackwaslike)


## Introduction
Pyramid extension that bundles all bootstrap 4 resources, including
font-awesome.  Allows for locally hosted development and CDN hosted production.


Also includes master layout template for jinja2 and chameleon template languages.


## Installation
```shell
pip3 install pyramid_bootstrap
```


## Usage

### App Factory Config
Include in your pyramid config either through .ini file, ZCML, or in python, ex:
```python
config.include('pyramid_bootstrap')
```

### Example templates
`home.jinja2`
```jinja2
{% extends "pyramid_bootstrap:/templates/bs4/layout.jinja2" %}

{% block title %}Quick Tutorial: {{ name }}{% endblock title %}

{% block content %}
<h1>Hi {{ name }}</h1>
{% endblock content %}
```

`home.pt`
```chameleon
<metal:macro use-macro="master">
  <metal:slot fill-slot="title">
    <title>Quick Tutorial: ${name}</title>
  </metal:slot>

  <metal:slot fill-slot="content">
    <h1>Hi ${name}</h1>
    <p>Chameleon is an XML-based templating language</p>
  </metal:slot>
</metal:macro>
```


## Changes
* [CHANGELOG](CHANGELOG.md)
