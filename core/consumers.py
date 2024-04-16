from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NotificationConsumers(AsyncJsonWebsocketConsumer):

    async def connect(self):
        # print("Connnected..")
        self.user = self.scope['user']
        if not self.user or not self.user.is_authenticated:
            await self.close()
        else:
            self.group_name = 'notification'
            try:
                await self.channel_layer.group_add(self.group_name, self.channel_name)
            except Exception as e:
                print(f"Error adding channel to group: {e}")
                await self.close()
            else:
                await self.accept()


    # async def receive_json(self, content, **kwargs):
    #     message = content['message']
    #     # print(message)
    #     # print(self.group_name)

    #     await self.channel_layer.group_send(self.group_name,{
    #         'type':'send.notification',
    #         'notification':message
    #     })

    async def send_notification(self, event):
        print(event)
        await self.send_json({
            'notification':event['notification']

        })

    
  
  



        
        