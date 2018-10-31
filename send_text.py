from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "YOUR ACCOUNT_SID"
# Your Auth Token from twilio.com/console
auth_token  = "YOUR AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+######", 
    from_="+######",
    body="PYTHON IS FUN!")

print(message.sid)
