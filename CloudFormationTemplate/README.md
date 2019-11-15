## :warning: If you are a maintainer of this github repo, when you update the CloudFormation template and want to make changes to EventEngine, please make sure the OwnerArn of the Cloud9 is updated to the following. Remember that this change is only made to the Event Engine template. 

### See below for OwnerArn for Cloud9 instance in current template
```
OwnerArn: !Ref "AWS::NoValue"
```

### Change the above to the following
```
OwnerArn: !Sub "arn:aws:sts::${AWS::AccountId}:assumed-role/TeamRole/MasterKey"
```

