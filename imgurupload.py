from imgurpython import ImgurClient

client_id = "9c5e85230d3df52"
client_secret = "3d722b8f08385aef8ebb92c284457325ecb15347"

client = ImgurClient(client_id,client_secret)

response = client.upload_from_path("pog.png")
print(response["link"][:-1])
