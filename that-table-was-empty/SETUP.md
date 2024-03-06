# setup

To support this talk, I tried to replicate this situation with a little Redshift in my personal account.

* nodes: 1
* instance type: `dc2.large`
* 

Created a database (https://docs.aws.amazon.com/redshift/latest/gsg/t_creating_database.html):

```sql
CREATE DATABASE prod;
```

* created a role per https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-iam-policies.html

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

Then ran this to create both a Redshift schema and a database in Glue data catalog

```sql
CREATE EXTERNAL SCHEMA
    conda
FROM DATA CATALOG
DATABASE
    'conda' 
IAM_ROLE
    'arn:aws:iam::${ACCOUNT}:role/redshift-glue-access'
CREATE EXTERNAL DATABASE IF NOT EXISTS;
```

Then created a table for the `conda` download stats.

```sql
CREATE EXTERNAL TABLE
    conda.download_stats
(data_source VARCHAR, time TIMESTAMP, pkg_name VARCHAR, pkg_version VARCHAR, pkg_platform VARCHAR, pkg_python VARCHAR, counts BIGINT)
PARTITIONED BY (
    date_year 
)
STORED AS PARQUET
LOCATION { 's3://anaconda-package-data/conda/hourly/' }
```

data_source: anaconda for Anaconda distribution, conda-forge for the conda-forge channel on Anaconda.org, and bioconda for the bioconda channel on Anaconda.org.
time: UTC time, binned by hour
pkg_name: Package name (Ex: pandas)
pkg_version: Package version (Ex: 0.23.0)
pkg_platform: One of linux-32, linux-64, osx-64, win-32, win-64, linux-armv7, linux-ppcle64, linux-aarch64, or noarch
pkg_python: Python version required by the package, if any (Ex: 3.7)
counts: Number of downloads for this combination of attributs

Registered this data in Glue:

* https://www.anaconda.com/blog/announcing-public-anaconda-package-download-data
* https://anaconda-package-data.s3.amazonaws.com/
* https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-external-schemas.html
* https://github.com/ContinuumIO/anaconda-package-data
