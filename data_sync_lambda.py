import json
import boto3

# Initialize Boto3 client
redshift = boto3.client('redshift-data')

# Redshift connection parameters
CLUSTER_ID = 'your-cluster-id'
DATABASE = 'volunteer_db'
DB_USER = 'your_username'

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # SQL to load data into Redshift
    copy_sql = f'''
    COPY volunteer_profiles
    FROM 's3://{bucket}/{key}'
    IAM_ROLE 'your-iam-role-arn'
    CSV
    IGNOREHEADER 1;
    '''
    
    # Execute the SQL command to load data into Redshift
    response = redshift.execute_statement(
        ClusterIdentifier=CLUSTER_ID,
        Database=DATABASE,
        DbUser=DB_USER,
        Sql=copy_sql
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data synchronized successfully!')
    }
