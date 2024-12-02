
#!/bin/bash


export AWS_REGION=us-east-1
export AWS_ACCOUNT=986635652628

aws sqs purge-queue --queue-url https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_A_CANADA
aws sqs purge-queue --queue-url https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_B_CANADA
aws sqs purge-queue --queue-url https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_C_CANADA
aws sqs purge-queue --queue-url https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_D_CANADA
aws sqs purge-queue --queue-url https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_E_CANADA

for n in {1..120} 
do
    a=`aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url "https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_A_CANADA" --query 'Attributes.ApproximateNumberOfMessages' | tr -d '"'`
    b=`aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url "https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_B_CANADA" --query 'Attributes.ApproximateNumberOfMessages' | tr -d '"'`
    c=`aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url "https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_C_CANADA" --query 'Attributes.ApproximateNumberOfMessages' | tr -d '"'`
    d=`aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url "https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_D_CANADA" --query 'Attributes.ApproximateNumberOfMessages' | tr -d '"'`
    e=`aws sqs get-queue-attributes --attribute-names ApproximateNumberOfMessages --queue-url "https://sqs.${AWS_REGION}.amazonaws.com/${AWS_ACCOUNT}/NEW_APPLICATION_E_CANADA" --query 'Attributes.ApproximateNumberOfMessages' | tr -d '"'`
    echo $(date) + " " + $(($a+$b+$c+$d+$e))
    sleep 0.01
done


