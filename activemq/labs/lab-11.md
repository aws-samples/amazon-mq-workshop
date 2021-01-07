# Lab 11: Polyglot programming

In all the labs earlier, we used examples programs written in Java programming language. In this Lab, you will discover how you can use other popular programming languages to write applications on different OS platforms.

Amazon MQ client applications that either to produce or consume messages, can be written in multiple languages. Most popular of them all is Java, as the ecosystem supports a popular messaging abstraction specification called JMS, Java Messaging Specification.

## .Net/C# Clients

In this Lab, we will use .Net client written in C# that was cross-compiled for both Windows and Linux. Open the Cloud9 workspace named MQClient. If you continuing from Lab10, it's the same workspace.

If you want to continue in Linux, go to ```dotnet-client/linux-x64``` directory, if you want to run on Windows 10, go to ```dotnet-client/win10-x64```

**When using ActiveMQ NMS C#/.Net Library, BROKER_URL must be in the format activemq:ssl:hostname:port**

### Windows build using Visual Studio 
  - Open the csproj file 
  - Build debug or release binaries

### Windows build using command line 

```
dotnet build -c Debug -r win10-x64
dotnet publish -c Release -r win10-x64
```

### Windows run using dotnet

```
dotnet AmazonMQDotNet.dll --url <BROKER_URL> --mode sender --type queue --destination NMS.Q --name "Client1"
dotnet AmazonMQDotNet.dll --url <BROKER_URL> --mode receiver --type queue --destination NMS.Q 
```

### Windows run using EXE 

```
AmazonMQDotNet.exe --url <BROKER_URL> --mode sender --type queue --destination NMS.Q --name "Client1"
AmazonMQDotNet.exe --url <BROKER_URL> --mode receiver --type queue --destination NMS.Q 
```

For running C# programs, you need mono runtime which can be installed by logging in as root and following these [instructions](https://www.mono-project.com/download/stable/#download-lin-centos)

### Linux executable can be built on Windows machine

```
dotnet build -c Debug -r linux-x64
dotnet publish -c Release -r linux-x64
```

### Linux run using mono 

```
mono AmazonMQDotNet.dll --url <BROKER_URL> --mode sender --type queue --destination NMS.Q --name "Client1"
mono AmazonMQDotNet.dll --url <BROKER_URL> --mode receiver --type queue --destination NMS.Q 
```

### Linux using native executable 

```
AmazonMQDotNet --url <BROKER_URL> --mode sender --type queue --destination NMS.Q --name "Client1"
AmazonMQDotNet --url <BROKER_URL> --mode receiver --type queue --destination NMS.Q 
```

# Completion

Congratulations, you've successfully completed this Workshop! Please check again later as we add more labs and improve content in the existing labs. If you find any problems running this workshop or have suggestions for improvement, please raise an issue on Github.

Thank you!

[Return to the Workshop Landing page](/README.md)


