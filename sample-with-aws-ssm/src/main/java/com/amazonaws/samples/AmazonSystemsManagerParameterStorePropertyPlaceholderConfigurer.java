package com.amazonaws.samples;

import org.springframework.beans.factory.InitializingBean;
import org.springframework.util.Assert;

import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagement;
import com.amazonaws.services.simplesystemsmanagement.AWSSimpleSystemsManagementClientBuilder;
import com.amazonaws.services.simplesystemsmanagement.model.GetParameterRequest;

public class AmazonSystemsManagerParameterStorePropertyPlaceholderConfigurer implements InitializingBean {

    private String env;
    private AWSSimpleSystemsManagement ssmClient;

    public String lookup(String parameter) {
        return internalLookup(parameter, false);
    }

    public String lookup(String parameter, boolean decrypt) {
        return internalLookup(parameter, decrypt);
    }

    private String internalLookup(String parameter, boolean decrypt) {
        return ssmClient.getParameter(
            new GetParameterRequest()
                .withName("/" + env + "/" + parameter)
                .withWithDecryption(Boolean.TRUE))
                .getParameter().getValue();
    }

    public String getEnv() {
        return env;
    }

    public void setEnv(String env) {
        this.env = env;
    }

    @Override
    public void afterPropertiesSet()  {
        Assert.notNull(this.env, "env is required");

        ssmClient = AWSSimpleSystemsManagementClientBuilder.standard().build();
    }
}