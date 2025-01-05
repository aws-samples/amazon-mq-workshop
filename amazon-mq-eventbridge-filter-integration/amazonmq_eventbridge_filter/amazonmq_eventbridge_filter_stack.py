import os
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_amazonmq as amazonmq,
    aws_ec2 as ec2,
    aws_secretsmanager as sm,
    Fn as fn,
    aws_events as events,
    aws_pipes as pipes,
    aws_iam as iam,
    aws_events_targets as targets,
    aws_sqs as sqs,
)
from constructs import Construct


class AmazonmqEventbridgeFilterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC with subnets
        app_vpc = ec2.Vpc(
            self,
            "vpc",
            max_azs=1,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="private_subnet",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                ),
                ec2.SubnetConfiguration(
                    name="public_subnet", subnet_type=ec2.SubnetType.PUBLIC
                ),
            ],
        )


        # # Security group rules remain the same
        # mq_security_group.add_ingress_rule(
        #     ec2.Peer.any_ipv4(),
        #     ec2.Port.tcp(61617),
        #     "Allow OpenWire SSL"
        # )
        # mq_security_group.add_ingress_rule(
        #     ec2.Peer.any_ipv4(),
        #     ec2.Port.tcp(8162),
        #     "Allow Web Console"
        # )


        # MQ Security Group
        mq_security_group = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=app_vpc,
            description="Allow MQ Access",
            allow_all_outbound=True,
        )

        mq_security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_traffic())

        public_subnets = [
            public_subnet.node.default_child.attr_subnet_id
            for public_subnet in app_vpc.public_subnets
        ]

        security_group = [mq_security_group.node.default_child.attr_group_id]

        mq_secret = sm.Secret(
            self,
            "SecretAmazonMQ",
            description="This is the secret for my AmazonMQ instance",
            secret_name="AmazonMQSecret",
            generate_secret_string=sm.SecretStringGenerator(
                secret_string_template='{"username": "admin"}',
                generate_string_key="password",
                password_length=16,
                exclude_characters='"@/, :=',
            ),
        )

        amazonmqProducerBroker = amazonmq.CfnBroker(
            self,
            "ProducerAmazonMQBroker",
            auto_minor_version_upgrade=True,
            broker_name="ProducerBroker",
            deployment_mode="SINGLE_INSTANCE",
            engine_type="ActiveMQ",
            engine_version="5.17.6",
            host_instance_type="mq.t3.micro",
            publicly_accessible=True,
            storage_type="efs",
            authentication_strategy="simple",
            maintenance_window_start_time={
                "dayOfWeek": "FRIDAY",
                "timeOfDay": "17:00",
                "timeZone": "UTC",
            },
            logs={"audit": False, "general": True},
            security_groups=security_group,
            subnet_ids=public_subnets,
            users=[
                amazonmq.CfnBroker.UserProperty(
                    username="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:username}}",
                        ]
                    ),
                    password="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:password}}",
                        ]
                    ),
                    console_access=True,
                )
            ],
            encryption_options={"useAwsOwnedKey": True},
        )

        amazonmqConsumerBroker = amazonmq.CfnBroker(
            self,
            "ConsumerAmazonMQBroker",
            auto_minor_version_upgrade=True,
            broker_name="ConsumerBroker",
            deployment_mode="SINGLE_INSTANCE",
            engine_type="ActiveMQ",
            engine_version="5.17.6",
            host_instance_type="mq.t3.micro",
            publicly_accessible=True,
            storage_type="efs",
            authentication_strategy="simple",
            maintenance_window_start_time={
                "dayOfWeek": "FRIDAY",
                "timeOfDay": "17:00",
                "timeZone": "UTC",
            },
            logs={"audit": False, "general": True},
            security_groups=security_group,
            subnet_ids=public_subnets,
            users=[
                amazonmq.CfnBroker.UserProperty(
                    username="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:username}}",
                        ]
                    ),
                    password="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:password}}",
                        ]
                    ),
                    console_access=True,
                )
            ],
            encryption_options={"useAwsOwnedKey": True},
        )

        amazonmqFilterBroker = amazonmq.CfnBroker(
            self,
            "FilterAmazonMQBroker",
            auto_minor_version_upgrade=True,
            broker_name="FilterBroker",
            deployment_mode="SINGLE_INSTANCE",
            engine_type="ActiveMQ",
            engine_version="5.17.6",
            host_instance_type="mq.t3.micro",
            publicly_accessible=True,
            storage_type="efs",
            authentication_strategy="simple",
            maintenance_window_start_time={
                "dayOfWeek": "FRIDAY",
                "timeOfDay": "17:00",
                "timeZone": "UTC",
            },
            logs={"audit": False, "general": True},
            security_groups=security_group,
            subnet_ids=public_subnets,
            users=[
                amazonmq.CfnBroker.UserProperty(
                    username="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:username}}",
                        ]
                    ),
                    password="".join(
                        [
                            "{{resolve:secretsmanager:",
                            mq_secret.secret_full_arn,
                            ":SecretString:password}}",
                        ]
                    ),
                    console_access=True,
                )
            ],
            encryption_options={"useAwsOwnedKey": True},
        )

        filter_broker_configuration = amazonmq.CfnConfiguration(
            self,
            "FilterBrokerConfiguration",
            data=fn.base64(
                fn.join(
                    delimiter="",
                    list_of_values=[
                        """<?xml version="1.0" encoding="UTF-8" standalone="yes"?> <broker schedulePeriodForDestinationPurge="10000" xmlns="http://activemq.apache.org/schema/core"> <destinationInterceptors> <mirroredQueue copyMessage="true" postfix=".qmirror" prefix=""/> <virtualDestinationInterceptor> <virtualDestinations> <virtualTopic name="&gt;" prefix="VirtualTopicConsumers.*." selectorAware="false"/> <compositeQueue name="ALL_INBOUND"> <forwardTo> <filteredDestination queue="NEW_APPLICATION_A_CANADA" selector="message_type = 'new' AND description like '%APPLICATION_A' AND country = 'canada' "/> <filteredDestination queue="NEW_APPLICATION_A_US" selector="message_type = 'new' AND description like '%APPLICATION_A' AND country = 'US' "/> <filteredDestination queue="NEW_APPLICATION_A_UK" selector="message_type = 'new' AND description like '%APPLICATION_A' AND country = 'UK' "/> <filteredDestination queue="NEW_APPLICATION_B_CANADA" selector="message_type = 'new' AND description like '%APPLICATION_B' AND country = 'canada' "/> <filteredDestination queue="NEW_APPLICATION_B_US" selector="message_type = 'new' AND description like '%APPLICATION_B' AND country = 'US' "/> <filteredDestination queue="NEW_APPLICATION_B_UK" selector="message_type = 'new' AND description like '%APPLICATION_B' AND country = 'UK' "/> <filteredDestination queue="NEW_APPLICATION_C_CANADA" selector="message_type = 'new' AND description like '%APPLICATION_C' AND country = 'canada' "/> <filteredDestination queue="NEW_APPLICATION_C_US" selector="message_type = 'new' AND description like '%APPLICATION_C' AND country = 'US' "/> <filteredDestination queue="NEW_APPLICATION_C_UK" selector="message_type = 'new' AND description like '%APPLICATION_C' AND country = 'UK' "/> <filteredDestination queue="NEW_APPLICATION_D_CANADA" selector="message_type = 'new' AND description like '%APPLICATION_D' AND country = 'canada' "/> <filteredDestination queue="NEW_APPLICATION_D_US" selector="message_type = 'new' AND description like '%APPLICATION_D' AND country = 'US' "/> <filteredDestination queue="NEW_APPLICATION_D_UK" selector="message_type = 'new' AND description like '%APPLICATION_D' AND country = 'UK' "/> <filteredDestination queue="NEW_APPLICATION_E_CANADA" selector="message_type = 'new' AND description like '%APPLICATION_E' AND country = 'canada' "/> <filteredDestination queue="NEW_APPLICATION_E_US" selector="message_type = 'new' AND description like '%APPLICATION_E' AND country = 'US' "/> <filteredDestination queue="NEW_APPLICATION_E_UK" selector="message_type = 'new' AND description like '%APPLICATION_E' AND country = 'UK' "/> </forwardTo> </compositeQueue> </virtualDestinations> </virtualDestinationInterceptor> </destinationInterceptors> <destinationPolicy> <policyMap> <policyEntries> <policyEntry gcInactiveDestinations="true" inactiveTimoutBeforeGC="600000" topic="&gt;"> <pendingMessageLimitStrategy> <constantPendingMessageLimitStrategy limit="1000"/> </pendingMessageLimitStrategy> </policyEntry> <policyEntry gcInactiveDestinations="true" inactiveTimoutBeforeGC="600000" queue="&gt;"/> </policyEntries> </policyMap> </destinationPolicy> <plugins> </plugins> <networkConnectors> <networkConnector duplex="true" messageTTL="2" name="ConsumerBroker" networkTTL="2" uri="static:(""",
                        fn.select(0, amazonmqConsumerBroker.attr_open_wire_endpoints),
                        ')" userName="admin"/> </networkConnectors> </broker>',
                    ],
                )
            ),
            engine_type="ACTIVEMQ",
            engine_version="5.17.6",
            name="FilterBrokerConfiguration",
        )
        producer_broker_configuration = amazonmq.CfnConfiguration(
            self,
            "ProducerBrokerConfiguration",
            data=fn.base64(
                fn.join(
                    delimiter="",
                    list_of_values=[
                        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?> <broker schedulePeriodForDestinationPurge="10000" xmlns="http://activemq.apache.org/schema/core"> <destinationPolicy> <policyMap> <policyEntries> <policyEntry gcInactiveDestinations="true" inactiveTimoutBeforeGC="600000" topic="&gt;"> <pendingMessageLimitStrategy> <constantPendingMessageLimitStrategy limit="1000"/> </pendingMessageLimitStrategy> </policyEntry> <policyEntry gcInactiveDestinations="true" inactiveTimoutBeforeGC="600000" queue="&gt;"/> </policyEntries> </policyMap> </destinationPolicy> <plugins> </plugins> <networkConnectors> <networkConnector duplex="false" messageTTL="2" name="FilterBroker" networkTTL="2" staticBridge="true" uri="static:(',
                        fn.select(0, amazonmqFilterBroker.attr_open_wire_endpoints),
                        ')" userName="admin"> <staticallyIncludedDestinations> <queue physicalName="ALL_INBOUND"/> </staticallyIncludedDestinations> </networkConnector> </networkConnectors> </broker>',
                    ],
                )
            ),
            engine_type="ACTIVEMQ",
            engine_version="5.17.6",
            name="ProducerBrokerConfiguration",
        )

        filter_broker_configuration_association = amazonmq.CfnConfigurationAssociation(  # noqa: F841
            self,
            "filter_broker_configuration_association",
            broker=amazonmqFilterBroker.ref,
            configuration=amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty(
                id=filter_broker_configuration.ref,
                revision=filter_broker_configuration.attr_revision,
            ),
        )

        producer_broker_configuration_association = amazonmq.CfnConfigurationAssociation(  # noqa: F841
            self,
            "producer_broker_configuration_association",
            broker=amazonmqProducerBroker.ref,
            configuration=amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty(
                id=producer_broker_configuration.ref,
                revision=producer_broker_configuration.attr_revision,
            ),
        )

        policy = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["mq:DescribeBroker"],
                    effect=iam.Effect.ALLOW,
                    resources=["*"],
                ),
                iam.PolicyStatement(
                    actions=["secretsmanager:GetSecretValue"],
                    effect=iam.Effect.ALLOW,
                    resources=[mq_secret.secret_full_arn],
                ),
                iam.PolicyStatement(
                    actions=[
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeVpcs",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=["*"],
                ),
                iam.PolicyStatement(
                    actions=[
                        "events:PutEvents",
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=["*"],
                ),
            ]
        )
        # Pipe Role
        pipe_role = iam.Role(
            self,
            "PipeRole",
            assumed_by=iam.ServicePrincipal(service="pipes.amazonaws.com"),
            inline_policies={"pipe_policy": policy},
        )

        bus = events.EventBus(
            self, "amazonmq_filter_bus", event_bus_name="MyCustomEventBus"
        )

        mq_pipe_source_properties = pipes.CfnPipe.PipeSourceParametersProperty(
            active_mq_broker_parameters=pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty(
                credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                    basic_auth=mq_secret.secret_full_arn
                ),
                queue_name="EVENT_BRIDGE_INBOUND",
                batch_size=10,
            )
        )

        mq_pipe_target_properties = pipes.CfnPipe.PipeTargetParametersProperty(
            event_bridge_event_bus_parameters=pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty()
        )

        mq_pipe = pipes.CfnPipe(  # noqa: F841
            self,
            "PipeMQSource",
            role_arn=pipe_role.role_arn,
            source=amazonmqProducerBroker.attr_arn,
            target=bus.event_bus_arn,
            source_parameters=mq_pipe_source_properties,
            target_parameters=mq_pipe_target_properties,
        )
        ###########################################################################
        # SQS Queues
        sqs_queue_application_a_canada = sqs.Queue(
            self, "NEW_APPLICATION_A_CANADA", queue_name="NEW_APPLICATION_A_CANADA"
        )

        rule_application_a_canada = events.Rule(
            self,
            "rule_application_a_canada",
            event_pattern=events.EventPattern(
                detail={
                    "properties": {
                        "country": [{"equals-ignore-case": "canada"}],
                        "description": [{"wildcard": "*APPLICATION_A"}],
                    }
                }
            ),
            event_bus=bus,
        )

        rule_application_a_canada.add_target(
            target=targets.SqsQueue(sqs_queue_application_a_canada)
        )
        ###########################################################################
        ###########################################################################
        # SQS Queues
        sqs_queue_application_b_canada = sqs.Queue(
            self, "NEW_APPLICATION_B_CANADA", queue_name="NEW_APPLICATION_B_CANADA"
        )

        rule_application_b_canada = events.Rule(
            self,
            "rule_application_b_canada",
            event_pattern=events.EventPattern(
                detail={
                    "properties": {
                        "country": [{"equals-ignore-case": "canada"}],
                        "description": [{"wildcard": "*APPLICATION_B"}],
                    }
                }
            ),
            event_bus=bus,
        )

        rule_application_b_canada.add_target(
            target=targets.SqsQueue(sqs_queue_application_b_canada)
        )
        ###########################################################################
        ###########################################################################
        # SQS Queues
        sqs_queue_application_c_canada = sqs.Queue(
            self, "NEW_APPLICATION_C_CANADA", queue_name="NEW_APPLICATION_C_CANADA"
        )

        rule_application_c_canada = events.Rule(
            self,
            "rule_application_c_canada",
            event_pattern=events.EventPattern(
                detail={
                    "properties": {
                        "country": [{"equals-ignore-case": "canada"}],
                        "description": [{"wildcard": "*APPLICATION_C"}],
                    }
                }
            ),
            event_bus=bus,
        )

        rule_application_c_canada.add_target(
            target=targets.SqsQueue(sqs_queue_application_c_canada)
        )
        ###########################################################################
        ###########################################################################
        # SQS Queues
        sqs_queue_application_d_canada = sqs.Queue(
            self, "NEW_APPLICATION_D_CANADA", queue_name="NEW_APPLICATION_D_CANADA"
        )

        rule_application_d_canada = events.Rule(
            self,
            "rule_application_d_canada",
            event_pattern=events.EventPattern(
                detail={
                    "properties": {
                        "country": [{"equals-ignore-case": "canada"}],
                        "description": [{"wildcard": "*APPLICATION_D"}],
                    }
                }
            ),
            event_bus=bus,
        )

        rule_application_d_canada.add_target(
            target=targets.SqsQueue(sqs_queue_application_d_canada)
        )
        ###########################################################################
        ###########################################################################
        # SQS Queues
        sqs_queue_application_e_canada = sqs.Queue(
            self, "NEW_APPLICATION_E_CANADA", queue_name="NEW_APPLICATION_E_CANADA"
        )

        rule_application_e_canada = events.Rule(
            self,
            "rule_application_e_canada",
            event_pattern=events.EventPattern(
                detail={
                    "properties": {
                        "country": [{"equals-ignore-case": "canada"}],
                        "description": [{"wildcard": "*APPLICATION_E"}],
                    }
                }
            ),
            event_bus=bus,
        )

        rule_application_e_canada.add_target(
            target=targets.SqsQueue(sqs_queue_application_e_canada)
        )
        ###########################################################################
        CfnOutput(self, "AmazonMQ Secret ARN: ", value=mq_secret.secret_full_arn)
        CfnOutput(self, "Producer Broker Host: ", value=f'{amazonmqProducerBroker.ref}-1.mq.{os.environ["CDK_DEFAULT_REGION"]}.amazonaws.com' )
        CfnOutput(self, "Consumer Broker Host: ", value=f'{amazonmqConsumerBroker.ref}-1.mq.{os.environ["CDK_DEFAULT_REGION"]}.amazonaws.com')
        CfnOutput(self, "Filter Broker Host: ", value=f'{amazonmqFilterBroker.ref}-1.mq.{os.environ["CDK_DEFAULT_REGION"]}.amazonaws.com')
        CfnOutput(self, "Producer Broker Console: ", value=f'https://{os.environ["CDK_DEFAULT_REGION"]}.console.amazonaws.com/amazonmq/home?region={os.environ["CDK_DEFAULT_REGION"]}#/brokers/{amazonmqProducerBroker.ref}-1')
        CfnOutput(self, "Consumer Broker Console: ", value=f'https://{os.environ["CDK_DEFAULT_REGION"]}.console.amazonaws.com/amazonmq/home?region={os.environ["CDK_DEFAULT_REGION"]}#/brokers/{amazonmqConsumerBroker.ref}-1')
        CfnOutput(self, "Filter Broker Console: ", value=f'https://{os.environ["CDK_DEFAULT_REGION"]}.console.amazonaws.com/amazonmq/home?region={os.environ["CDK_DEFAULT_REGION"]}#/brokers/{amazonmqFilterBroker.ref}-1')
        # CfnOutput(self, "Producer Broker ARN: ", value=amazonmqProducerBroker.attr_arn)
        # CfnOutput(self, "Consumer Broker ARN: ", value=amazonmqConsumerBroker.attr_arn)
        # CfnOutput(self, "Filter Broker ARN: ", value=amazonmqFilterBroker.attr_arn)
        #SQS output
        # CfnOutput(self, "SQS Queue A: ", value=sqs_queue_application_a_canada.queue_name)
        # CfnOutput(self, "SQS Queue B: ", value=sqs_queue_application_b_canada.queue_name)
        # CfnOutput(self, "SQS Queue C: ", value=sqs_queue_application_c_canada.queue_name)
        # CfnOutput(self, "SQS Queue D: ", value=sqs_queue_application_d_canada.queue_name)
        # CfnOutput(self, "SQS Queue E: ", value=sqs_queue_application_e_canada.queue_name)
        # CfnOutput(self, "SQS Queue F: ", value=sqs_queue_application_e_canada.queue_name)
          

