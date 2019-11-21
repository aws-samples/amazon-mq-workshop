**If you are not an official maintainer or a committer for this Github repo, please ignore this README and move on...**

** :warning: This applies to official maintainer or committer only **

When you update the CloudFormation template and want to make changes to EventEngine, please make sure the OwnerArn of the Cloud9 is updated to the following. Remember that this change is only made to the EventEngine template. 

** See below for OwnerArn for Cloud9 instance in current template **
```
OwnerArn: !Ref "AWS::NoValue"
```

** Change the above to the following **
```
OwnerArn: !Sub "arn:aws:sts::${AWS::AccountId}:assumed-role/TeamRole/MasterKey"
```

