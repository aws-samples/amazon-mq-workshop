r'''
# AWS::ApplicationSignals Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_applicationsignals as applicationsignals
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ApplicationSignals construct libraries](https://constructs.dev/search?q=applicationsignals)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ApplicationSignals resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationSignals.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ApplicationSignals](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationSignals.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnServiceLevelObjective(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective",
):
    '''Creates or updates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations.

    Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.

    Create an SLO to set a target for a service or operation’s availability or latency. CloudWatch measures this target frequently you can find whether it has been breached.

    When you create an SLO, you set an *attainment goal* for it. An *attainment goal* is the ratio of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.

    After you have created an SLO, you can retrieve error budget reports for it. An *error budget* is the number of periods or amount of time that your service can accumulate during an interval before your overall SLO budget health is breached and the SLO is considered to be unmet. for example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.

    When you call this operation, Application Signals creates the *AWSServiceRoleForCloudWatchApplicationSignals* service-linked role, if it doesn't already exist in your account. This service- linked role has the following permissions:

    - ``xray:GetServiceGraph``
    - ``logs:StartQuery``
    - ``logs:GetQueryResults``
    - ``cloudwatch:GetMetricData``
    - ``cloudwatch:ListMetrics``
    - ``tag:GetResources``
    - ``autoscaling:DescribeAutoScalingGroups``

    You can easily set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.

    For more information about SLOs, see `Service level objectives (SLOs) <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html
    :cloudformationResource: AWS::ApplicationSignals::ServiceLevelObjective
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationsignals as applicationsignals
        
        cfn_service_level_objective = applicationsignals.CfnServiceLevelObjective(self, "MyCfnServiceLevelObjective",
            name="name",
            sli=applicationsignals.CfnServiceLevelObjective.SliProperty(
                comparison_operator="comparisonOperator",
                metric_threshold=123,
                sli_metric=applicationsignals.CfnServiceLevelObjective.SliMetricProperty(
                    key_attributes={
                        "key_attributes_key": "keyAttributes"
                    },
                    metric_data_queries=[applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty(
                        id="id",
        
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        metric_stat=applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                            metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                                dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                                    name="name",
                                    value="value"
                                )],
                                metric_name="metricName",
                                namespace="namespace"
                            ),
                            period=123,
                            stat="stat",
        
                            # the properties below are optional
                            unit="unit"
                        ),
                        return_data=False
                    )],
                    metric_type="metricType",
                    operation_name="operationName",
                    period_seconds=123,
                    statistic="statistic"
                )
            ),
        
            # the properties below are optional
            description="description",
            goal=applicationsignals.CfnServiceLevelObjective.GoalProperty(
                attainment_goal=123,
                interval=applicationsignals.CfnServiceLevelObjective.IntervalProperty(
                    calendar_interval=applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty(
                        duration=123,
                        duration_unit="durationUnit",
                        start_time=123
                    ),
                    rolling_interval=applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty(
                        duration=123,
                        duration_unit="durationUnit"
                    )
                ),
                warning_threshold=123
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        sli: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.SliProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        goal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.GoalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for this SLO.
        :param sli: A structure containing information about the performance metric that this SLO monitors.
        :param description: An optional description for this SLO. Default: - "No description"
        :param goal: This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.
        :param tags: A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the cloudwatch:TagResource permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8476d024be5b448cfb8f9ae2f80fa7f2083296f712cdb7cd12e69365dd7adba1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceLevelObjectiveProps(
            name=name, sli=sli, description=description, goal=goal, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71593741af71e952b8edcbf3d4a100ccac3627fda6dcff137c7d24df9820e5bb)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922e83db8165cd861bbc31a25dc4a9c84e6441a3e72c10857eb4ba5ae99314cd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of this SLO.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> jsii.Number:
        '''The date and time that this SLO was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> jsii.Number:
        '''The time that this SLO was most recently updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for this SLO.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d1b42972f3b8a4430dca27e7ecab3fce56490ad1edcfabdc346becf5f4c998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sli")
    def sli(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.SliProperty"]:
        '''A structure containing information about the performance metric that this SLO monitors.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.SliProperty"], jsii.get(self, "sli"))

    @sli.setter
    def sli(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.SliProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938ccf6991aba4b5875a4ca09dfcdb00a5c7e9a92bba0e785ddfbebb228037c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sli", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this SLO.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6761a51565a6d9d6b93723803df5fa7735ec11aa5f14c9cc222e4e60eb54506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="goal")
    def goal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.GoalProperty"]]:
        '''This structure contains the attributes that determine the goal of an SLO.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.GoalProperty"]], jsii.get(self, "goal"))

    @goal.setter
    def goal(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.GoalProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72f1f3f286714a7cb6611be91fc84bc135d11974635585192dc6a6bbfe2f51e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goal", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the SLO.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45578973503123093d3b0c8f845e2df0c9ad023b7df510f3a7b7ee7abcccd506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration": "duration",
            "duration_unit": "durationUnit",
            "start_time": "startTime",
        },
    )
    class CalendarIntervalProperty:
        def __init__(
            self,
            *,
            duration: jsii.Number,
            duration_unit: builtins.str,
            start_time: jsii.Number,
        ) -> None:
            '''If the interval for this service level objective is a calendar interval, this structure contains the interval specifications.

            :param duration: Specifies the duration of each calendar interval. For example, if ``Duration`` is ``1`` and ``DurationUnit`` is ``MONTH`` , each interval is one month, aligned with the calendar.
            :param duration_unit: Specifies the calendar interval unit.
            :param start_time: The date and time when you want the first interval to start. Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: ``1698778057`` As soon as one calendar interval ends, another automatically begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-calendarinterval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                calendar_interval_property = applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty(
                    duration=123,
                    duration_unit="durationUnit",
                    start_time=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb256cb6878f107649da0ff6e94d5a653ad8e2c683a434ba458525e129419535)
                check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
                check_type(argname="argument duration_unit", value=duration_unit, expected_type=type_hints["duration_unit"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "duration": duration,
                "duration_unit": duration_unit,
                "start_time": start_time,
            }

        @builtins.property
        def duration(self) -> jsii.Number:
            '''Specifies the duration of each calendar interval.

            For example, if ``Duration`` is ``1`` and ``DurationUnit`` is ``MONTH`` , each interval is one month, aligned with the calendar.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-calendarinterval.html#cfn-applicationsignals-servicelevelobjective-calendarinterval-duration
            '''
            result = self._values.get("duration")
            assert result is not None, "Required property 'duration' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def duration_unit(self) -> builtins.str:
            '''Specifies the calendar interval unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-calendarinterval.html#cfn-applicationsignals-servicelevelobjective-calendarinterval-durationunit
            '''
            result = self._values.get("duration_unit")
            assert result is not None, "Required property 'duration_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> jsii.Number:
            '''The date and time when you want the first interval to start.

            Be sure to choose a time that configures the intervals the way that you want. For example, if you want weekly intervals starting on Mondays at 6 a.m., be sure to specify a start time that is a Monday at 6 a.m.

            When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: ``1698778057``

            As soon as one calendar interval ends, another automatically begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-calendarinterval.html#cfn-applicationsignals-servicelevelobjective-calendarinterval-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CalendarIntervalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''A dimension is a name/value pair that is part of the identity of a metric.

            Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish ``InstanceId`` as a dimension name, and the actual instance ID as the value for that dimension.

            You can assign up to 30 dimensions to a metric.

            :param name: The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon ( ``:`` ). ASCII control characters are not supported as part of dimension names.
            :param value: The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                dimension_property = applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e8e6b95cda618658802fc7b704459e5b42989b01fe12f60c38caea77f865804)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension.

            Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon ( ``:`` ). ASCII control characters are not supported as part of dimension names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-dimension.html#cfn-applicationsignals-servicelevelobjective-dimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-dimension.html#cfn-applicationsignals-servicelevelobjective-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.GoalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attainment_goal": "attainmentGoal",
            "interval": "interval",
            "warning_threshold": "warningThreshold",
        },
    )
    class GoalProperty:
        def __init__(
            self,
            *,
            attainment_goal: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.IntervalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            warning_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''This structure contains the attributes that determine the goal of an SLO.

            This includes the time period for evaluation and the attainment threshold.

            :param attainment_goal: The threshold that determines if the goal is being met. An *attainment goal* is the ratio of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state. If you omit this parameter, 99 is used to represent 99% as the attainment goal.
            :param interval: The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval. If you omit this parameter, a rolling interval of 7 days is used.
            :param warning_threshold: The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-goal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                goal_property = applicationsignals.CfnServiceLevelObjective.GoalProperty(
                    attainment_goal=123,
                    interval=applicationsignals.CfnServiceLevelObjective.IntervalProperty(
                        calendar_interval=applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty(
                            duration=123,
                            duration_unit="durationUnit",
                            start_time=123
                        ),
                        rolling_interval=applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty(
                            duration=123,
                            duration_unit="durationUnit"
                        )
                    ),
                    warning_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfc131adfea10ec8f2150d53534dabca2819dd847e258cdb22dd5820d87c65e9)
                check_type(argname="argument attainment_goal", value=attainment_goal, expected_type=type_hints["attainment_goal"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument warning_threshold", value=warning_threshold, expected_type=type_hints["warning_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attainment_goal is not None:
                self._values["attainment_goal"] = attainment_goal
            if interval is not None:
                self._values["interval"] = interval
            if warning_threshold is not None:
                self._values["warning_threshold"] = warning_threshold

        @builtins.property
        def attainment_goal(self) -> typing.Optional[jsii.Number]:
            '''The threshold that determines if the goal is being met.

            An *attainment goal* is the ratio of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.

            If you omit this parameter, 99 is used to represent 99% as the attainment goal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-goal.html#cfn-applicationsignals-servicelevelobjective-goal-attainmentgoal
            '''
            result = self._values.get("attainment_goal")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.IntervalProperty"]]:
            '''The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.

            If you omit this parameter, a rolling interval of 7 days is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-goal.html#cfn-applicationsignals-servicelevelobjective-goal-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.IntervalProperty"]], result)

        @builtins.property
        def warning_threshold(self) -> typing.Optional[jsii.Number]:
            '''The percentage of remaining budget over total budget that you want to get warnings for.

            If you omit this parameter, the default of 50.0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-goal.html#cfn-applicationsignals-servicelevelobjective-goal-warningthreshold
            '''
            result = self._values.get("warning_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GoalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.IntervalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "calendar_interval": "calendarInterval",
            "rolling_interval": "rollingInterval",
        },
    )
    class IntervalProperty:
        def __init__(
            self,
            *,
            calendar_interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.CalendarIntervalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rolling_interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.RollingIntervalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The time period used to evaluate the SLO.

            It can be either a calendar interval or rolling interval.

            :param calendar_interval: If the interval is a calendar interval, this structure contains the interval specifications.
            :param rolling_interval: If the interval is a rolling interval, this structure contains the interval specifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-interval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                interval_property = applicationsignals.CfnServiceLevelObjective.IntervalProperty(
                    calendar_interval=applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty(
                        duration=123,
                        duration_unit="durationUnit",
                        start_time=123
                    ),
                    rolling_interval=applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty(
                        duration=123,
                        duration_unit="durationUnit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30cac26980883e0f67d516f4ddebfd0c363ae3aeb6eb60f4ae3e55228be79fc8)
                check_type(argname="argument calendar_interval", value=calendar_interval, expected_type=type_hints["calendar_interval"])
                check_type(argname="argument rolling_interval", value=rolling_interval, expected_type=type_hints["rolling_interval"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if calendar_interval is not None:
                self._values["calendar_interval"] = calendar_interval
            if rolling_interval is not None:
                self._values["rolling_interval"] = rolling_interval

        @builtins.property
        def calendar_interval(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.CalendarIntervalProperty"]]:
            '''If the interval is a calendar interval, this structure contains the interval specifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-interval.html#cfn-applicationsignals-servicelevelobjective-interval-calendarinterval
            '''
            result = self._values.get("calendar_interval")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.CalendarIntervalProperty"]], result)

        @builtins.property
        def rolling_interval(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.RollingIntervalProperty"]]:
            '''If the interval is a rolling interval, this structure contains the interval specifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-interval.html#cfn-applicationsignals-servicelevelobjective-interval-rollinginterval
            '''
            result = self._values.get("rolling_interval")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.RollingIntervalProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntervalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "account_id": "accountId",
            "expression": "expression",
            "metric_stat": "metricStat",
            "return_data": "returnData",
        },
    )
    class MetricDataQueryProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            account_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.MetricStatProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Use this structure to define a metric or metric math expression that you want to use as for a service level objective.

            Each ``MetricDataQuery`` in the ``MetricDataQueries`` array specifies either a metric to retrieve, or a metric math expression to be performed on retrieved metrics. A single ``MetricDataQueries`` array can include as many as 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of those ``Expression`` structures, exactly one must have true as the value for ``ReturnData`` . The result of this expression used for the SLO.

            For more information about metric math expressions, see `Use metric math <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html>`_ .

            Within each ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :param id: A short name used to tie this object to the results in the response. This ``Id`` must be unique within a ``MetricDataQueries`` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            :param account_id: The ID of the account where this metric is located. If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.
            :param expression: This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this ``MetricDataQueries`` structure. A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* . Within each ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param metric_stat: A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO. Within one ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param return_data: Use this only if you are using a metric math expression for the SLO. Specify ``true`` for ``ReturnData`` for only the one expression result to use as the alarm. For all other metrics and expressions in the same ``CreateServiceLevelObjective`` operation, specify ``ReturnData`` as ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                metric_data_query_property = applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty(
                    id="id",
                
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    metric_stat=applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                        metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                            dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        period=123,
                        stat="stat",
                
                        # the properties below are optional
                        unit="unit"
                    ),
                    return_data=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c04fce2d6f659e54bcf95336fd734b9dda8c1a66b044793f92533f4b2b9ac20c)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
                check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if account_id is not None:
                self._values["account_id"] = account_id
            if expression is not None:
                self._values["expression"] = expression
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def id(self) -> builtins.str:
            '''A short name used to tie this object to the results in the response.

            This ``Id`` must be unique within a ``MetricDataQueries`` array. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the metric math expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html#cfn-applicationsignals-servicelevelobjective-metricdataquery-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the account where this metric is located.

            If you are performing this operation in a monitoring account, use this to specify which source account to retrieve this metric from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html#cfn-applicationsignals-servicelevelobjective-metricdataquery-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''This field can contain a metric math expression to be performed on the other metrics that you are retrieving within this ``MetricDataQueries`` structure.

            A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Within each ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html#cfn-applicationsignals-servicelevelobjective-metricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricStatProperty"]]:
            '''A metric to be used directly for the SLO, or to be used in the math expression that will be used for the SLO.

            Within one ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html#cfn-applicationsignals-servicelevelobjective-metricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricStatProperty"]], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use this only if you are using a metric math expression for the SLO.

            Specify ``true`` for ``ReturnData`` for only the one expression result to use as the alarm. For all other metrics and expressions in the same ``CreateServiceLevelObjective`` operation, specify ``ReturnData`` as ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricdataquery.html#cfn-applicationsignals-servicelevelobjective-metricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric used for a service level indicator, including the metric name, namespace, and dimensions.

            :param dimensions: An array of one or more dimensions to use to define the metric that you want to use. For more information, see `Dimensions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension>`_ .
            :param metric_name: The name of the metric to use.
            :param namespace: The namespace of the metric. For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                metric_property = applicationsignals.CfnServiceLevelObjective.MetricProperty(
                    dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94c3dac51fe1c8fc13cb0f314cd26fbce563c808cc2f39fe4ee2a01d00f47555)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.DimensionProperty"]]]]:
            '''An array of one or more dimensions to use to define the metric that you want to use.

            For more information, see `Dimensions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metric.html#cfn-applicationsignals-servicelevelobjective-metric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.DimensionProperty"]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metric.html#cfn-applicationsignals-servicelevelobjective-metric-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric.

            For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metric.html#cfn-applicationsignals-servicelevelobjective-metric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.MetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric": "metric",
            "period": "period",
            "stat": "stat",
            "unit": "unit",
        },
    )
    class MetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.MetricProperty", typing.Dict[builtins.str, typing.Any]]],
            period: jsii.Number,
            stat: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric to be used as the service level indicator, along with the statistics, period, and unit.

            :param metric: The metric to use as the service level indicator, including the metric name, namespace, and dimensions.
            :param period: The granularity, in seconds, to be used for the metric. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.
            :param stat: The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ .
            :param unit: If you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                metric_stat_property = applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                    metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                        dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    period=123,
                    stat="stat",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9112cc9d5e83260e285e14202026cd0c682ccbbd611252cb22444f31adb6fc6c)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric": metric,
                "period": period,
                "stat": stat,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricProperty"]:
            '''The metric to use as the service level indicator, including the metric name, namespace, and dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricstat.html#cfn-applicationsignals-servicelevelobjective-metricstat-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricProperty"], result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The granularity, in seconds, to be used for the metric.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricstat.html#cfn-applicationsignals-servicelevelobjective-metricstat-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def stat(self) -> builtins.str:
            '''The statistic to use for comparison to the threshold.

            It can be any CloudWatch statistic or extended statistic. For more information about statistics, see `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricstat.html#cfn-applicationsignals-servicelevelobjective-metricstat-stat
            '''
            result = self._values.get("stat")
            assert result is not None, "Required property 'stat' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''If you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch.

            If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-metricstat.html#cfn-applicationsignals-servicelevelobjective-metricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty",
        jsii_struct_bases=[],
        name_mapping={"duration": "duration", "duration_unit": "durationUnit"},
    )
    class RollingIntervalProperty:
        def __init__(
            self,
            *,
            duration: jsii.Number,
            duration_unit: builtins.str,
        ) -> None:
            '''If the interval for this SLO is a rolling interval, this structure contains the interval specifications.

            :param duration: Specifies the duration of each rolling interval. For example, if ``Duration`` is ``7`` and ``DurationUnit`` is ``DAY`` , each rolling interval is seven days.
            :param duration_unit: Specifies the rolling interval unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-rollinginterval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                rolling_interval_property = applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty(
                    duration=123,
                    duration_unit="durationUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ea5efcc7f9d7eb11cc8de5d96525adb6a7e2bfc30446b0fcdb3c7cd640413c1)
                check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
                check_type(argname="argument duration_unit", value=duration_unit, expected_type=type_hints["duration_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "duration": duration,
                "duration_unit": duration_unit,
            }

        @builtins.property
        def duration(self) -> jsii.Number:
            '''Specifies the duration of each rolling interval.

            For example, if ``Duration`` is ``7`` and ``DurationUnit`` is ``DAY`` , each rolling interval is seven days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-rollinginterval.html#cfn-applicationsignals-servicelevelobjective-rollinginterval-duration
            '''
            result = self._values.get("duration")
            assert result is not None, "Required property 'duration' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def duration_unit(self) -> builtins.str:
            '''Specifies the rolling interval unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-rollinginterval.html#cfn-applicationsignals-servicelevelobjective-rollinginterval-durationunit
            '''
            result = self._values.get("duration_unit")
            assert result is not None, "Required property 'duration_unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RollingIntervalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.SliMetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_attributes": "keyAttributes",
            "metric_data_queries": "metricDataQueries",
            "metric_type": "metricType",
            "operation_name": "operationName",
            "period_seconds": "periodSeconds",
            "statistic": "statistic",
        },
    )
    class SliMetricProperty:
        def __init__(
            self,
            *,
            key_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            metric_data_queries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.MetricDataQueryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_type: typing.Optional[builtins.str] = None,
            operation_name: typing.Optional[builtins.str] = None,
            period_seconds: typing.Optional[jsii.Number] = None,
            statistic: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to specify the metric to be used for the SLO.

            :param key_attributes: If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to. To do so, you must specify at least the ``Type`` , ``Name`` , and ``Environment`` attributes. This is a string-to-string map. It can include the following fields. - ``Type`` designates the type of object this is. - ``ResourceType`` specifies the type of the resource. This field is used only when the value of the ``Type`` field is ``Resource`` or ``AWS::Resource`` . - ``Name`` specifies the name of the object. This is used only if the value of the ``Type`` field is ``Service`` , ``RemoteService`` , or ``AWS::Service`` . - ``Identifier`` identifies the resource objects of this resource. This is used only if the value of the ``Type`` field is ``Resource`` or ``AWS::Resource`` . - ``Environment`` specifies the location where this object is hosted, or what it belongs to.
            :param metric_data_queries: If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression.
            :param metric_type: If the SLO is to monitor either the ``LATENCY`` or ``AVAILABILITY`` metric that Application Signals collects, use this field to specify which of those metrics is used.
            :param operation_name: If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.
            :param period_seconds: The number of seconds to use as the period for SLO evaluation. Your application's performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.
            :param statistic: The statistic to use for comparison to the threshold. It can be any CloudWatch statistic or extended statistic. For more information about statistics, see `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                sli_metric_property = applicationsignals.CfnServiceLevelObjective.SliMetricProperty(
                    key_attributes={
                        "key_attributes_key": "keyAttributes"
                    },
                    metric_data_queries=[applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty(
                        id="id",
                
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        metric_stat=applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                            metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                                dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                                    name="name",
                                    value="value"
                                )],
                                metric_name="metricName",
                                namespace="namespace"
                            ),
                            period=123,
                            stat="stat",
                
                            # the properties below are optional
                            unit="unit"
                        ),
                        return_data=False
                    )],
                    metric_type="metricType",
                    operation_name="operationName",
                    period_seconds=123,
                    statistic="statistic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86b5c7cbf1916d1f3e415fc49b371acf007c9210e4158ca70f0735fb4ce3ca36)
                check_type(argname="argument key_attributes", value=key_attributes, expected_type=type_hints["key_attributes"])
                check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
                check_type(argname="argument metric_type", value=metric_type, expected_type=type_hints["metric_type"])
                check_type(argname="argument operation_name", value=operation_name, expected_type=type_hints["operation_name"])
                check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key_attributes is not None:
                self._values["key_attributes"] = key_attributes
            if metric_data_queries is not None:
                self._values["metric_data_queries"] = metric_data_queries
            if metric_type is not None:
                self._values["metric_type"] = metric_type
            if operation_name is not None:
                self._values["operation_name"] = operation_name
            if period_seconds is not None:
                self._values["period_seconds"] = period_seconds
            if statistic is not None:
                self._values["statistic"] = statistic

        @builtins.property
        def key_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''If this SLO is related to a metric collected by Application Signals, you must use this field to specify which service the SLO metric is related to.

            To do so, you must specify at least the ``Type`` , ``Name`` , and ``Environment`` attributes.

            This is a string-to-string map. It can include the following fields.

            - ``Type`` designates the type of object this is.
            - ``ResourceType`` specifies the type of the resource. This field is used only when the value of the ``Type`` field is ``Resource`` or ``AWS::Resource`` .
            - ``Name`` specifies the name of the object. This is used only if the value of the ``Type`` field is ``Service`` , ``RemoteService`` , or ``AWS::Service`` .
            - ``Identifier`` identifies the resource objects of this resource. This is used only if the value of the ``Type`` field is ``Resource`` or ``AWS::Resource`` .
            - ``Environment`` specifies the location where this object is hosted, or what it belongs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-keyattributes
            '''
            result = self._values.get("key_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def metric_data_queries(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricDataQueryProperty"]]]]:
            '''If this SLO monitors a CloudWatch metric or the result of a CloudWatch metric math expression, use this structure to specify that metric or expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-metricdataqueries
            '''
            result = self._values.get("metric_data_queries")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.MetricDataQueryProperty"]]]], result)

        @builtins.property
        def metric_type(self) -> typing.Optional[builtins.str]:
            '''If the SLO is to monitor either the ``LATENCY`` or ``AVAILABILITY`` metric that Application Signals collects, use this field to specify which of those metrics is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-metrictype
            '''
            result = self._values.get("metric_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operation_name(self) -> typing.Optional[builtins.str]:
            '''If the SLO is to monitor a specific operation of the service, use this field to specify the name of that operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-operationname
            '''
            result = self._values.get("operation_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def period_seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds to use as the period for SLO evaluation.

            Your application's performance is compared to the SLI during each period. For each period, the application is determined to have either achieved or not achieved the necessary performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-periodseconds
            '''
            result = self._values.get("period_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The statistic to use for comparison to the threshold.

            It can be any CloudWatch statistic or extended statistic. For more information about statistics, see `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-slimetric.html#cfn-applicationsignals-servicelevelobjective-slimetric-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SliMetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjective.SliProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "metric_threshold": "metricThreshold",
            "sli_metric": "sliMetric",
        },
    )
    class SliProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            metric_threshold: jsii.Number,
            sli_metric: typing.Union[_IResolvable_da3f097b, typing.Union["CfnServiceLevelObjective.SliMetricProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''This structure specifies the information about the service and the performance metric that an SLO is to monitor.

            :param comparison_operator: The arithmetic operation to use when comparing the specified metric to the threshold.
            :param metric_threshold: The value that the SLI metric is compared to.
            :param sli_metric: Use this structure to specify the metric to be used for the SLO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-sli.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationsignals as applicationsignals
                
                sli_property = applicationsignals.CfnServiceLevelObjective.SliProperty(
                    comparison_operator="comparisonOperator",
                    metric_threshold=123,
                    sli_metric=applicationsignals.CfnServiceLevelObjective.SliMetricProperty(
                        key_attributes={
                            "key_attributes_key": "keyAttributes"
                        },
                        metric_data_queries=[applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty(
                            id="id",
                
                            # the properties below are optional
                            account_id="accountId",
                            expression="expression",
                            metric_stat=applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                                metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                                    dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                                        name="name",
                                        value="value"
                                    )],
                                    metric_name="metricName",
                                    namespace="namespace"
                                ),
                                period=123,
                                stat="stat",
                
                                # the properties below are optional
                                unit="unit"
                            ),
                            return_data=False
                        )],
                        metric_type="metricType",
                        operation_name="operationName",
                        period_seconds=123,
                        statistic="statistic"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fcb2d383c03844ff1706f4720c7bf04c5a00252d1e49f3ecb2c00c22bf5cbe1f)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument metric_threshold", value=metric_threshold, expected_type=type_hints["metric_threshold"])
                check_type(argname="argument sli_metric", value=sli_metric, expected_type=type_hints["sli_metric"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "metric_threshold": metric_threshold,
                "sli_metric": sli_metric,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''The arithmetic operation to use when comparing the specified metric to the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-sli.html#cfn-applicationsignals-servicelevelobjective-sli-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_threshold(self) -> jsii.Number:
            '''The value that the SLI metric is compared to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-sli.html#cfn-applicationsignals-servicelevelobjective-sli-metricthreshold
            '''
            result = self._values.get("metric_threshold")
            assert result is not None, "Required property 'metric_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def sli_metric(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.SliMetricProperty"]:
            '''Use this structure to specify the metric to be used for the SLO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationsignals-servicelevelobjective-sli.html#cfn-applicationsignals-servicelevelobjective-sli-slimetric
            '''
            result = self._values.get("sli_metric")
            assert result is not None, "Required property 'sli_metric' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnServiceLevelObjective.SliMetricProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SliProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationsignals.CfnServiceLevelObjectiveProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "sli": "sli",
        "description": "description",
        "goal": "goal",
        "tags": "tags",
    },
)
class CfnServiceLevelObjectiveProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        sli: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.SliProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        goal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.GoalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceLevelObjective``.

        :param name: A name for this SLO.
        :param sli: A structure containing information about the performance metric that this SLO monitors.
        :param description: An optional description for this SLO. Default: - "No description"
        :param goal: This structure contains the attributes that determine the goal of an SLO. This includes the time period for evaluation and the attainment threshold.
        :param tags: A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the cloudwatch:TagResource permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationsignals as applicationsignals
            
            cfn_service_level_objective_props = applicationsignals.CfnServiceLevelObjectiveProps(
                name="name",
                sli=applicationsignals.CfnServiceLevelObjective.SliProperty(
                    comparison_operator="comparisonOperator",
                    metric_threshold=123,
                    sli_metric=applicationsignals.CfnServiceLevelObjective.SliMetricProperty(
                        key_attributes={
                            "key_attributes_key": "keyAttributes"
                        },
                        metric_data_queries=[applicationsignals.CfnServiceLevelObjective.MetricDataQueryProperty(
                            id="id",
            
                            # the properties below are optional
                            account_id="accountId",
                            expression="expression",
                            metric_stat=applicationsignals.CfnServiceLevelObjective.MetricStatProperty(
                                metric=applicationsignals.CfnServiceLevelObjective.MetricProperty(
                                    dimensions=[applicationsignals.CfnServiceLevelObjective.DimensionProperty(
                                        name="name",
                                        value="value"
                                    )],
                                    metric_name="metricName",
                                    namespace="namespace"
                                ),
                                period=123,
                                stat="stat",
            
                                # the properties below are optional
                                unit="unit"
                            ),
                            return_data=False
                        )],
                        metric_type="metricType",
                        operation_name="operationName",
                        period_seconds=123,
                        statistic="statistic"
                    )
                ),
            
                # the properties below are optional
                description="description",
                goal=applicationsignals.CfnServiceLevelObjective.GoalProperty(
                    attainment_goal=123,
                    interval=applicationsignals.CfnServiceLevelObjective.IntervalProperty(
                        calendar_interval=applicationsignals.CfnServiceLevelObjective.CalendarIntervalProperty(
                            duration=123,
                            duration_unit="durationUnit",
                            start_time=123
                        ),
                        rolling_interval=applicationsignals.CfnServiceLevelObjective.RollingIntervalProperty(
                            duration=123,
                            duration_unit="durationUnit"
                        )
                    ),
                    warning_threshold=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a302456885343cc9ce5e0497feed773de1ef0f44e2934f97458bfdc5a810dee)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sli", value=sli, expected_type=type_hints["sli"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument goal", value=goal, expected_type=type_hints["goal"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "sli": sli,
        }
        if description is not None:
            self._values["description"] = description
        if goal is not None:
            self._values["goal"] = goal
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for this SLO.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html#cfn-applicationsignals-servicelevelobjective-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sli(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.SliProperty]:
        '''A structure containing information about the performance metric that this SLO monitors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html#cfn-applicationsignals-servicelevelobjective-sli
        '''
        result = self._values.get("sli")
        assert result is not None, "Required property 'sli' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.SliProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this SLO.

        :default: - "No description"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html#cfn-applicationsignals-servicelevelobjective-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def goal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.GoalProperty]]:
        '''This structure contains the attributes that determine the goal of an SLO.

        This includes the time period for evaluation and the attainment threshold.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html#cfn-applicationsignals-servicelevelobjective-goal
        '''
        result = self._values.get("goal")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.GoalProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the SLO.

        You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the cloudwatch:TagResource permission.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationsignals-servicelevelobjective.html#cfn-applicationsignals-servicelevelobjective-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceLevelObjectiveProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServiceLevelObjective",
    "CfnServiceLevelObjectiveProps",
]

publication.publish()

def _typecheckingstub__8476d024be5b448cfb8f9ae2f80fa7f2083296f712cdb7cd12e69365dd7adba1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    sli: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.SliProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    goal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.GoalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71593741af71e952b8edcbf3d4a100ccac3627fda6dcff137c7d24df9820e5bb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922e83db8165cd861bbc31a25dc4a9c84e6441a3e72c10857eb4ba5ae99314cd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d1b42972f3b8a4430dca27e7ecab3fce56490ad1edcfabdc346becf5f4c998(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938ccf6991aba4b5875a4ca09dfcdb00a5c7e9a92bba0e785ddfbebb228037c3(
    value: typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.SliProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6761a51565a6d9d6b93723803df5fa7735ec11aa5f14c9cc222e4e60eb54506(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72f1f3f286714a7cb6611be91fc84bc135d11974635585192dc6a6bbfe2f51e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServiceLevelObjective.GoalProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45578973503123093d3b0c8f845e2df0c9ad023b7df510f3a7b7ee7abcccd506(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb256cb6878f107649da0ff6e94d5a653ad8e2c683a434ba458525e129419535(
    *,
    duration: jsii.Number,
    duration_unit: builtins.str,
    start_time: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8e6b95cda618658802fc7b704459e5b42989b01fe12f60c38caea77f865804(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc131adfea10ec8f2150d53534dabca2819dd847e258cdb22dd5820d87c65e9(
    *,
    attainment_goal: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.IntervalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    warning_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30cac26980883e0f67d516f4ddebfd0c363ae3aeb6eb60f4ae3e55228be79fc8(
    *,
    calendar_interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.CalendarIntervalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rolling_interval: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.RollingIntervalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c04fce2d6f659e54bcf95336fd734b9dda8c1a66b044793f92533f4b2b9ac20c(
    *,
    id: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    expression: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.MetricStatProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c3dac51fe1c8fc13cb0f314cd26fbce563c808cc2f39fe4ee2a01d00f47555(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9112cc9d5e83260e285e14202026cd0c682ccbbd611252cb22444f31adb6fc6c(
    *,
    metric: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.MetricProperty, typing.Dict[builtins.str, typing.Any]]],
    period: jsii.Number,
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea5efcc7f9d7eb11cc8de5d96525adb6a7e2bfc30446b0fcdb3c7cd640413c1(
    *,
    duration: jsii.Number,
    duration_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b5c7cbf1916d1f3e415fc49b371acf007c9210e4158ca70f0735fb4ce3ca36(
    *,
    key_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    metric_data_queries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.MetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_type: typing.Optional[builtins.str] = None,
    operation_name: typing.Optional[builtins.str] = None,
    period_seconds: typing.Optional[jsii.Number] = None,
    statistic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb2d383c03844ff1706f4720c7bf04c5a00252d1e49f3ecb2c00c22bf5cbe1f(
    *,
    comparison_operator: builtins.str,
    metric_threshold: jsii.Number,
    sli_metric: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.SliMetricProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a302456885343cc9ce5e0497feed773de1ef0f44e2934f97458bfdc5a810dee(
    *,
    name: builtins.str,
    sli: typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.SliProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    goal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServiceLevelObjective.GoalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
