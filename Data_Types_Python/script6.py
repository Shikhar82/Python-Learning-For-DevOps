text = "We are learning Python for DevOps"
new_text = text.split( )
#print ("Words:", new_text)
print(text.split( )[2])

arn = "arn:partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")
#print("Display arn:", new_arn)
print(arn.split("/")[1])

