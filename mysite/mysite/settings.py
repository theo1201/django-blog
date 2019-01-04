"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# ：设置及配置项目。包括初始化缺省设置

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8#x(%0x#a6fku$=-ckhsod^1e*t_(we72^rg66+$($noillwvz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# : DEBUG 模式或者运行测试下不使用该设置。一旦将网站迁移到生产环境并将 DEBUG 设置为 False ，则需要在该设置中添加域名/主机来使用 Django 网站。
ALLOWED_HOSTS = []


# Application definition
# 所有项目都需要编辑的设置，Django 从这个设置中读取处于激活状态的应用。默认情况下，Django 包含以下应用：
INSTALLED_APPS = [
    'django.contrib.admin', #网站
    'django.contrib.auth',#权限框架；
    'django.contrib.contenttypes',#内容框架；
    'django.contrib.sessions',#会话框架；
    'django.contrib.messages',# 消息框架；
    'django.contrib.staticfiles',# 静态文件管理框架；
    'blog',
]
# 需要执行的中间件元组。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ：定义项目应用的主 URL 模式的 Python 模块。
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# 设置项目使用的所有数据库的字典。必须设置一个 default 数据库。默认使用 SQLite3 数据库。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
#  定义 Django 网站默认使用的语言。
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 配置SMTP服务器
# 收发邮件
#  服务器主机。默认为 localhost
EMAIL_HOST = 'smtp.gmail.com'
# 服务器的用户名
EMAIL_HOST_USER = 'your_account@hotmail.com'
#  SMTP 服务器的密码
EMAIL_HOST_PASSWORD = 'your_password'
# 服务器端口。默认为 25
EMAIL_PORT = 587
# EMAIL_USE_TLS: 是否使用 TLS 安全连接；
# EMAIL_USE_SSL: 是否使用隐式 SSL 安全连接。
# EMAIL_USE_TLS 和 EMAIL_USE_SSL 的默认设置都为False
# 需要配置其中一个为 True ，但是不能两个都设置为True。一般端口 587 对应 TLS ，端口 465 对应 SSL（加强 TSL ）。
EMAIL_USE_TLS = True


# 163邮箱
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'your_account@163.com'
EMAIL_HOST_PASSWORD = 'your_auth_code'  #邮箱的授权码而非密码
EMAIL_PORT = 465
EMAIL_USE_SSL = True
