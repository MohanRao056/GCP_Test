from google.cloud import bigquery
from multiprocessing import Process
import os
import logging
from GCP_test_config import *

#log settings
logging.basicConfig(filename=log_filename, filemode='a', format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s", level=logging.INFO)


#loading data to BQ
def bq_load_data(table_id,query,write_disposition):
    try:
        client = bigquery.Client.from_service_account_json(service_account)
        job_config = bigquery.QueryJobConfig(
            allow_large_results=True, 
            destination=table_id, 
            use_legacy_sql=False,
            write_disposition=write_disposition
        )
        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        logging.info(f"Query results loaded to the table {table_id}")
        logging.info(f"parent process: {os.getppid()}")
        logging.info(f"process id: {os.getpid()}")
    except Exception as e:
        raise Exception(f"Failed to load the data to BQ table ==> {e}")

def run_pipeline():
    try:
        #This will execute the sql script in sequential or parallel mode depending on the configuration of tmp_sql in GCP_test_config.py
        for sql_file in tmp_sql:
            if type(sql_file) is list:
                process_list=[]
                for sql in sql_file:
                    with open(f"{tmp_folder}/{sql}") as f:
                        query=f.read()
                        table_name=sql.split('.')[0]
                        table_id=f"{project_id}.{tmp_dataset}.{table_name}"
                        p = Process(target=bq_load_data, args=(table_id,query,write_disposition))
                        p.start()
                        process_list.append(p)
                for p in process_list:
                    p.join()   
            else:
                with open(f"{tmp_folder}/{sql_file}") as f:
                    query=f.read()
                    table_name=sql_file.split('.')[0]
                    table_id=f"{project_id}.{tmp_dataset}.{table_name}"
                    bq_load_data(table_id,query,write_disposition)

        #Loading the final Product table
        for sql_file in final_sql:
            with open(f"{final_folder}/{sql_file}") as f:
                query=f.read()
                table_name=sql_file.split('.')[0]
                table_id=f"{project_id}.{final_dataset}.{table_name}"
                bq_load_data(table_id,query,write_disposition)
            
        logging.info("Data pipeline success!!")
        logging.info("***********************")
    except Exception as e:
        logging.error("Data Pipeline Failed!!")
        logging.error(str(e))
        logging.info("***********************")
        raise Exception(f"Data Pipeline Failed!! ==> {e}")

if __name__ == "__main__":
    run_pipeline()