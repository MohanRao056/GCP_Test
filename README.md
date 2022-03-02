# GCP_Test

#Initial Setup

 1. Install BQ client library
	pip install --upgrade google-cloud-bigquery
	
 2. Create service account and update the loaction of the service account in GCP_test_config.py file
	service_account="mohan-test-236502-1462334d1843.json"
	I have placed it in home dir

---------------------------------------------	

#Files In Ziped folder/home folder

 1. GCP_test.py -- Data pipeline code which can be configured to run in sequential/parallel mode by doing config change in the GCP_test_config.py file
 
 2. GCP_test_config.py -- Configuration file , Change config "tmp_sql" to run the code in parallel
 
 3. main.py -- Flask app
 
 
NOTE: Parallelism is implemented only for sql script present in tmp folder

---------------------------------------------
 
#Triggering Script

 1. To run pipeline in sequence
 
	python3 GCP_test.py
	
 2. To run pipeline in parallel
 
	Update the "tmp_sql" variable as shown below in GCP_test_config.py tmp_sql=['inventory_items.sql',['item_purchase_prices.sql','product_categories.sql'],'product_images.sql','variant_images.sql','products.sql','variants.sql']
	
	This setting will execute "item_purchase_prices.sql" and "product_categories.sql" in parallel
 
	python3 GCP_test.py
	
-----------------------------------------------

I have some credit card issue because of which I was not able enable the $300 credit from GCP. So I was not able to deploy the API on app engine/Cloud function. But I have tested the code in my local

#To run the FLASK code in locall, Follow the below steps

 1.  python3 main.py
 
 Endpoints
 
 ##Welcome Page
 http://127.0.0.1:8080/
 
 
 ##To run the pipeline to populate tmp and final dataset
 http://127.0.0.1:8080/POST/run
 
 
 ##To append the data to a table
 http://127.0.0.1:8080/POST/categories?id=100&category_name=test
 

 ##This will give error message saying id1 column not present
 http://127.0.0.1:8080/POST/categories?id1=100&category_name=test
 
 
--------------------------------
Provided BQ data viewer permission to data@luxola.com user