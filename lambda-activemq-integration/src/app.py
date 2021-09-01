import json
import base64

def lambda_handler(event, context):
    
    #print(event)
    #print(context.aws_request_id)
    for message in event["messages"]:
        queueName = message["destination"]["physicalName"]
        base64messageBody = message["data"]
        plainMessageBody = base64.b64decode(base64messageBody).decode("utf-8")
        #print(plainMessageBody)
        print("Lambda ", context.function_name, " Receiver: received ", plainMessageBody)

    return {
        'statusCode': 200,
        'body': json.dumps('Recieved messages from ActiveMQ broker')
    }
