#! /bin/bash

set -eo pipefail

FILENAME="$(date +'%Y-%m-%d').gz"

MONGODB_URI="mongodb://"
MONGODB_PORT=${MONGODB_PORT:-27017}
MONGODB_HOST=${MONGODB_HOST:-mongodb}
MONGODB_AUTHDB=${MONGODB_AUTHDB:-admin}

if [ -n "${MONGODB_USERNAME}" ] && [ -n "${MONGODB_PASSWORD}" ]; then
    MONGODB_URI+="${MONGODB_USERNAME}:${MONGODB_PASSWORD}@"
fi

MONGODB_URI+="${MONGODB_HOST}:${MONGODB_PORT}/${MONGODB_DATABASES}?authSource=${MONGODB_AUTHDB}"

if [ "$1" = 'mysql' ]; then
      mysqldump -u $MYSQL_ROOT_USERNAME -h $MYSQL_HOST -P $MYSQL_PORT --password=$MYSQL_ROOT_PASSWORD \
            --all-databases --single-transaction --flush-logs | gzip > $FILENAME
elif [ "$1" = 'mongo' ]; then
      mongodump --uri="${MONGODB_URI}" --gzip --archive=$FILENAME
else
    echo "Unknown database type"
    exit 1
fi

if [ "$BACKUP_STORAGE_SERVICE" = 'aws-s3' ]; then
      if [[ -z "${BACKUP_CUSTOM_STORAGE_ENDPOINT}" ]]; then
            aws s3 mv $FILENAME s3://$S3_BUCKET_NAME/$BUCKET_PATH/$1/
      else
            aws --endpoint-url $BACKUP_CUSTOM_STORAGE_ENDPOINT s3 mv $FILENAME s3://$S3_BUCKET_NAME/$BUCKET_PATH/$1/
      fi
elif [ "$BACKUP_STORAGE_SERVICE" = 'azure-blob' ]; then
      azcopy cp $FILENAME "https://${AZURE_STORAGE_ACCOUNT}.blob.core.windows.net/${AZURE_STORAGE_CONTAINER_NAME}/$BUCKET_PATH/${1}/$FILENAME?${AZURE_STORAGE_SAS_TOKEN}"
else
    echo "Unknown storage service"
    exit 1
fi
