#! /bin/bash

set -eo pipefail

FILENAME="$(date +'%Y-%m-%d').gz"

if [ "$1" = 'mysql' ]; then
      echo "1"
      mysqldump -u $MYSQL_ROOT_USERNAME -h $MYSQL_HOST -P $MYSQL_PORT --password=$MYSQL_ROOT_PASSWORD \
            --all-databases --single-transaction --flush-logs | gzip > $FILENAME
elif [ "$1" = 'mongo' ]; then
      if [[ -z "${MONGODB_USERNAME}" ]]; then
            mongodump \
            --host $MONGODB_HOST:$MONGODB_PORT \
            -d $MONGODB_DATABASES --gzip \
            --archive=$FILENAME
      else
            mongodump --username $MONGODB_USERNAME --password $MONGODB_PASSWORD --authenticationDatabase=admin \
            --host $MONGODB_HOST:$MONGODB_PORT \
            -d $MONGODB_DATABASES --gzip \
            --archive=$FILENAME
      fi
else
    echo "Unknown database type"
    exit 1
fi

if [[ -z "${BACKUP_CUSTOM_STORAGE_ENDPOINT}" ]]; then
      aws s3 mv $FILENAME s3://$S3_BUCKET_NAME/$BUCKET_PATH/$1/
else
      aws -endpoint-url $BACKUP_CUSTOM_STORAGE_ENDPOINT s3 mv $FILENAME s3://$S3_BUCKET_NAME/$BUCKET_PATH/$1/
fi
