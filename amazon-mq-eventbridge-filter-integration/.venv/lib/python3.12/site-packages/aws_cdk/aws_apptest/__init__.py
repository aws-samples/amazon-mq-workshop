r'''
# AWS::AppTest Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_apptest as apptest
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppTest construct libraries](https://constructs.dev/search?q=apptest)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppTest resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppTest.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppTest](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppTest.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTestCase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase",
):
    '''Creates a test case for an application.

    For more information about test cases, see `Test cases <https://docs.aws.amazon.com/m2/latest/userguide/testing-test-cases.html>`_ and `Application Testing concepts <https://docs.aws.amazon.com/m2/latest/userguide/concepts-apptest.html>`_ in the *AWS Mainframe Modernization User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html
    :cloudformationResource: AWS::AppTest::TestCase
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apptest as apptest
        
        cfn_test_case = apptest.CfnTestCase(self, "MyCfnTestCase",
            name="name",
            steps=[apptest.CfnTestCase.StepProperty(
                action=apptest.CfnTestCase.StepActionProperty(
                    compare_action=apptest.CfnTestCase.CompareActionProperty(
                        input=apptest.CfnTestCase.InputProperty(
                            file=apptest.CfnTestCase.InputFileProperty(
                                file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                                    database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                        source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                            capture_tool="captureTool",
                                            type="type"
                                        ),
                                        target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                            capture_tool="captureTool",
                                            type="type"
                                        )
                                    ),
                                    data_sets=[apptest.CfnTestCase.DataSetProperty(
                                        ccsid="ccsid",
                                        format="format",
                                        length=123,
                                        name="name",
                                        type="type"
                                    )]
                                ),
                                source_location="sourceLocation",
                                target_location="targetLocation"
                            )
                        ),
        
                        # the properties below are optional
                        output=apptest.CfnTestCase.OutputProperty(
                            file=apptest.CfnTestCase.OutputFileProperty(
                                file_location="fileLocation"
                            )
                        )
                    ),
                    mainframe_action=apptest.CfnTestCase.MainframeActionProperty(
                        action_type=apptest.CfnTestCase.MainframeActionTypeProperty(
                            batch=apptest.CfnTestCase.BatchProperty(
                                batch_job_name="batchJobName",
        
                                # the properties below are optional
                                batch_job_parameters={
                                    "batch_job_parameters_key": "batchJobParameters"
                                },
                                export_data_set_names=["exportDataSetNames"]
                            ),
                            tn3270=apptest.CfnTestCase.TN3270Property(
                                script=apptest.CfnTestCase.ScriptProperty(
                                    script_location="scriptLocation",
                                    type="type"
                                ),
        
                                # the properties below are optional
                                export_data_set_names=["exportDataSetNames"]
                            )
                        ),
                        resource="resource",
        
                        # the properties below are optional
                        properties=apptest.CfnTestCase.MainframeActionPropertiesProperty(
                            dms_task_arn="dmsTaskArn"
                        )
                    ),
                    resource_action=apptest.CfnTestCase.ResourceActionProperty(
                        cloud_formation_action=apptest.CfnTestCase.CloudFormationActionProperty(
                            resource="resource",
        
                            # the properties below are optional
                            action_type="actionType"
                        ),
                        m2_managed_application_action=apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                            action_type="actionType",
                            resource="resource",
        
                            # the properties below are optional
                            properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                                force_stop=False,
                                import_data_set_location="importDataSetLocation"
                            )
                        ),
                        m2_non_managed_application_action=apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                            action_type="actionType",
                            resource="resource"
                        )
                    )
                ),
                name="name",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.StepProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the test case.
        :param steps: The steps in the test case.
        :param description: The description of the test case.
        :param tags: The specified tags of the test case.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54328fdade9df4505a5f85498cf53fc62e7fc59a222ac471d1a63974ed7f0a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTestCaseProps(
            name=name, steps=steps, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224090306333e2fc48135738c3d25b5e41f34e68b81b058fbfb26e7eda0deb3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b44c10d3df56f34cf8ff918478ccaaa747cba69c96444d92b98e0cf0cb4efe1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The creation time of the test case.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateTime")
    def attr_last_update_time(self) -> builtins.str:
        '''The last update time of the test case.

        :cloudformationAttribute: LastUpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestVersion")
    def attr_latest_version(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: LatestVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLatestVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the test case.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTestCaseArn")
    def attr_test_case_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the test case.

        :cloudformationAttribute: TestCaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTestCaseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTestCaseId")
    def attr_test_case_id(self) -> builtins.str:
        '''The response test case ID of the test case.

        :cloudformationAttribute: TestCaseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTestCaseId"))

    @builtins.property
    @jsii.member(jsii_name="attrTestCaseVersion")
    def attr_test_case_version(self) -> _IResolvable_da3f097b:
        '''The version of the test case.

        :cloudformationAttribute: TestCaseVersion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrTestCaseVersion"))

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
        '''The name of the test case.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b8945362e3fa289aad135a767811c67a4cdb45010d2377c0fb6dd670ca829f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTestCase.StepProperty"]]]:
        '''The steps in the test case.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTestCase.StepProperty"]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTestCase.StepProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0a0c6d80a2bab21c010f9956a7784691e07a0d6ed782a3cc4f9fe81b470a060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "steps", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the test case.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d3be2bb2b7f3fe2d6ec231a15d229997932dffe177165c78ec826c8431cca3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The specified tags of the test case.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e8acfd7d3d54fa56bbe1ab5b9bc79609eaccb189083fe4b8cc7217ad659a8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.BatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "batch_job_name": "batchJobName",
            "batch_job_parameters": "batchJobParameters",
            "export_data_set_names": "exportDataSetNames",
        },
    )
    class BatchProperty:
        def __init__(
            self,
            *,
            batch_job_name: builtins.str,
            batch_job_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            export_data_set_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines a batch.

            :param batch_job_name: The job name of the batch.
            :param batch_job_parameters: The batch job parameters of the batch.
            :param export_data_set_names: The export data set names of the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-batch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                batch_property = apptest.CfnTestCase.BatchProperty(
                    batch_job_name="batchJobName",
                
                    # the properties below are optional
                    batch_job_parameters={
                        "batch_job_parameters_key": "batchJobParameters"
                    },
                    export_data_set_names=["exportDataSetNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__22fbc9e8380b6b0f7acb2ff9ce8665660f1341dbe513e19f269854edf36bf947)
                check_type(argname="argument batch_job_name", value=batch_job_name, expected_type=type_hints["batch_job_name"])
                check_type(argname="argument batch_job_parameters", value=batch_job_parameters, expected_type=type_hints["batch_job_parameters"])
                check_type(argname="argument export_data_set_names", value=export_data_set_names, expected_type=type_hints["export_data_set_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "batch_job_name": batch_job_name,
            }
            if batch_job_parameters is not None:
                self._values["batch_job_parameters"] = batch_job_parameters
            if export_data_set_names is not None:
                self._values["export_data_set_names"] = export_data_set_names

        @builtins.property
        def batch_job_name(self) -> builtins.str:
            '''The job name of the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-batch.html#cfn-apptest-testcase-batch-batchjobname
            '''
            result = self._values.get("batch_job_name")
            assert result is not None, "Required property 'batch_job_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_job_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The batch job parameters of the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-batch.html#cfn-apptest-testcase-batch-batchjobparameters
            '''
            result = self._values.get("batch_job_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def export_data_set_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The export data set names of the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-batch.html#cfn-apptest-testcase-batch-exportdatasetnames
            '''
            result = self._values.get("export_data_set_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.CloudFormationActionProperty",
        jsii_struct_bases=[],
        name_mapping={"resource": "resource", "action_type": "actionType"},
    )
    class CloudFormationActionProperty:
        def __init__(
            self,
            *,
            resource: builtins.str,
            action_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the CloudFormation action.

            :param resource: The resource of the CloudFormation action.
            :param action_type: The action type of the CloudFormation action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-cloudformationaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                cloud_formation_action_property = apptest.CfnTestCase.CloudFormationActionProperty(
                    resource="resource",
                
                    # the properties below are optional
                    action_type="actionType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78e388b0bdedf30c61617f56e880ca6fde56252f230c4ae15398e7f9e212b149)
                check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
                check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource": resource,
            }
            if action_type is not None:
                self._values["action_type"] = action_type

        @builtins.property
        def resource(self) -> builtins.str:
            '''The resource of the CloudFormation action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-cloudformationaction.html#cfn-apptest-testcase-cloudformationaction-resource
            '''
            result = self._values.get("resource")
            assert result is not None, "Required property 'resource' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def action_type(self) -> typing.Optional[builtins.str]:
            '''The action type of the CloudFormation action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-cloudformationaction.html#cfn-apptest-testcase-cloudformationaction-actiontype
            '''
            result = self._values.get("action_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudFormationActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.CompareActionProperty",
        jsii_struct_bases=[],
        name_mapping={"input": "input", "output": "output"},
    )
    class CompareActionProperty:
        def __init__(
            self,
            *,
            input: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.InputProperty", typing.Dict[builtins.str, typing.Any]]],
            output: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.OutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Compares the action.

            :param input: The input of the compare action.
            :param output: The output of the compare action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-compareaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                compare_action_property = apptest.CfnTestCase.CompareActionProperty(
                    input=apptest.CfnTestCase.InputProperty(
                        file=apptest.CfnTestCase.InputFileProperty(
                            file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                                database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                    source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                        capture_tool="captureTool",
                                        type="type"
                                    ),
                                    target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                        capture_tool="captureTool",
                                        type="type"
                                    )
                                ),
                                data_sets=[apptest.CfnTestCase.DataSetProperty(
                                    ccsid="ccsid",
                                    format="format",
                                    length=123,
                                    name="name",
                                    type="type"
                                )]
                            ),
                            source_location="sourceLocation",
                            target_location="targetLocation"
                        )
                    ),
                
                    # the properties below are optional
                    output=apptest.CfnTestCase.OutputProperty(
                        file=apptest.CfnTestCase.OutputFileProperty(
                            file_location="fileLocation"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2dc4b8e39cea5f0693b421e043e7fe695a5071e9da674e0b21910651149bec6)
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input": input,
            }
            if output is not None:
                self._values["output"] = output

        @builtins.property
        def input(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.InputProperty"]:
            '''The input of the compare action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-compareaction.html#cfn-apptest-testcase-compareaction-input
            '''
            result = self._values.get("input")
            assert result is not None, "Required property 'input' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.InputProperty"], result)

        @builtins.property
        def output(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.OutputProperty"]]:
            '''The output of the compare action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-compareaction.html#cfn-apptest-testcase-compareaction-output
            '''
            result = self._values.get("output")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.OutputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CompareActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.DataSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ccsid": "ccsid",
            "format": "format",
            "length": "length",
            "name": "name",
            "type": "type",
        },
    )
    class DataSetProperty:
        def __init__(
            self,
            *,
            ccsid: builtins.str,
            format: builtins.str,
            length: jsii.Number,
            name: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Defines a data set.

            :param ccsid: The CCSID of the data set.
            :param format: The format of the data set.
            :param length: The length of the data set.
            :param name: The name of the data set.
            :param type: The type of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                data_set_property = apptest.CfnTestCase.DataSetProperty(
                    ccsid="ccsid",
                    format="format",
                    length=123,
                    name="name",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d3400848ac30aaffccbe005fccaa7513d639cff48d08f645573a9df55178db62)
                check_type(argname="argument ccsid", value=ccsid, expected_type=type_hints["ccsid"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
                check_type(argname="argument length", value=length, expected_type=type_hints["length"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ccsid": ccsid,
                "format": format,
                "length": length,
                "name": name,
                "type": type,
            }

        @builtins.property
        def ccsid(self) -> builtins.str:
            '''The CCSID of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html#cfn-apptest-testcase-dataset-ccsid
            '''
            result = self._values.get("ccsid")
            assert result is not None, "Required property 'ccsid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def format(self) -> builtins.str:
            '''The format of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html#cfn-apptest-testcase-dataset-format
            '''
            result = self._values.get("format")
            assert result is not None, "Required property 'format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def length(self) -> jsii.Number:
            '''The length of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html#cfn-apptest-testcase-dataset-length
            '''
            result = self._values.get("length")
            assert result is not None, "Required property 'length' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html#cfn-apptest-testcase-dataset-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the data set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-dataset.html#cfn-apptest-testcase-dataset-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.DatabaseCDCProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_metadata": "sourceMetadata",
            "target_metadata": "targetMetadata",
        },
    )
    class DatabaseCDCProperty:
        def __init__(
            self,
            *,
            source_metadata: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.SourceDatabaseMetadataProperty", typing.Dict[builtins.str, typing.Any]]],
            target_metadata: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.TargetDatabaseMetadataProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines the Change Data Capture (CDC) of the database.

            :param source_metadata: The source metadata of the database CDC.
            :param target_metadata: The target metadata of the database CDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-databasecdc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                database_cDCProperty = apptest.CfnTestCase.DatabaseCDCProperty(
                    source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                        capture_tool="captureTool",
                        type="type"
                    ),
                    target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                        capture_tool="captureTool",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d36ecfd05054aba47bc762f73ceae48c439f201dd893fd3061a68183286a719)
                check_type(argname="argument source_metadata", value=source_metadata, expected_type=type_hints["source_metadata"])
                check_type(argname="argument target_metadata", value=target_metadata, expected_type=type_hints["target_metadata"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_metadata": source_metadata,
                "target_metadata": target_metadata,
            }

        @builtins.property
        def source_metadata(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.SourceDatabaseMetadataProperty"]:
            '''The source metadata of the database CDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-databasecdc.html#cfn-apptest-testcase-databasecdc-sourcemetadata
            '''
            result = self._values.get("source_metadata")
            assert result is not None, "Required property 'source_metadata' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.SourceDatabaseMetadataProperty"], result)

        @builtins.property
        def target_metadata(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.TargetDatabaseMetadataProperty"]:
            '''The target metadata of the database CDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-databasecdc.html#cfn-apptest-testcase-databasecdc-targetmetadata
            '''
            result = self._values.get("target_metadata")
            assert result is not None, "Required property 'target_metadata' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.TargetDatabaseMetadataProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseCDCProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.FileMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"database_cdc": "databaseCdc", "data_sets": "dataSets"},
    )
    class FileMetadataProperty:
        def __init__(
            self,
            *,
            database_cdc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.DatabaseCDCProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            data_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.DataSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies a file metadata.

            :param database_cdc: The database CDC of the file metadata.
            :param data_sets: The data sets of the file metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-filemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                file_metadata_property = apptest.CfnTestCase.FileMetadataProperty(
                    database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                        source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                            capture_tool="captureTool",
                            type="type"
                        ),
                        target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                            capture_tool="captureTool",
                            type="type"
                        )
                    ),
                    data_sets=[apptest.CfnTestCase.DataSetProperty(
                        ccsid="ccsid",
                        format="format",
                        length=123,
                        name="name",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8de2285ee9d01f8af93180870ea0c2f5ecdd6beff2742d493c28c8d7fc1ee71f)
                check_type(argname="argument database_cdc", value=database_cdc, expected_type=type_hints["database_cdc"])
                check_type(argname="argument data_sets", value=data_sets, expected_type=type_hints["data_sets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if database_cdc is not None:
                self._values["database_cdc"] = database_cdc
            if data_sets is not None:
                self._values["data_sets"] = data_sets

        @builtins.property
        def database_cdc(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.DatabaseCDCProperty"]]:
            '''The database CDC of the file metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-filemetadata.html#cfn-apptest-testcase-filemetadata-databasecdc
            '''
            result = self._values.get("database_cdc")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.DatabaseCDCProperty"]], result)

        @builtins.property
        def data_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTestCase.DataSetProperty"]]]]:
            '''The data sets of the file metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-filemetadata.html#cfn-apptest-testcase-filemetadata-datasets
            '''
            result = self._values.get("data_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTestCase.DataSetProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.InputFileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_metadata": "fileMetadata",
            "source_location": "sourceLocation",
            "target_location": "targetLocation",
        },
    )
    class InputFileProperty:
        def __init__(
            self,
            *,
            file_metadata: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.FileMetadataProperty", typing.Dict[builtins.str, typing.Any]]],
            source_location: builtins.str,
            target_location: builtins.str,
        ) -> None:
            '''Specifies the input file.

            :param file_metadata: The file metadata of the input file.
            :param source_location: The source location of the input file.
            :param target_location: The target location of the input file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-inputfile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                input_file_property = apptest.CfnTestCase.InputFileProperty(
                    file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                        database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                            source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                capture_tool="captureTool",
                                type="type"
                            ),
                            target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                capture_tool="captureTool",
                                type="type"
                            )
                        ),
                        data_sets=[apptest.CfnTestCase.DataSetProperty(
                            ccsid="ccsid",
                            format="format",
                            length=123,
                            name="name",
                            type="type"
                        )]
                    ),
                    source_location="sourceLocation",
                    target_location="targetLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f28601f160942e96b555754f69dce46666a04754e210669650325280dafe4984)
                check_type(argname="argument file_metadata", value=file_metadata, expected_type=type_hints["file_metadata"])
                check_type(argname="argument source_location", value=source_location, expected_type=type_hints["source_location"])
                check_type(argname="argument target_location", value=target_location, expected_type=type_hints["target_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_metadata": file_metadata,
                "source_location": source_location,
                "target_location": target_location,
            }

        @builtins.property
        def file_metadata(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.FileMetadataProperty"]:
            '''The file metadata of the input file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-inputfile.html#cfn-apptest-testcase-inputfile-filemetadata
            '''
            result = self._values.get("file_metadata")
            assert result is not None, "Required property 'file_metadata' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.FileMetadataProperty"], result)

        @builtins.property
        def source_location(self) -> builtins.str:
            '''The source location of the input file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-inputfile.html#cfn-apptest-testcase-inputfile-sourcelocation
            '''
            result = self._values.get("source_location")
            assert result is not None, "Required property 'source_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_location(self) -> builtins.str:
            '''The target location of the input file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-inputfile.html#cfn-apptest-testcase-inputfile-targetlocation
            '''
            result = self._values.get("target_location")
            assert result is not None, "Required property 'target_location' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputFileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.InputProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file"},
    )
    class InputProperty:
        def __init__(
            self,
            *,
            file: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.InputFileProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the input.

            :param file: The file in the input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                input_property = apptest.CfnTestCase.InputProperty(
                    file=apptest.CfnTestCase.InputFileProperty(
                        file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                            database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                    capture_tool="captureTool",
                                    type="type"
                                ),
                                target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                    capture_tool="captureTool",
                                    type="type"
                                )
                            ),
                            data_sets=[apptest.CfnTestCase.DataSetProperty(
                                ccsid="ccsid",
                                format="format",
                                length=123,
                                name="name",
                                type="type"
                            )]
                        ),
                        source_location="sourceLocation",
                        target_location="targetLocation"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c40dc1b73b144ba165a7b730bcde38e82d41aaeaab3afe13e4c264c2bacea8c3)
                check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file": file,
            }

        @builtins.property
        def file(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.InputFileProperty"]:
            '''The file in the input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-input.html#cfn-apptest-testcase-input-file
            '''
            result = self._values.get("file")
            assert result is not None, "Required property 'file' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.InputFileProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.M2ManagedActionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "force_stop": "forceStop",
            "import_data_set_location": "importDataSetLocation",
        },
    )
    class M2ManagedActionPropertiesProperty:
        def __init__(
            self,
            *,
            force_stop: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            import_data_set_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the AWS Mainframe Modernization managed action properties.

            :param force_stop: Force stops the AWS Mainframe Modernization managed action properties.
            :param import_data_set_location: The import data set location of the AWS Mainframe Modernization managed action properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedactionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                m2_managed_action_properties_property = apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                    force_stop=False,
                    import_data_set_location="importDataSetLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aff55b515e89331733a8ca8c4623288706ae79f94b2490ad50cdb7175419e644)
                check_type(argname="argument force_stop", value=force_stop, expected_type=type_hints["force_stop"])
                check_type(argname="argument import_data_set_location", value=import_data_set_location, expected_type=type_hints["import_data_set_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if force_stop is not None:
                self._values["force_stop"] = force_stop
            if import_data_set_location is not None:
                self._values["import_data_set_location"] = import_data_set_location

        @builtins.property
        def force_stop(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Force stops the AWS Mainframe Modernization managed action properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedactionproperties.html#cfn-apptest-testcase-m2managedactionproperties-forcestop
            '''
            result = self._values.get("force_stop")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def import_data_set_location(self) -> typing.Optional[builtins.str]:
            '''The import data set location of the AWS Mainframe Modernization managed action properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedactionproperties.html#cfn-apptest-testcase-m2managedactionproperties-importdatasetlocation
            '''
            result = self._values.get("import_data_set_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M2ManagedActionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.M2ManagedApplicationActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_type": "actionType",
            "resource": "resource",
            "properties": "properties",
        },
    )
    class M2ManagedApplicationActionProperty:
        def __init__(
            self,
            *,
            action_type: builtins.str,
            resource: builtins.str,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.M2ManagedActionPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the AWS Mainframe Modernization managed application action.

            :param action_type: The action type of the AWS Mainframe Modernization managed application action.
            :param resource: The resource of the AWS Mainframe Modernization managed application action.
            :param properties: The properties of the AWS Mainframe Modernization managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedapplicationaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                m2_managed_application_action_property = apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                    action_type="actionType",
                    resource="resource",
                
                    # the properties below are optional
                    properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                        force_stop=False,
                        import_data_set_location="importDataSetLocation"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f85973754bf13c76a3e2a3b4f358eeb66b15c5bfc88d5b29fc330839fcdd4d8e)
                check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
                check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_type": action_type,
                "resource": resource,
            }
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def action_type(self) -> builtins.str:
            '''The action type of the AWS Mainframe Modernization managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedapplicationaction.html#cfn-apptest-testcase-m2managedapplicationaction-actiontype
            '''
            result = self._values.get("action_type")
            assert result is not None, "Required property 'action_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource(self) -> builtins.str:
            '''The resource of the AWS Mainframe Modernization managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedapplicationaction.html#cfn-apptest-testcase-m2managedapplicationaction-resource
            '''
            result = self._values.get("resource")
            assert result is not None, "Required property 'resource' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2ManagedActionPropertiesProperty"]]:
            '''The properties of the AWS Mainframe Modernization managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2managedapplicationaction.html#cfn-apptest-testcase-m2managedapplicationaction-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2ManagedActionPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M2ManagedApplicationActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.M2NonManagedApplicationActionProperty",
        jsii_struct_bases=[],
        name_mapping={"action_type": "actionType", "resource": "resource"},
    )
    class M2NonManagedApplicationActionProperty:
        def __init__(
            self,
            *,
            action_type: builtins.str,
            resource: builtins.str,
        ) -> None:
            '''Specifies the AWS Mainframe Modernization non-managed application action.

            :param action_type: The action type of the AWS Mainframe Modernization non-managed application action.
            :param resource: The resource of the AWS Mainframe Modernization non-managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2nonmanagedapplicationaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                m2_non_managed_application_action_property = apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                    action_type="actionType",
                    resource="resource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9e48f9d87d696062223660256adb542d5d3a507fd31fc3bd02ac988f477784e)
                check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
                check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_type": action_type,
                "resource": resource,
            }

        @builtins.property
        def action_type(self) -> builtins.str:
            '''The action type of the AWS Mainframe Modernization non-managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2nonmanagedapplicationaction.html#cfn-apptest-testcase-m2nonmanagedapplicationaction-actiontype
            '''
            result = self._values.get("action_type")
            assert result is not None, "Required property 'action_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource(self) -> builtins.str:
            '''The resource of the AWS Mainframe Modernization non-managed application action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-m2nonmanagedapplicationaction.html#cfn-apptest-testcase-m2nonmanagedapplicationaction-resource
            '''
            result = self._values.get("resource")
            assert result is not None, "Required property 'resource' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "M2NonManagedApplicationActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.MainframeActionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"dms_task_arn": "dmsTaskArn"},
    )
    class MainframeActionPropertiesProperty:
        def __init__(
            self,
            *,
            dms_task_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the mainframe action properties.

            :param dms_task_arn: The DMS task ARN of the mainframe action properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                mainframe_action_properties_property = apptest.CfnTestCase.MainframeActionPropertiesProperty(
                    dms_task_arn="dmsTaskArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f3cbaf004a4c64cc1ecc337ba06f597a70cd172a30d84319dd2546797c61870)
                check_type(argname="argument dms_task_arn", value=dms_task_arn, expected_type=type_hints["dms_task_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dms_task_arn is not None:
                self._values["dms_task_arn"] = dms_task_arn

        @builtins.property
        def dms_task_arn(self) -> typing.Optional[builtins.str]:
            '''The DMS task ARN of the mainframe action properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactionproperties.html#cfn-apptest-testcase-mainframeactionproperties-dmstaskarn
            '''
            result = self._values.get("dms_task_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MainframeActionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.MainframeActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_type": "actionType",
            "resource": "resource",
            "properties": "properties",
        },
    )
    class MainframeActionProperty:
        def __init__(
            self,
            *,
            action_type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.MainframeActionTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            resource: builtins.str,
            properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.MainframeActionPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the mainframe action.

            :param action_type: The action type of the mainframe action.
            :param resource: The resource of the mainframe action.
            :param properties: The properties of the mainframe action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                mainframe_action_property = apptest.CfnTestCase.MainframeActionProperty(
                    action_type=apptest.CfnTestCase.MainframeActionTypeProperty(
                        batch=apptest.CfnTestCase.BatchProperty(
                            batch_job_name="batchJobName",
                
                            # the properties below are optional
                            batch_job_parameters={
                                "batch_job_parameters_key": "batchJobParameters"
                            },
                            export_data_set_names=["exportDataSetNames"]
                        ),
                        tn3270=apptest.CfnTestCase.TN3270Property(
                            script=apptest.CfnTestCase.ScriptProperty(
                                script_location="scriptLocation",
                                type="type"
                            ),
                
                            # the properties below are optional
                            export_data_set_names=["exportDataSetNames"]
                        )
                    ),
                    resource="resource",
                
                    # the properties below are optional
                    properties=apptest.CfnTestCase.MainframeActionPropertiesProperty(
                        dms_task_arn="dmsTaskArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91394299bcb7ab56e13f3a27df57457d3656de73e850c88cf377f8170b9c4f30)
                check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
                check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_type": action_type,
                "resource": resource,
            }
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def action_type(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionTypeProperty"]:
            '''The action type of the mainframe action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeaction.html#cfn-apptest-testcase-mainframeaction-actiontype
            '''
            result = self._values.get("action_type")
            assert result is not None, "Required property 'action_type' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionTypeProperty"], result)

        @builtins.property
        def resource(self) -> builtins.str:
            '''The resource of the mainframe action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeaction.html#cfn-apptest-testcase-mainframeaction-resource
            '''
            result = self._values.get("resource")
            assert result is not None, "Required property 'resource' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionPropertiesProperty"]]:
            '''The properties of the mainframe action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeaction.html#cfn-apptest-testcase-mainframeaction-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MainframeActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.MainframeActionTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"batch": "batch", "tn3270": "tn3270"},
    )
    class MainframeActionTypeProperty:
        def __init__(
            self,
            *,
            batch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.BatchProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tn3270: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.TN3270Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the mainframe action type.

            :param batch: The batch of the mainframe action type.
            :param tn3270: The tn3270 port of the mainframe action type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactiontype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                mainframe_action_type_property = apptest.CfnTestCase.MainframeActionTypeProperty(
                    batch=apptest.CfnTestCase.BatchProperty(
                        batch_job_name="batchJobName",
                
                        # the properties below are optional
                        batch_job_parameters={
                            "batch_job_parameters_key": "batchJobParameters"
                        },
                        export_data_set_names=["exportDataSetNames"]
                    ),
                    tn3270=apptest.CfnTestCase.TN3270Property(
                        script=apptest.CfnTestCase.ScriptProperty(
                            script_location="scriptLocation",
                            type="type"
                        ),
                
                        # the properties below are optional
                        export_data_set_names=["exportDataSetNames"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96c6abe4da2018f3b1e24e02a9f038e914b06af61954a6a784abe93d7594a104)
                check_type(argname="argument batch", value=batch, expected_type=type_hints["batch"])
                check_type(argname="argument tn3270", value=tn3270, expected_type=type_hints["tn3270"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if batch is not None:
                self._values["batch"] = batch
            if tn3270 is not None:
                self._values["tn3270"] = tn3270

        @builtins.property
        def batch(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.BatchProperty"]]:
            '''The batch of the mainframe action type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactiontype.html#cfn-apptest-testcase-mainframeactiontype-batch
            '''
            result = self._values.get("batch")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.BatchProperty"]], result)

        @builtins.property
        def tn3270(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.TN3270Property"]]:
            '''The tn3270 port of the mainframe action type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-mainframeactiontype.html#cfn-apptest-testcase-mainframeactiontype-tn3270
            '''
            result = self._values.get("tn3270")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.TN3270Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MainframeActionTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.OutputFileProperty",
        jsii_struct_bases=[],
        name_mapping={"file_location": "fileLocation"},
    )
    class OutputFileProperty:
        def __init__(
            self,
            *,
            file_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an output file.

            :param file_location: The file location of the output file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-outputfile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                output_file_property = apptest.CfnTestCase.OutputFileProperty(
                    file_location="fileLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c44a4f0d7883cc89887a1f9471deac980763e434ca5bbcc95da77e162acd8fa3)
                check_type(argname="argument file_location", value=file_location, expected_type=type_hints["file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if file_location is not None:
                self._values["file_location"] = file_location

        @builtins.property
        def file_location(self) -> typing.Optional[builtins.str]:
            '''The file location of the output file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-outputfile.html#cfn-apptest-testcase-outputfile-filelocation
            '''
            result = self._values.get("file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={"file": "file"},
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            file: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.OutputFileProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies an output.

            :param file: The file of the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                output_property = apptest.CfnTestCase.OutputProperty(
                    file=apptest.CfnTestCase.OutputFileProperty(
                        file_location="fileLocation"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__695167e76c7b9eee0044387c1a700ef5312fd67eb8cc5d53caeed30fb9d21c1e)
                check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file": file,
            }

        @builtins.property
        def file(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.OutputFileProperty"]:
            '''The file of the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-output.html#cfn-apptest-testcase-output-file
            '''
            result = self._values.get("file")
            assert result is not None, "Required property 'file' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.OutputFileProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.ResourceActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_formation_action": "cloudFormationAction",
            "m2_managed_application_action": "m2ManagedApplicationAction",
            "m2_non_managed_application_action": "m2NonManagedApplicationAction",
        },
    )
    class ResourceActionProperty:
        def __init__(
            self,
            *,
            cloud_formation_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.CloudFormationActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            m2_managed_application_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.M2ManagedApplicationActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            m2_non_managed_application_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.M2NonManagedApplicationActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies a resource action.

            :param cloud_formation_action: The CloudFormation action of the resource action.
            :param m2_managed_application_action: The AWS Mainframe Modernization managed application action of the resource action.
            :param m2_non_managed_application_action: The AWS Mainframe Modernization non-managed application action of the resource action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-resourceaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                resource_action_property = apptest.CfnTestCase.ResourceActionProperty(
                    cloud_formation_action=apptest.CfnTestCase.CloudFormationActionProperty(
                        resource="resource",
                
                        # the properties below are optional
                        action_type="actionType"
                    ),
                    m2_managed_application_action=apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                        action_type="actionType",
                        resource="resource",
                
                        # the properties below are optional
                        properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                            force_stop=False,
                            import_data_set_location="importDataSetLocation"
                        )
                    ),
                    m2_non_managed_application_action=apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                        action_type="actionType",
                        resource="resource"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3e4bb03de2d729d83767f3875aa711f32328989ac1ceb9eb12d1d6eea68ef8f7)
                check_type(argname="argument cloud_formation_action", value=cloud_formation_action, expected_type=type_hints["cloud_formation_action"])
                check_type(argname="argument m2_managed_application_action", value=m2_managed_application_action, expected_type=type_hints["m2_managed_application_action"])
                check_type(argname="argument m2_non_managed_application_action", value=m2_non_managed_application_action, expected_type=type_hints["m2_non_managed_application_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_formation_action is not None:
                self._values["cloud_formation_action"] = cloud_formation_action
            if m2_managed_application_action is not None:
                self._values["m2_managed_application_action"] = m2_managed_application_action
            if m2_non_managed_application_action is not None:
                self._values["m2_non_managed_application_action"] = m2_non_managed_application_action

        @builtins.property
        def cloud_formation_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.CloudFormationActionProperty"]]:
            '''The CloudFormation action of the resource action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-resourceaction.html#cfn-apptest-testcase-resourceaction-cloudformationaction
            '''
            result = self._values.get("cloud_formation_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.CloudFormationActionProperty"]], result)

        @builtins.property
        def m2_managed_application_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2ManagedApplicationActionProperty"]]:
            '''The AWS Mainframe Modernization managed application action of the resource action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-resourceaction.html#cfn-apptest-testcase-resourceaction-m2managedapplicationaction
            '''
            result = self._values.get("m2_managed_application_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2ManagedApplicationActionProperty"]], result)

        @builtins.property
        def m2_non_managed_application_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2NonManagedApplicationActionProperty"]]:
            '''The AWS Mainframe Modernization non-managed application action of the resource action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-resourceaction.html#cfn-apptest-testcase-resourceaction-m2nonmanagedapplicationaction
            '''
            result = self._values.get("m2_non_managed_application_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.M2NonManagedApplicationActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.ScriptProperty",
        jsii_struct_bases=[],
        name_mapping={"script_location": "scriptLocation", "type": "type"},
    )
    class ScriptProperty:
        def __init__(
            self,
            *,
            script_location: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Specifies the script.

            :param script_location: The script location of the scripts.
            :param type: The type of the scripts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-script.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                script_property = apptest.CfnTestCase.ScriptProperty(
                    script_location="scriptLocation",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9491bc096d573fc68bb677f00cad6e1b7ed657a3325e8791453c1dd26760783b)
                check_type(argname="argument script_location", value=script_location, expected_type=type_hints["script_location"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "script_location": script_location,
                "type": type,
            }

        @builtins.property
        def script_location(self) -> builtins.str:
            '''The script location of the scripts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-script.html#cfn-apptest-testcase-script-scriptlocation
            '''
            result = self._values.get("script_location")
            assert result is not None, "Required property 'script_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the scripts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-script.html#cfn-apptest-testcase-script-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.SourceDatabaseMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"capture_tool": "captureTool", "type": "type"},
    )
    class SourceDatabaseMetadataProperty:
        def __init__(self, *, capture_tool: builtins.str, type: builtins.str) -> None:
            '''Specifies the source database metadata.

            :param capture_tool: The capture tool of the source database metadata.
            :param type: The type of the source database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-sourcedatabasemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                source_database_metadata_property = apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                    capture_tool="captureTool",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5109465ec6db43508a3040f8bf0c54ad2138ec7b18876e19b096bfe966b7e69)
                check_type(argname="argument capture_tool", value=capture_tool, expected_type=type_hints["capture_tool"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capture_tool": capture_tool,
                "type": type,
            }

        @builtins.property
        def capture_tool(self) -> builtins.str:
            '''The capture tool of the source database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-sourcedatabasemetadata.html#cfn-apptest-testcase-sourcedatabasemetadata-capturetool
            '''
            result = self._values.get("capture_tool")
            assert result is not None, "Required property 'capture_tool' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the source database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-sourcedatabasemetadata.html#cfn-apptest-testcase-sourcedatabasemetadata-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceDatabaseMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.StepActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compare_action": "compareAction",
            "mainframe_action": "mainframeAction",
            "resource_action": "resourceAction",
        },
    )
    class StepActionProperty:
        def __init__(
            self,
            *,
            compare_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.CompareActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mainframe_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.MainframeActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resource_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.ResourceActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies a step action.

            :param compare_action: The compare action of the step action.
            :param mainframe_action: The mainframe action of the step action.
            :param resource_action: The resource action of the step action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-stepaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                step_action_property = apptest.CfnTestCase.StepActionProperty(
                    compare_action=apptest.CfnTestCase.CompareActionProperty(
                        input=apptest.CfnTestCase.InputProperty(
                            file=apptest.CfnTestCase.InputFileProperty(
                                file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                                    database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                        source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                            capture_tool="captureTool",
                                            type="type"
                                        ),
                                        target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                            capture_tool="captureTool",
                                            type="type"
                                        )
                                    ),
                                    data_sets=[apptest.CfnTestCase.DataSetProperty(
                                        ccsid="ccsid",
                                        format="format",
                                        length=123,
                                        name="name",
                                        type="type"
                                    )]
                                ),
                                source_location="sourceLocation",
                                target_location="targetLocation"
                            )
                        ),
                
                        # the properties below are optional
                        output=apptest.CfnTestCase.OutputProperty(
                            file=apptest.CfnTestCase.OutputFileProperty(
                                file_location="fileLocation"
                            )
                        )
                    ),
                    mainframe_action=apptest.CfnTestCase.MainframeActionProperty(
                        action_type=apptest.CfnTestCase.MainframeActionTypeProperty(
                            batch=apptest.CfnTestCase.BatchProperty(
                                batch_job_name="batchJobName",
                
                                # the properties below are optional
                                batch_job_parameters={
                                    "batch_job_parameters_key": "batchJobParameters"
                                },
                                export_data_set_names=["exportDataSetNames"]
                            ),
                            tn3270=apptest.CfnTestCase.TN3270Property(
                                script=apptest.CfnTestCase.ScriptProperty(
                                    script_location="scriptLocation",
                                    type="type"
                                ),
                
                                # the properties below are optional
                                export_data_set_names=["exportDataSetNames"]
                            )
                        ),
                        resource="resource",
                
                        # the properties below are optional
                        properties=apptest.CfnTestCase.MainframeActionPropertiesProperty(
                            dms_task_arn="dmsTaskArn"
                        )
                    ),
                    resource_action=apptest.CfnTestCase.ResourceActionProperty(
                        cloud_formation_action=apptest.CfnTestCase.CloudFormationActionProperty(
                            resource="resource",
                
                            # the properties below are optional
                            action_type="actionType"
                        ),
                        m2_managed_application_action=apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                            action_type="actionType",
                            resource="resource",
                
                            # the properties below are optional
                            properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                                force_stop=False,
                                import_data_set_location="importDataSetLocation"
                            )
                        ),
                        m2_non_managed_application_action=apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                            action_type="actionType",
                            resource="resource"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d032b095aec0a923a2a2276cfba87076f22f92cbaa96be53c20ace6c9c654fdf)
                check_type(argname="argument compare_action", value=compare_action, expected_type=type_hints["compare_action"])
                check_type(argname="argument mainframe_action", value=mainframe_action, expected_type=type_hints["mainframe_action"])
                check_type(argname="argument resource_action", value=resource_action, expected_type=type_hints["resource_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compare_action is not None:
                self._values["compare_action"] = compare_action
            if mainframe_action is not None:
                self._values["mainframe_action"] = mainframe_action
            if resource_action is not None:
                self._values["resource_action"] = resource_action

        @builtins.property
        def compare_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.CompareActionProperty"]]:
            '''The compare action of the step action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-stepaction.html#cfn-apptest-testcase-stepaction-compareaction
            '''
            result = self._values.get("compare_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.CompareActionProperty"]], result)

        @builtins.property
        def mainframe_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionProperty"]]:
            '''The mainframe action of the step action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-stepaction.html#cfn-apptest-testcase-stepaction-mainframeaction
            '''
            result = self._values.get("mainframe_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.MainframeActionProperty"]], result)

        @builtins.property
        def resource_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.ResourceActionProperty"]]:
            '''The resource action of the step action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-stepaction.html#cfn-apptest-testcase-stepaction-resourceaction
            '''
            result = self._values.get("resource_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTestCase.ResourceActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.StepProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "description": "description",
        },
    )
    class StepProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.StepActionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a step.

            :param action: The action of the step.
            :param name: The name of the step.
            :param description: The description of the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-step.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                step_property = apptest.CfnTestCase.StepProperty(
                    action=apptest.CfnTestCase.StepActionProperty(
                        compare_action=apptest.CfnTestCase.CompareActionProperty(
                            input=apptest.CfnTestCase.InputProperty(
                                file=apptest.CfnTestCase.InputFileProperty(
                                    file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                                        database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                            source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                                capture_tool="captureTool",
                                                type="type"
                                            ),
                                            target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                                capture_tool="captureTool",
                                                type="type"
                                            )
                                        ),
                                        data_sets=[apptest.CfnTestCase.DataSetProperty(
                                            ccsid="ccsid",
                                            format="format",
                                            length=123,
                                            name="name",
                                            type="type"
                                        )]
                                    ),
                                    source_location="sourceLocation",
                                    target_location="targetLocation"
                                )
                            ),
                
                            # the properties below are optional
                            output=apptest.CfnTestCase.OutputProperty(
                                file=apptest.CfnTestCase.OutputFileProperty(
                                    file_location="fileLocation"
                                )
                            )
                        ),
                        mainframe_action=apptest.CfnTestCase.MainframeActionProperty(
                            action_type=apptest.CfnTestCase.MainframeActionTypeProperty(
                                batch=apptest.CfnTestCase.BatchProperty(
                                    batch_job_name="batchJobName",
                
                                    # the properties below are optional
                                    batch_job_parameters={
                                        "batch_job_parameters_key": "batchJobParameters"
                                    },
                                    export_data_set_names=["exportDataSetNames"]
                                ),
                                tn3270=apptest.CfnTestCase.TN3270Property(
                                    script=apptest.CfnTestCase.ScriptProperty(
                                        script_location="scriptLocation",
                                        type="type"
                                    ),
                
                                    # the properties below are optional
                                    export_data_set_names=["exportDataSetNames"]
                                )
                            ),
                            resource="resource",
                
                            # the properties below are optional
                            properties=apptest.CfnTestCase.MainframeActionPropertiesProperty(
                                dms_task_arn="dmsTaskArn"
                            )
                        ),
                        resource_action=apptest.CfnTestCase.ResourceActionProperty(
                            cloud_formation_action=apptest.CfnTestCase.CloudFormationActionProperty(
                                resource="resource",
                
                                # the properties below are optional
                                action_type="actionType"
                            ),
                            m2_managed_application_action=apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                                action_type="actionType",
                                resource="resource",
                
                                # the properties below are optional
                                properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                                    force_stop=False,
                                    import_data_set_location="importDataSetLocation"
                                )
                            ),
                            m2_non_managed_application_action=apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                                action_type="actionType",
                                resource="resource"
                            )
                        )
                    ),
                    name="name",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__693abf61935b40af6d279994a8215cbd6298c43e090f93aef648872426ba9439)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.StepActionProperty"]:
            '''The action of the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-step.html#cfn-apptest-testcase-step-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.StepActionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-step.html#cfn-apptest-testcase-step-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-step.html#cfn-apptest-testcase-step-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.TN3270Property",
        jsii_struct_bases=[],
        name_mapping={
            "script": "script",
            "export_data_set_names": "exportDataSetNames",
        },
    )
    class TN3270Property:
        def __init__(
            self,
            *,
            script: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTestCase.ScriptProperty", typing.Dict[builtins.str, typing.Any]]],
            export_data_set_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the TN3270 protocol.

            :param script: The script of the TN3270 protocol.
            :param export_data_set_names: The data set names of the TN3270 protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-tn3270.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                t_n3270_property = apptest.CfnTestCase.TN3270Property(
                    script=apptest.CfnTestCase.ScriptProperty(
                        script_location="scriptLocation",
                        type="type"
                    ),
                
                    # the properties below are optional
                    export_data_set_names=["exportDataSetNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9be2af67de11c7c1527c9ab1225496c360b31ec89b193994afe1085f5ddf487d)
                check_type(argname="argument script", value=script, expected_type=type_hints["script"])
                check_type(argname="argument export_data_set_names", value=export_data_set_names, expected_type=type_hints["export_data_set_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "script": script,
            }
            if export_data_set_names is not None:
                self._values["export_data_set_names"] = export_data_set_names

        @builtins.property
        def script(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTestCase.ScriptProperty"]:
            '''The script of the TN3270 protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-tn3270.html#cfn-apptest-testcase-tn3270-script
            '''
            result = self._values.get("script")
            assert result is not None, "Required property 'script' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTestCase.ScriptProperty"], result)

        @builtins.property
        def export_data_set_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The data set names of the TN3270 protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-tn3270.html#cfn-apptest-testcase-tn3270-exportdatasetnames
            '''
            result = self._values.get("export_data_set_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TN3270Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.TargetDatabaseMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"capture_tool": "captureTool", "type": "type"},
    )
    class TargetDatabaseMetadataProperty:
        def __init__(self, *, capture_tool: builtins.str, type: builtins.str) -> None:
            '''Specifies a target database metadata.

            :param capture_tool: The capture tool of the target database metadata.
            :param type: The type of the target database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-targetdatabasemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                target_database_metadata_property = apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                    capture_tool="captureTool",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a294d3841c7f78441bca4347b1a52c3d34715683c7ebe5ab5e8d2cb07c57de9)
                check_type(argname="argument capture_tool", value=capture_tool, expected_type=type_hints["capture_tool"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capture_tool": capture_tool,
                "type": type,
            }

        @builtins.property
        def capture_tool(self) -> builtins.str:
            '''The capture tool of the target database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-targetdatabasemetadata.html#cfn-apptest-testcase-targetdatabasemetadata-capturetool
            '''
            result = self._values.get("capture_tool")
            assert result is not None, "Required property 'capture_tool' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the target database metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-targetdatabasemetadata.html#cfn-apptest-testcase-targetdatabasemetadata-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetDatabaseMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apptest.CfnTestCase.TestCaseLatestVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status", "version": "version"},
    )
    class TestCaseLatestVersionProperty:
        def __init__(self, *, status: builtins.str, version: jsii.Number) -> None:
            '''Specifies the latest version of a test case.

            :param status: The status of the test case latest version.
            :param version: The version of the test case latest version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-testcaselatestversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apptest as apptest
                
                test_case_latest_version_property = apptest.CfnTestCase.TestCaseLatestVersionProperty(
                    status="status",
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f4c770ea457b4cd91039dd6060ef58f0f4231406f81979b98062ec9bcf66227)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
                "version": version,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of the test case latest version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-testcaselatestversion.html#cfn-apptest-testcase-testcaselatestversion-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> jsii.Number:
            '''The version of the test case latest version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apptest-testcase-testcaselatestversion.html#cfn-apptest-testcase-testcaselatestversion-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TestCaseLatestVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apptest.CfnTestCaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "steps": "steps",
        "description": "description",
        "tags": "tags",
    },
)
class CfnTestCaseProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.StepProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTestCase``.

        :param name: The name of the test case.
        :param steps: The steps in the test case.
        :param description: The description of the test case.
        :param tags: The specified tags of the test case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apptest as apptest
            
            cfn_test_case_props = apptest.CfnTestCaseProps(
                name="name",
                steps=[apptest.CfnTestCase.StepProperty(
                    action=apptest.CfnTestCase.StepActionProperty(
                        compare_action=apptest.CfnTestCase.CompareActionProperty(
                            input=apptest.CfnTestCase.InputProperty(
                                file=apptest.CfnTestCase.InputFileProperty(
                                    file_metadata=apptest.CfnTestCase.FileMetadataProperty(
                                        database_cdc=apptest.CfnTestCase.DatabaseCDCProperty(
                                            source_metadata=apptest.CfnTestCase.SourceDatabaseMetadataProperty(
                                                capture_tool="captureTool",
                                                type="type"
                                            ),
                                            target_metadata=apptest.CfnTestCase.TargetDatabaseMetadataProperty(
                                                capture_tool="captureTool",
                                                type="type"
                                            )
                                        ),
                                        data_sets=[apptest.CfnTestCase.DataSetProperty(
                                            ccsid="ccsid",
                                            format="format",
                                            length=123,
                                            name="name",
                                            type="type"
                                        )]
                                    ),
                                    source_location="sourceLocation",
                                    target_location="targetLocation"
                                )
                            ),
            
                            # the properties below are optional
                            output=apptest.CfnTestCase.OutputProperty(
                                file=apptest.CfnTestCase.OutputFileProperty(
                                    file_location="fileLocation"
                                )
                            )
                        ),
                        mainframe_action=apptest.CfnTestCase.MainframeActionProperty(
                            action_type=apptest.CfnTestCase.MainframeActionTypeProperty(
                                batch=apptest.CfnTestCase.BatchProperty(
                                    batch_job_name="batchJobName",
            
                                    # the properties below are optional
                                    batch_job_parameters={
                                        "batch_job_parameters_key": "batchJobParameters"
                                    },
                                    export_data_set_names=["exportDataSetNames"]
                                ),
                                tn3270=apptest.CfnTestCase.TN3270Property(
                                    script=apptest.CfnTestCase.ScriptProperty(
                                        script_location="scriptLocation",
                                        type="type"
                                    ),
            
                                    # the properties below are optional
                                    export_data_set_names=["exportDataSetNames"]
                                )
                            ),
                            resource="resource",
            
                            # the properties below are optional
                            properties=apptest.CfnTestCase.MainframeActionPropertiesProperty(
                                dms_task_arn="dmsTaskArn"
                            )
                        ),
                        resource_action=apptest.CfnTestCase.ResourceActionProperty(
                            cloud_formation_action=apptest.CfnTestCase.CloudFormationActionProperty(
                                resource="resource",
            
                                # the properties below are optional
                                action_type="actionType"
                            ),
                            m2_managed_application_action=apptest.CfnTestCase.M2ManagedApplicationActionProperty(
                                action_type="actionType",
                                resource="resource",
            
                                # the properties below are optional
                                properties=apptest.CfnTestCase.M2ManagedActionPropertiesProperty(
                                    force_stop=False,
                                    import_data_set_location="importDataSetLocation"
                                )
                            ),
                            m2_non_managed_application_action=apptest.CfnTestCase.M2NonManagedApplicationActionProperty(
                                action_type="actionType",
                                resource="resource"
                            )
                        )
                    ),
                    name="name",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0102711c9306b53678129775395001b31372e5a003401d98d2cae036d61dc66b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "steps": steps,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the test case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html#cfn-apptest-testcase-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTestCase.StepProperty]]]:
        '''The steps in the test case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html#cfn-apptest-testcase-steps
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTestCase.StepProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the test case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html#cfn-apptest-testcase-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The specified tags of the test case.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apptest-testcase.html#cfn-apptest-testcase-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTestCaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnTestCase",
    "CfnTestCaseProps",
]

publication.publish()

def _typecheckingstub__b54328fdade9df4505a5f85498cf53fc62e7fc59a222ac471d1a63974ed7f0a5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.StepProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224090306333e2fc48135738c3d25b5e41f34e68b81b058fbfb26e7eda0deb3b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b44c10d3df56f34cf8ff918478ccaaa747cba69c96444d92b98e0cf0cb4efe1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b8945362e3fa289aad135a767811c67a4cdb45010d2377c0fb6dd670ca829f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a0c6d80a2bab21c010f9956a7784691e07a0d6ed782a3cc4f9fe81b470a060(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTestCase.StepProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d3be2bb2b7f3fe2d6ec231a15d229997932dffe177165c78ec826c8431cca3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8acfd7d3d54fa56bbe1ab5b9bc79609eaccb189083fe4b8cc7217ad659a8e7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fbc9e8380b6b0f7acb2ff9ce8665660f1341dbe513e19f269854edf36bf947(
    *,
    batch_job_name: builtins.str,
    batch_job_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    export_data_set_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e388b0bdedf30c61617f56e880ca6fde56252f230c4ae15398e7f9e212b149(
    *,
    resource: builtins.str,
    action_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2dc4b8e39cea5f0693b421e043e7fe695a5071e9da674e0b21910651149bec6(
    *,
    input: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.InputProperty, typing.Dict[builtins.str, typing.Any]]],
    output: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.OutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3400848ac30aaffccbe005fccaa7513d639cff48d08f645573a9df55178db62(
    *,
    ccsid: builtins.str,
    format: builtins.str,
    length: jsii.Number,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d36ecfd05054aba47bc762f73ceae48c439f201dd893fd3061a68183286a719(
    *,
    source_metadata: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.SourceDatabaseMetadataProperty, typing.Dict[builtins.str, typing.Any]]],
    target_metadata: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.TargetDatabaseMetadataProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de2285ee9d01f8af93180870ea0c2f5ecdd6beff2742d493c28c8d7fc1ee71f(
    *,
    database_cdc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.DatabaseCDCProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.DataSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28601f160942e96b555754f69dce46666a04754e210669650325280dafe4984(
    *,
    file_metadata: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.FileMetadataProperty, typing.Dict[builtins.str, typing.Any]]],
    source_location: builtins.str,
    target_location: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40dc1b73b144ba165a7b730bcde38e82d41aaeaab3afe13e4c264c2bacea8c3(
    *,
    file: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.InputFileProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff55b515e89331733a8ca8c4623288706ae79f94b2490ad50cdb7175419e644(
    *,
    force_stop: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    import_data_set_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85973754bf13c76a3e2a3b4f358eeb66b15c5bfc88d5b29fc330839fcdd4d8e(
    *,
    action_type: builtins.str,
    resource: builtins.str,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.M2ManagedActionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e48f9d87d696062223660256adb542d5d3a507fd31fc3bd02ac988f477784e(
    *,
    action_type: builtins.str,
    resource: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3cbaf004a4c64cc1ecc337ba06f597a70cd172a30d84319dd2546797c61870(
    *,
    dms_task_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91394299bcb7ab56e13f3a27df57457d3656de73e850c88cf377f8170b9c4f30(
    *,
    action_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.MainframeActionTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    resource: builtins.str,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.MainframeActionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c6abe4da2018f3b1e24e02a9f038e914b06af61954a6a784abe93d7594a104(
    *,
    batch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.BatchProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tn3270: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.TN3270Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44a4f0d7883cc89887a1f9471deac980763e434ca5bbcc95da77e162acd8fa3(
    *,
    file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695167e76c7b9eee0044387c1a700ef5312fd67eb8cc5d53caeed30fb9d21c1e(
    *,
    file: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.OutputFileProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4bb03de2d729d83767f3875aa711f32328989ac1ceb9eb12d1d6eea68ef8f7(
    *,
    cloud_formation_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.CloudFormationActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    m2_managed_application_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.M2ManagedApplicationActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    m2_non_managed_application_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.M2NonManagedApplicationActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9491bc096d573fc68bb677f00cad6e1b7ed657a3325e8791453c1dd26760783b(
    *,
    script_location: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5109465ec6db43508a3040f8bf0c54ad2138ec7b18876e19b096bfe966b7e69(
    *,
    capture_tool: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d032b095aec0a923a2a2276cfba87076f22f92cbaa96be53c20ace6c9c654fdf(
    *,
    compare_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.CompareActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mainframe_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.MainframeActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.ResourceActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693abf61935b40af6d279994a8215cbd6298c43e090f93aef648872426ba9439(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.StepActionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be2af67de11c7c1527c9ab1225496c360b31ec89b193994afe1085f5ddf487d(
    *,
    script: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.ScriptProperty, typing.Dict[builtins.str, typing.Any]]],
    export_data_set_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a294d3841c7f78441bca4347b1a52c3d34715683c7ebe5ab5e8d2cb07c57de9(
    *,
    capture_tool: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4c770ea457b4cd91039dd6060ef58f0f4231406f81979b98062ec9bcf66227(
    *,
    status: builtins.str,
    version: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0102711c9306b53678129775395001b31372e5a003401d98d2cae036d61dc66b(
    *,
    name: builtins.str,
    steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTestCase.StepProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
