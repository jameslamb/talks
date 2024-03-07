# setup

To support this talk, I tried to replicate this situation with a little Redshift in my personal account.

* nodes: 1
* instance type: `dc2.large`
* region: `us-east-1`

Created an IAM role per https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-iam-policies.html and attached it to the cluster.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListMultipartUploadParts",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": [
                "arn:aws:s3:::anaconda-package-data",
                "arn:aws:s3:::anaconda-package-data/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:CreateDatabase",
                "glue:DeleteDatabase",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:UpdateDatabase",
                "glue:CreateTable",
                "glue:DeleteTable",
                "glue:BatchDeleteTable",
                "glue:UpdateTable",
                "glue:GetTable",
                "glue:GetTables",
                "glue:BatchCreatePartition",
                "glue:CreatePartition",
                "glue:DeletePartition",
                "glue:BatchDeletePartition",
                "glue:UpdatePartition",
                "glue:GetPartition",
                "glue:GetPartitions",
                "glue:BatchGetPartition"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

I went into the Redshift query editor in the AWS console to run SQL.

Created a database (https://docs.aws.amazon.com/redshift/latest/gsg/t_creating_database.html):

```sql
CREATE DATABASE prod;
```

Then ran this to create both a Redshift schema and a database in Glue data catalog

```sql
CREATE EXTERNAL SCHEMA
    search_tracking
FROM DATA CATALOG
DATABASE
    'search_tracking'
IAM_ROLE
    'arn:aws:iam::${ACCOUNT}:role/redshift-glue-access'
CREATE EXTERNAL DATABASE IF NOT EXISTS;
```

Then created a table for the `conda` download stats.

```sql
CREATE EXTERNAL TABLE
    search_tracking.download_stats
(data_source VARCHAR, time TIMESTAMP, pkg_name VARCHAR,
 pkg_version VARCHAR, pkg_platform VARCHAR, pkg_python VARCHAR,
 counts BIGINT)
PARTITIONED BY (
    date_year int,
    date_month int,
    date_day TIMESTAMP
)
STORED AS PARQUET
LOCATION 's3://anaconda-package-data/conda/hourly/'
```

Then rregistered a partition

```shell
aws --region us-west-2 \
    glue create-partition \
        --database-name 'search_tracking' \
        --table-name 'download_stats' \
        --partition-input '
            {
                "Values": ["2017", "01", "2017-01-01"],
                "StorageDescriptor": {
                    "Location": "s3://anaconda-package-data/conda/hourly/2017/01/2017-01-01",
                    "InputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
                    "SerdeInfo": {
                        "SerializationLibrary": "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
                    }
                }
            }'
```

References:

* https://www.anaconda.com/blog/announcing-public-anaconda-package-download-data
* https://anaconda-package-data.s3.amazonaws.com/
* https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-schemas.html
* https://github.com/ContinuumIO/anaconda-package-data
* https://docs.aws.amazon.com/cli/latest/reference/glue/create-partition.html
