# Volunter-Network_Platform
### Descripion: 
Designed and built a scalable ETL pipeline using AWS Glue and Redshift for centralizing volunteer-related data from multiple sources. Leveraged AWS Lambda for real-time synchronization and deployed event-driven architectures to ensure data consistency across the platform.

### Note of Confidentiality
This project was part of a research initiative at Northeastern University centered on developing a scalable ETL pipeline and database infrastructure for volunteer data management. Due to the sensitive nature of the project, not all code and data can be shared publicly. The files included in this repository showcase selected components of our work, illustrating the methodologies and technologies utilized throughout the project. Thank you for your understanding.

---

### 1. **etl_pipeline.py**
This script orchestrates the ETL (Extract, Transform, Load) process for volunteer data. It extracts data from multiple sources, including CSV and JSON files, performs necessary transformations such as data cleaning and normalization, and loads the processed data into AWS S3 for centralized storage. The implementation includes robust logging and error handling to ensure data integrity and smooth operation.

### 2. **redshift_setup.py**
This script sets up the database schema on AWS Redshift for managing volunteer profiles and activities. It creates necessary tables with optimized schemas and implements indexing strategies to enhance query performance. The script also includes logging to provide feedback on the table creation process and to help track any errors that may occur.

### 3. **data_sync_lambda.py**
This AWS Lambda function triggers real-time synchronization of volunteer data from AWS S3 into AWS Redshift upon new data uploads. It executes a SQL COPY command to load the data and incorporates comprehensive logging and error handling to ensure data consistency and provide visibility into the synchronization process.

### 4. **data_visualization.py**
This script retrieves volunteer data from AWS Redshift and visualizes it using Matplotlib and Seaborn. It generates insightful visualizations, such as bar plots of volunteer activities, helping stakeholders analyze engagement levels effectively. The script demonstrates the integration of data fetching, processing, and visualization in a seamless workflow.
