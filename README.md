# This is A Python-based ETL (Extract, Transform, Load) pipeline for processing CSV data and loading it into a MySQL database with configurable transformations.

## Installation
Install the reuired dependencies:
```bash
pip install -r requirement.txt
```
## Configuration
create a `config.yaml` file
```yaml
database:
  host: localhost
  user: your_username
  password: your_password
  name: your_database

paths:
  input_csv: ETLpipeline/data
  google_application_cred: "your google .json credentials file"

google_cloud:
  bucket_name: your_bucket
  blob_name: your_blob_name
  ```
## Run the ETL pipeline
```python
python main.py
```  