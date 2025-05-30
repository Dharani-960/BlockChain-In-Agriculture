from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Login.html', views.Login, name="Login"), 
	       path('Register.html', views.Register, name="Register"),
	       path('RegisterAction', views.RegisterAction, name="RegisterAction"),
	       path('UserLogin', views.UserLogin, name="UserLogin"),
	       path('UploadCrop.html', views.UploadCrop, name="UploadCrop"),
	       path('UploadCropAction', views.UploadCropAction, name="UploadCropAction"),
	       path('FertilizerInfo.html', views.FertilizerInfo, name="FertilizerInfo"),
	       path('ViewOrdersForFarmer.html', views.ViewOrdersForFarmer, name="ViewOrdersForFarmer"),
	       path('BrowseProducts.html', views.BrowseProducts, name="BrowseProducts"),
	       path('SearchProductAction', views.SearchProductAction, name="SearchProductAction"),
	       path('PurchaseProducts.html', views.PurchaseProducts, name="PurchaseProducts"),
	       path('MillerSearchProductAction', views.MillerSearchProductAction, name="MillerSearchProductAction"),
	       path('SaleToConsumer.html', views.SaleToConsumer, name="SaleToConsumer"),
	       path('ConsumerSaleAction', views.ConsumerSaleAction, name="ConsumerSaleAction"),
	       path('BookOrder', views.BookOrder, name="BookOrder"),
	       path('MillerBookOrder', views.MillerBookOrder, name="MillerBookOrder"),
]