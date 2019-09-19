using System;
using System.Threading;
using System.Threading.Tasks;

using Apache.NMS;

using McMaster.Extensions.CommandLineUtils;

using Amazon.SimpleSystemsManagement;
using Amazon.SimpleSystemsManagement.Model;


namespace AmazonMQDotNet
{
    class MessageCounter
    {
        public int count = 0;
    }
    class Program
    {
        protected static ITextMessage message = null;
        protected static AutoResetEvent semaphore = new AutoResetEvent(false);
        protected static TimeSpan receiveTimeout = TimeSpan.FromSeconds(1000);
        static async Task<string> GetUserPassword()
        {
            string retVal = "";
            var region = Amazon.RegionEndpoint.USEast1;

            var request = new GetParameterRequest()
            {
                Name = "MQBrokerUserPassword"
            };

            using (var client = new AmazonSimpleSystemsManagementClient(region))
            {
                try
                {
                    var response = await client.GetParameterAsync(request);
                    retVal = response.Parameter.Value;
                }
                catch (Exception ex)
                {
                    Console.Error.WriteLine($"Error occurred: {ex.Message}");
                }
            }
            return retVal;
        }

        protected static void OnMessage(IMessage receivedMsg)
        {
            message = receivedMsg as ITextMessage;
            Console.WriteLine(string.Format("Recvied message {0}",  message.Text));
        }

        public static int Main(string[] args)
        {
            var app = new CommandLineApplication();
            MessageCounter counter = new MessageCounter();

            var optionURL = app.Option("--url <BROKER_URL>", "Broker URL", CommandOptionType.SingleValue).IsRequired();

            var optionUser = app.Option("--user <BROKER_USER>", "Broker user-id", CommandOptionType.SingleValue);

            var optionPassword = app.Option("--password <BROKER_PASSWORD>", "Broker password", CommandOptionType.SingleValue);

            var optionMode = app.Option("--mode <sender_or_receiver>", "App mode", CommandOptionType.SingleValue).IsRequired();

            var optionType = app.Option("--type <queue_or_topic>", "Destination Type", CommandOptionType.SingleValue).IsRequired();

            var optionDest = app.Option("--destination <DEST_NAME>", "Destination name", CommandOptionType.SingleValue).IsRequired();

            var optionCliName = app.Option("--name <CLIENT_NAME>", "Client name", CommandOptionType.SingleValue).IsRequired();

            var optionInterval = app.Option<int>("--interval <milliseconds>", "Time delay between messages", CommandOptionType.SingleValue);

            var optionNotPersistent = app.Option<bool>("--notPersistent <true_or_false>", "Persistent or Non Persistent messages", CommandOptionType.SingleValue);

            var optionTTL = app.Option<int>("--ttl <milliseconds>", "Message expiry time", CommandOptionType.SingleValue);

            app.OnExecute(() =>
            {
                string temp = GetUserPassword().Result;

                string[] userPassword = temp.Split(',');
                string user = userPassword[0];
                string password = userPassword[1];

                Uri connecturi = new Uri(optionURL.Value());


                IConnectionFactory factory = new NMSConnectionFactory(connecturi);
                if (optionUser.HasValue())
                {
                    user = optionUser.Value();
                }
                if (optionPassword.HasValue())
                {
                    password = optionPassword.Value();
                }

                using (IConnection connection = factory.CreateConnection(user, password))
                {
                    connection.ClientId = "AmazonMQWorkshop - " + DateTimeOffset.Now.ToUnixTimeMilliseconds();
                    connection.Start();
                    IDestination destination;
                    using (ISession session = connection.CreateSession())
                    {
                        if (optionType.Value().Equals("queue"))
                        {
                            destination = session.GetQueue(optionDest.Value());
                        }
                        else
                        {
                            destination = session.GetTopic(optionDest.Value());
                        }
                        if (optionMode.Value().Equals("sender"))
                        {
                            using (IMessageProducer producer = session.CreateProducer(destination))
                            {
                                if (optionNotPersistent.HasValue())
                                {
                                    producer.DeliveryMode = MsgDeliveryMode.NonPersistent;
                                }
                                else
                                {
                                    producer.DeliveryMode = MsgDeliveryMode.Persistent;
                                }
                                while(true)
                                {
                                    string msgId = Guid.NewGuid().ToString();
                                    string message = string.Format("Mesage number {0}", counter.count++);
                                    ITextMessage request = session.CreateTextMessage(message);
                                    request.NMSMessageId = msgId;
                                    request.NMSCorrelationID = msgId;
                                    producer.Send(request);
                                    Console.WriteLine(string.Format("{0} Sent {1}", optionCliName.Value(), message));
                                    Thread.Sleep(1000);
                                }
                            }
                        } else
                        {
                            using (IMessageConsumer consumer = session.CreateConsumer(destination))
                            {
                                consumer.Listener += new MessageListener(OnMessage);
                                semaphore.WaitOne((int)receiveTimeout.TotalMilliseconds, true);
                            }
                        }
                    }
                }
            });
            return app.Execute(args);
        }
    }
}
