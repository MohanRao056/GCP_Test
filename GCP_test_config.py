service_account="mohan-test-236502-1462334d1843.json"
project_id='mohan-test-236502'
tmp_dataset='tmp'
final_dataset='final'
raw_dataset='raw'
tmp_folder="data-test-sde/res/tmp"
final_folder="data-test-sde/res/final"
#This setting will execute the script in sequential way
tmp_sql=['inventory_items.sql','item_purchase_prices.sql','product_categories.sql','product_images.sql','variant_images.sql','products.sql','variants.sql']
#This setting will execute item_purchase_prices.sql and product_categories.sql in parallel
#tmp_sql=['inventory_items.sql',['item_purchase_prices.sql','product_categories.sql'],'product_images.sql','variant_images.sql','products.sql','variants.sql']
final_sql=['products.sql']
write_disposition="WRITE_TRUNCATE"
log_filename='GCP_test.log'