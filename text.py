from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC07f19a39b42b5c6daee2d8a4b8910e70"
# Your Auth Token from twilio.com/console
auth_token = "cdc90a5c80f4b70fb22547a53ed01694"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886911001163",
    from_="+18172412058",
    body="你好啊~~~~~~~~~~~~~"
)

print(message.sid)
