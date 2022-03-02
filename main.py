from flask import Flask, request
from google.cloud import bigquery
import GCP_test
from GCP_test_config import *

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome Page!'

@app.route('/POST/run')
def run_pipeline():
    try:
        GCP_test.run_pipeline()
        return "Data pipeline success!!"
    except Exception as e:
        return "Data Pipeline Failed!!"
    
@app.route('/POST/<table_name>')
def append_data(table_name):
    data=request.args
    table_id=f"{project_id}.{raw_dataset}.{table_name}"
    try:
        client = bigquery.Client.from_service_account_json(service_account)
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"
        )
        job = client.load_table_from_json([data],table_id,job_config=job_config)
        job.result()
        return f"Data appended succssfully to table {table_id}"
    except Exception as e:
        return f"Failed to append data to table {table_id} ==> {e}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