# Corrected CfnOutputs using the proper attributes
        # Producer Broker OpenWire SSL Endpoint
        CfnOutput(
            self,
            "AMQ_Producer_URL",
            value=f"ssl://{amazonmqProducerBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:61617",
            description="Producer Broker OpenWire SSL Endpoint"
        )

        # Consumer Broker OpenWire SSL Endpoint
        CfnOutput(
            self,
            "AMQ_Consumer_URL",
            value=f"ssl://{amazonmqConsumerBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:61617",
            description="Consumer Broker OpenWire SSL Endpoint"
        )

        # Filter Broker OpenWire SSL Endpoint
        # CfnOutput(
        #     self,
        #     "AMQ_FilterBroker_URL",
        #     value=f"ssl://{amazonmqFilterBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:61617",
        #     description="Filter Broker OpenWire SSL Endpoint"
        # )

        # Web Console URLs
        CfnOutput(
            self,
            "AMQ_ProducerBrokerConsoleURL",
            value=f"https://{amazonmqProducerBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:8162",
            description="Producer Broker Web Console URL"
        )

        CfnOutput(
            self,
            "AMQ_ConsumerBrokerConsoleURL",
            value=f"https://{amazonmqConsumerBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:8162",
            description="Consumer Broker Web Console URL"
        )

        CfnOutput(
            self,
            "AMQ_FilterBrokerConsoleURL",
            value=f"https://{amazonmqFilterBroker.ref}-1.mq.{os.environ['CDK_DEFAULT_REGION']}.amazonaws.com:8162",
            description="Filter Broker Web Console URL"
        )

        # You can also use the OpenWire endpoints attribute directly
        CfnOutput(
            self,
            "AMQ_ProducerBroker_URL",
            value=fn.join(",", amazonmqProducerBroker.attr_open_wire_endpoints),
            description="Producer Broker OpenWire Endpoints"
        )

        CfnOutput(
            self,
            "AMQ_ConsumerBroker_URL",
            value=fn.join(",", amazonmqConsumerBroker.attr_open_wire_endpoints),
            description="Consumer Broker OpenWire Endpoints"
        )

        # CfnOutput(
        #     self,
        #     "FilterBrokerOpenWireEndpoints",
        #     value=fn.join(",", amazonmqFilterBroker.attr_open_wire_endpoints),
        #     description="Filter Broker OpenWire Endpoints"
        # )


        # SQS Queue URLs for all applications
        CfnOutput(
            self,
            "ApplicationACanadaQueueUrl",
            value=f"https://sqs.{Stack.of(self).region}.amazonaws.com/{Stack.of(self).account}/NEW_APPLICATION_A_CANADA",
            description="Application A Canada Queue URL"
        )

        CfnOutput(
            self,
            "ApplicationBCanadaQueueUrl",
            value=f"https://sqs.{Stack.of(self).region}.amazonaws.com/{Stack.of(self).account}/NEW_APPLICATION_B_CANADA",
            description="Application B Canada Queue URL"
        )

        CfnOutput(
            self,
            "ApplicationCCanadaQueueUrl",
            value=f"https://sqs.{Stack.of(self).region}.amazonaws.com/{Stack.of(self).account}/NEW_APPLICATION_C_CANADA",
            description="Application C Canada Queue URL"
        )

        CfnOutput(
            self,
            "ApplicationDCanadaQueueUrl",
            value=f"https://sqs.{Stack.of(self).region}.amazonaws.com/{Stack.of(self).account}/NEW_APPLICATION_D_CANADA",
            description="Application D Canada Queue URL"
        )

        CfnOutput(
            self,
            "ApplicationECanadaQueueUrl",
            value=f"https://sqs.{Stack.of(self).region}.amazonaws.com/{Stack.of(self).account}/NEW_APPLICATION_E_CANADA",
            description="Application E Canada Queue URL"
        )
  